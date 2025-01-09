# api/serializers.py
from rest_framework import viewsets
from django.db.models import Prefetch
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myApp.models import (
    Role, Avoir, Fabricant, Fournisseur, Consommable, StockConsommable,
    ModeleEquipement, EstCompatible, Lieu, Equipement, Constituer,
    InformationStatut, DocumentTechnique, Correspondre, Defaillance,
    DocumentDefaillance, Intervention, DocumentIntervention
)
from .serializers import (
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
)

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

