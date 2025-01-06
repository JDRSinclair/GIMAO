from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from myApp.models import Role, Avoir, Fabricant, Fournisseur, Consommable, StockConsommable, ModeleEquipement, EstCompatible, Lieu, Equipement, Constituer, InformationMaintenance, DocumentTechnique, Correspondre, Defaillance, DocumentDefaillance, Intervention, DocumentIntervention
from .serializers import RoleSerializer, AvoirSerializer, FabricantSerializer, FournisseurSerializer, ConsommableSerializer, StockConsommableSerializer, ModeleEquipementSerializer, EstCompatibleSerializer, LieuSerializer, EquipementSerializer, ConstituerSerializer, InformationMaintenanceSerializer, DocumentTechniqueSerializer, CorrespondreSerializer, DefaillanceSerializer, DocumentDefaillanceSerializer, InterventionSerializer, DocumentInterventionSerializer

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

    def get_queryset(self):
        if self.action == 'list':
            return Lieu.objects.filter(lieuParent__isnull=True)
        return super().get_queryset()

    @action(detail=True, methods=['get'])
    def sous_lieux(self, request, pk=None):
        lieu = self.get_object()
        sous_lieux = Lieu.objects.filter(lieuParent=lieu)
        serializer = LieuSerializer(sous_lieux, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def types_equipements(self, request, pk=None):
        lieu = self.get_object()
        types_equipements = ModeleEquipement.objects.filter(equipement__lieu__lieuParent=lieu).distinct()
        serializer = ModeleEquipementSerializer(types_equipements, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def equipements_by_lieu_and_type(self, request, pk=None):
        lieu = self.get_object()
        typeEquipementId = request.query_params.get('typeEquipementId')
        if typeEquipementId:
            type_equipement = ModeleEquipement.objects.get(id=typeEquipementId)
            equipements = Equipement.objects.filter(lieu__lieuParent=lieu, modeleEquipement=type_equipement)
        else:
            equipements = Equipement.objects.filter(lieu__lieuParent=lieu)
        serializer = EquipementSerializer(equipements, many=True)
        return Response(serializer.data)

class EquipementViewSet(viewsets.ModelViewSet):
    queryset = Equipement.objects.all()
    serializer_class = EquipementSerializer

class ConstituerViewSet(viewsets.ModelViewSet):
    queryset = Constituer.objects.all()
    serializer_class = ConstituerSerializer

class InformationMaintenanceViewSet(viewsets.ModelViewSet):
    queryset = InformationMaintenance.objects.all()
    serializer_class = InformationMaintenanceSerializer

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
