# api/serializers.py
from rest_framework import viewsets
from django.db.models import Prefetch
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST


from myApp.models import (
    Role, Avoir, Fabricant, Fournisseur, Consommable, StockConsommable,
    ModeleEquipement, EstCompatible, Lieu, Equipement, Constituer,
    InformationStatut, DocumentTechnique, Correspondre, Defaillance,
    DocumentDefaillance, Intervention, DocumentIntervention
)
from .serializers import (
    UserSerializer,
    RoleSerializer,
    AvoirSerializer,
    FabricantSerializer,
    FournisseurSerializer,
    ConsommableSerializer,
    StockConsommableSerializer,
    ModeleEquipementSerializer,
    EstCompatibleSerializer,
    LieuSerializer,
    EquipementSerializer,
    ConstituerSerializer,
    InformationStatutSerializer,
    DocumentTechniqueSerializer,
    CorrespondreSerializer,
    DefaillanceSerializer,
    DocumentDefaillanceSerializer,
    InterventionSerializer,
    DocumentInterventionSerializer,

    EquipementDetailSerializer,
    LieuHierarchySerializer,
    EquipementAffichageSerializer,
    InterventionAfficherSerializer,
)

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class AvoirViewSet(viewsets.ModelViewSet):
    queryset = Avoir.objects.all()
    serializer_class = AvoirSerializer

class FabricantViewSet(viewsets.ModelViewSet):
    queryset = Fabricant.objects.all()
    serializer_class = FabricantSerializer

class FournisseurViewSet(viewsets.ModelViewSet):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

class ConsommableViewSet(viewsets.ModelViewSet):
    queryset = Consommable.objects.all()
    serializer_class = ConsommableSerializer

class StockConsommableViewSet(viewsets.ModelViewSet):
    queryset = StockConsommable.objects.all()
    serializer_class = StockConsommableSerializer

class ModeleEquipementViewSet(viewsets.ModelViewSet):
    queryset = ModeleEquipement.objects.all()
    serializer_class = ModeleEquipementSerializer

class EstCompatibleViewSet(viewsets.ModelViewSet):
    queryset = EstCompatible.objects.all()
    serializer_class = EstCompatibleSerializer

class LieuViewSet(viewsets.ModelViewSet):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer

class EquipementViewSet(viewsets.ModelViewSet):
    queryset = Equipement.objects.all()
    serializer_class = EquipementSerializer

class ConstituerViewSet(viewsets.ModelViewSet):
    queryset = Constituer.objects.all()
    serializer_class = ConstituerSerializer

class InformationStatutViewSet(viewsets.ModelViewSet):
    queryset = InformationStatut.objects.all()
    serializer_class = InformationStatutSerializer

class DocumentTechniqueViewSet(viewsets.ModelViewSet):
    queryset = DocumentTechnique.objects.all()
    serializer_class = DocumentTechniqueSerializer

class CorrespondreViewSet(viewsets.ModelViewSet):
    queryset = Correspondre.objects.all()
    serializer_class = CorrespondreSerializer

class DefaillanceViewSet(viewsets.ModelViewSet):
    queryset = Defaillance.objects.all()
    serializer_class = DefaillanceSerializer

class DocumentDefaillanceViewSet(viewsets.ModelViewSet):
    queryset = DocumentDefaillance.objects.all()
    serializer_class = DocumentDefaillanceSerializer

class InterventionViewSet(viewsets.ModelViewSet):
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer

class DocumentInterventionViewSet(viewsets.ModelViewSet):
    queryset = DocumentIntervention.objects.all()
    serializer_class = DocumentInterventionSerializer



# --------------------------------------------------------------------------


# Affichage des equipemnts de la page Equipements.vue
class EquipementDetailViewSet(viewsets.ModelViewSet):
    queryset = Equipement.objects.select_related('lieu', 'modeleEquipement')
    serializer_class = EquipementDetailSerializer
    lookup_field = 'reference'

    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            'createurEquipement',
            'fournisseur',
            Prefetch('informationstatut_set', 
                     queryset=InformationStatut.objects.order_by('-dateChangement'),
                     to_attr='statuts')
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

# Affichage de la hiérarchie des lieux (LieuxExplorer)
@api_view(['GET'])
def get_lieux_hierarchy(request):
    top_level_lieux = Lieu.objects.filter(lieuParent__isnull=True).prefetch_related('lieu_set')
    serializer = LieuHierarchySerializer(top_level_lieux, many=True, context={'request': request})
    return Response(serializer.data)


class EquipementAffichageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet pour l'affichage détaillé des informations d'un équipement.
    """
    queryset = Equipement.objects.all()
    lookup_field = 'reference'

    def get_serializer_class(self):
        """
        Utilise EquipementAffichageSerializer pour la vue détaillée, 
        sinon utilise EquipementSerializer.
        """
        if self.action == 'retrieve':
            return EquipementAffichageSerializer
        return EquipementSerializer

    def get_queryset(self):
        """
        Optimise la requête avec select_related et prefetch_related pour la vue détaillée.
        """
        if self.action == 'retrieve':
            return Equipement.objects.select_related(
                'lieu', 
                'modeleEquipement__fabricant', 
                'fournisseur', 
                'createurEquipement'
            ).prefetch_related(
                self._prefetch_statuts(),
                self._prefetch_defaillances(),
                self._prefetch_consommables(),
                self._prefetch_documents_techniques(),
            )
        return Equipement.objects.all()

    def _prefetch_statuts(self):
        """Méthode auxiliaire pour précharger les statuts."""
        return Prefetch(
            'informationstatut_set', 
            queryset=InformationStatut.objects.order_by('-dateChangement'),
            to_attr='statuts'
        )

    def _prefetch_defaillances(self):
        """Méthode auxiliaire pour précharger les défaillances et les données associées."""
        return Prefetch(
            'defaillance_set', 
            queryset=Defaillance.objects.prefetch_related(
                'intervention_set',
                'documentdefaillance_set',
                'intervention_set__documentintervention_set'
            )
        )

    def _prefetch_consommables(self):
        """Méthode auxiliaire pour précharger les consommables compatibles."""
        return Prefetch(
            'modeleEquipement__estcompatible_set__consommable', 
            queryset=Consommable.objects.all()
        )

    def _prefetch_documents_techniques(self):
        """Méthode auxiliaire pour précharger les documents techniques."""
        return Prefetch(
            'modeleEquipement__correspondre_set__documentTechnique',
            queryset=DocumentTechnique.objects.all()
        )

    def get_object(self):
        """
        Récupère l'objet équipement et ajoute le dernier statut.
        """
        reference = self.kwargs.get('reference')
        queryset = self.get_queryset()
        try:
            obj = queryset.get(reference=reference)
            self.check_object_permissions(self.request, obj)
            obj.dernier_statut = obj.statuts[0] if hasattr(obj, 'statuts') and obj.statuts else None
            return obj
        except Equipement.DoesNotExist:
            raise NotFound(f"Aucun équipement trouvé avec la référence {reference}")


class InterventionAfficherViewSet(viewsets.ModelViewSet):
    queryset = Intervention.objects.all()
    serializer_class = InterventionAfficherSerializer

