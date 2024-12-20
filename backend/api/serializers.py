# api/serializers.py
from rest_framework import serializers
from myApp.models import Role, Avoir, Fabricant, Fournisseur, Consommable, StockConsommable, ModeleEquipement, EstCompatible, Lieu, Equipement, Constituer, InformationMaintenance, DocumentTechnique, Correspondre, Defaillance, DocumentDefaillance, Intervention, DocumentIntervention

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

class InformationMaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationMaintenance
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
