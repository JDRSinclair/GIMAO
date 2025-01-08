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
    RoleSerializer, AvoirSerializer, FabricantSerializer, FournisseurSerializer,
    ConsommableSerializer, StockConsommableSerializer, ModeleEquipementSerializer,
    EstCompatibleSerializer, LieuSerializer, EquipementSerializer, ConstituerSerializer,
    InformationStatutSerializer, DocumentTechniqueSerializer, CorrespondreSerializer,
    DefaillanceSerializer, DocumentDefaillanceSerializer, InterventionSerializer,
    DocumentInterventionSerializer,EquipementDetailSerializer ,LieuHierarchySerializer
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

class EquipementViewSet(viewsets.ModelViewSet):
    queryset = Equipement.objects.all()
    lookup_field = 'reference'
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EquipementDetailSerializer
        return EquipementSerializer

    def get_queryset(self):
        if self.action == 'retrieve':
            return Equipement.objects.select_related(
                'lieu', 
                'modeleEquipement__fabricant', 
                'fournisseur', 
                'createurEquipement'
            ).prefetch_related(
                Prefetch('informationstatut_set', 
                         queryset=InformationStatut.objects.order_by('-dateChangement'),
                         to_attr='statuts'),
                Prefetch('defaillance_set', 
                         queryset=Defaillance.objects.prefetch_related(
                             'intervention_set',
                             'documentdefaillance_set',
                             'intervention_set__documentintervention_set'
                         )),
                Prefetch('modeleEquipement__estcompatible_set__consommable', 
                         queryset=Consommable.objects.all()),
                Prefetch('modeleEquipement__correspondre_set__documentTechnique',
                         queryset=DocumentTechnique.objects.all()),
            )
        return Equipement.objects.all()

    def get_object(self):
        reference = self.kwargs.get('reference')
        try:
            obj = self.get_queryset().get(reference=reference)
            if hasattr(obj, 'statuts') and obj.statuts:
                obj.dernier_statut = obj.statuts[0]
            else:
                obj.dernier_statut = obj.informationstatut_set.order_by('-dateChangement').first()
            return obj
        except Equipement.DoesNotExist:
            raise NotFound(f"Aucun équipement trouvé avec la référence {reference}")

@api_view(['GET'])
def get_lieux_hierarchy(request):
    top_level_lieux = Lieu.objects.filter(lieuParent__isnull=True)
    serializer = LieuHierarchySerializer(top_level_lieux, many=True)
    return Response(serializer.data)