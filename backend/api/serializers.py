# api/serializers.py
from rest_framework import serializers
from django.db.models import Max
from django.contrib.auth.models import User
from myApp.models import (
    Role, Avoir, Fabricant, Fournisseur, Consommable, StockConsommable,
    ModeleEquipement, EstCompatible, Lieu, Equipement, Constituer,
    InformationStatut, DocumentTechnique, Correspondre, Defaillance,
    DocumentDefaillance, Intervention, DocumentIntervention
)

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class AvoirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avoir
        fields = '__all__'

class FabricantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricant
        fields = '__all__'

class ModeleEquipementDetailSerializer(serializers.ModelSerializer):
    fabricant = FabricantSerializer(read_only=True)

    class Meta:
        model = ModeleEquipement
        fields = '__all__'

class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = '__all__'

class ConsommableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consommable
        fields = '__all__'

class StockConsommableSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockConsommable
        fields = '__all__'

class ModeleEquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeleEquipement
        fields = '__all__'

class EstCompatibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstCompatible
        fields = '__all__'

class InformationStatutSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationStatut
        fields = '__all__'

class EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = '__all__'

class ConstituerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constituer
        fields = '__all__'

class DocumentTechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentTechnique
        fields = '__all__'

class DocumentTechniqueJointureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentTechnique
        fields = ['id']

class CorrespondreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correspondre
        fields = '__all__'

class DefaillanceSerializer(serializers.ModelSerializer):
    interventions = serializers.SerializerMethodField()

    class Meta:
        model = Defaillance
        fields = '__all__'

    def get_interventions(self, obj):
        from .serializers import InterventionSerializer
        return InterventionSerializer(obj.intervention_set.all(), many=True).data

class DocumentDefaillanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentDefaillance
        fields = '__all__'

class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = '__all__'

class DocumentInterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentIntervention
        fields = '__all__'

class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LieuHierarchySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Lieu
        fields = ['id', 'nomLieu', 'typeLieu', 'children']

    def get_children(self, obj):
        children = Lieu.objects.filter(lieuParent=obj)
        serializer = self.__class__(children, many=True)
        return serializer.data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['children']:
            representation.pop('children')
        return representation

class EquipementDetailSerializer(serializers.ModelSerializer):
    lieu = LieuSerializer(read_only=True)
    modeleEquipement = ModeleEquipementDetailSerializer(read_only=True)
    fournisseur = FournisseurSerializer(read_only=True)
    defaillances = serializers.SerializerMethodField()
    consommables_compatibles = serializers.SerializerMethodField()
    documents_techniques = serializers.SerializerMethodField()
    documents_defaillance = serializers.SerializerMethodField()
    documents_intervention = serializers.SerializerMethodField()
    dernier_statut = InformationStatutSerializer(read_only=True)

    class Meta:
        model = Equipement
        fields = ['reference', 'designation', 'lieu', 'modeleEquipement', 'fournisseur', 
                  'defaillances', 'consommables_compatibles', 
                  'documents_techniques', 'documents_defaillance', 'documents_intervention',
                  'dernier_statut']

    def get_interventions(self, obj):
        return InterventionSerializer(obj.defaillance_set.all().prefetch_related('intervention_set'), many=True).data

    def get_consommables_compatibles(self, obj):
        return ConsommableSerializer(obj.modeleEquipement.estcompatible_set.all().select_related('consommable'), many=True).data

    def get_documents_techniques(self, obj):
        # Récupérer les documents techniques via le modèle Correspondre
        correspondances = Correspondre.objects.filter(modeleEquipement=obj.modeleEquipement)
        documents_techniques = [correspondance.documentTechnique for correspondance in correspondances]
        return DocumentTechniqueSerializer(documents_techniques, many=True).data

    def get_documents_defaillance(self, obj):
        return DocumentDefaillanceSerializer(DocumentDefaillance.objects.filter(defaillance__equipement=obj), many=True).data

    def get_documents_intervention(self, obj):
        return DocumentInterventionSerializer(DocumentIntervention.objects.filter(intervention__defaillance__equipement=obj), many=True).data

    def get_defaillances(self, obj):
        return DefaillanceSerializer(obj.defaillance_set.all().prefetch_related('intervention_set'), many=True).data

    
    def get_dernier_statut(self, obj):
        dernier_statut = obj.informationstatut_set.order_by('-dateChangement').first()
        if dernier_statut:
            return {
                'statutEquipement': dernier_statut.statutEquipement,
                'dateChangement': dernier_statut.dateChangement,
                'ModificateurStatut': dernier_statut.ModificateurStatut.username if dernier_statut.ModificateurStatut else None
            }
        return None
