# api/serializers.py
from rest_framework import serializers
from django.db.models import Max
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

class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = '__all__'

class EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = '__all__'
        

class ConstituerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constituer
        fields = '__all__'

class InformationStatutSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationStatut
        fields = '__all__'

class DocumentTechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentTechnique
        fields = '__all__'

class CorrespondreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correspondre
        fields = '__all__'

class DefaillanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defaillance 
        fields = '__all__'

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
        


# -------------------------------------------------------------------------



class EquipementDetailSerializer(serializers.ModelSerializer):
    lieu = LieuSerializer(read_only=True)
    modeleEquipement = ModeleEquipementSerializer(read_only=True)
    statut = serializers.SerializerMethodField()

    class Meta:
        model = Equipement
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['lieu'] = LieuSerializer(instance.lieu).data
        representation['modeleEquipement'] = ModeleEquipementSerializer(instance.modeleEquipement).data
        return representation

    def get_statut(self, obj):
        dernier_statut = obj.informationstatut_set.order_by('-dateChangement').first()
        if dernier_statut:
            return {
                'statutEquipement': dernier_statut.statutEquipement,
                'dateChangement': dernier_statut.dateChangement,
                'ModificateurStatut': dernier_statut.ModificateurStatut.username if dernier_statut.ModificateurStatut else None
            }
        return None


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



