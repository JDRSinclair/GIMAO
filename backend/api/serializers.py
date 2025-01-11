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



class EquipementAffichageSerializer(serializers.ModelSerializer):
    lieu = LieuSerializer(read_only=True)
    modeleEquipement = ModeleEquipementSerializer(read_only=True)
    fournisseur = FournisseurSerializer(read_only=True)

    fabricant = serializers.SerializerMethodField()
    dernier_statut = InformationStatutSerializer(read_only=True)

    list_defaillances = serializers.SerializerMethodField()
    list_interventions = serializers.SerializerMethodField()
    liste_consommables = serializers.SerializerMethodField()
    liste_consommables_compatibles = serializers.SerializerMethodField()
    list_documents_techniques = serializers.SerializerMethodField()
    list_documents_defaillance = serializers.SerializerMethodField()
    list_documents_intervention = serializers.SerializerMethodField()

    class Meta:
        model = Equipement
        fields = [
            # Valeurs de base
            'reference', 'designation', 'dateCreation', 'dateMiseEnService', 
            'prixAchat', 'lienImageEquipement', 'createurEquipement', 
            'lieu', 'modeleEquipement', 'fournisseur',
            'preventifGlissant', 'joursIntervalleMaintenance',
            
            # Valeurs à recuperation simple
            'fabricant', 'dernier_statut',
            
            # Valeurs à recuperation complexes/multiples
            'list_defaillances','list_interventions', 'liste_consommables', 'liste_consommables_compatibles',
            'list_documents_techniques', 'list_documents_defaillance', 'list_documents_intervention'
        ]

        depth = 1

    def get_fabricant(self, obj):
        if obj.modeleEquipement and obj.modeleEquipement.fabricant:
            fabricant = obj.modeleEquipement.fabricant
            return {
                "id": fabricant.id,
                "nomFabricant": fabricant.nomFabricant,
                "paysFabricant": fabricant.paysFabricant,
                "mailFabricant": fabricant.mailFabricant,
                "numTelephoneFabricant": fabricant.numTelephoneFabricant,
                "serviceApresVente": fabricant.serviceApresVente
            }
        return None

    def get_dernier_statut(self, obj):
        dernier_statut = obj.informationstatut_set.order_by('-dateChangement').first()
        if dernier_statut:
            return {
                'statutEquipement': dernier_statut.statutEquipement,
                'dateChangement': dernier_statut.dateChangement,
                'ModificateurStatut': dernier_statut.ModificateurStatut.username if dernier_statut.ModificateurStatut else None
            }
        return None

    def get_list_defaillances(self, obj):
        defaillances = Defaillance.objects.filter(equipement=obj)
        return [
            {
                "id": defaillance.id,
                "commentaireDefaillance": defaillance.commentaireDefaillance,
                "niveau": defaillance.niveau,
                "utilisateur": defaillance.utilisateur.id if defaillance.utilisateur else None,
                "equipement": defaillance.equipement.reference
            }
            for defaillance in defaillances
        ]
    
    def get_list_interventions(self, obj):
    interventions = Intervention.objects.filter(defaillance__equipement=obj).select_related('defaillance', 'createurIntervention', 'responsable')
    return [
        {
            "id": intervention.id,
            "nomIntervention": intervention.nomIntervention,
            "interventionCurative": intervention.interventionCurative,
            "dateAssignation": intervention.dateAssignation,
            "dateCloture": intervention.dateCloture,
            "dateDebutIntervention": intervention.dateDebutIntervention,
            "dateFinIntervention": intervention.dateFinIntervention,
            "tempsEstime": intervention.tempsEstime,
            "commentaireIntervention": intervention.commentaireIntervention,
            "defaillance": {
                "id": intervention.defaillance.id,
                "commentaireDefaillance": intervention.defaillance.commentaireDefaillance,
                "niveau": intervention.defaillance.niveau,
            },
            "createurIntervention": intervention.createurIntervention.username if intervention.createurIntervention else None,
            "responsable": intervention.responsable.username if intervention.responsable else None,
        }
        for intervention in interventions
    ]

    def get_liste_consommables(self, obj):
        consommables = Consommable.objects.filter(
            constituer__equipement__reference=obj.reference
        ).select_related('constituer')
        return [
            {
                "id": consommable.id,
                "nomConsommable": consommable.nomConsommable,
                "descriptionConsommable": consommable.descriptionConsommable,
                "quantite": consommable.constituer_set.get(equipement__reference=obj.reference).quantite
            }
            for consommable in consommables
        ]

    def get_liste_consommables_compatibles(self, obj):
        consommables_compatibles = Consommable.objects.filter(
            estcompatible__modeleEquipement=obj.modeleEquipement
        ).select_related('estcompatible')
        return [
            {
                "id": consommable.id,
                "nomConsommable": consommable.nomConsommable,
                "descriptionConsommable": consommable.descriptionConsommable,
                "quantiteMinimale": consommable.quantiteMinimale,
                "quantiteMaximale": consommable.quantiteMaximale,
                "unite": consommable.unite
            }
            for consommable in consommables_compatibles
        ]

    def get_documents_techniques(self, obj):
        correspondances = Correspondre.objects.filter(modeleEquipement=obj.modeleEquipement)
        documents_techniques = [correspondance.documentTechnique for correspondance in correspondances]
        return DocumentTechniqueSerializer(documents_techniques, many=True).data

    def get_documents_defaillance(self, obj):
        return DocumentDefaillanceSerializer(DocumentDefaillance.objects.filter(defaillance__equipement=obj), many=True).data

    def get_documents_intervention(self, obj):
        return DocumentInterventionSerializer(DocumentIntervention.objects.filter(intervention__defaillance__equipement=obj), many=True).data

    
    
    
