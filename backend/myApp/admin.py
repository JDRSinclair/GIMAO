from django.contrib import admin
from .models import (
    Role, Utilisateur, Avoir, Fabricant, Fournisseur, Consommable,
    StockConsommable, ModeleEquipement, EstCompatible, Lieu, Equipement,
    Constituer, InformationMaintenance, DocumentTechnique, Correspondre,
    Defaillance, DocumentDefaillance, Intervention, DocumentIntervention
)

# Enregistrer les modèles dans l'interface d'administration
admin.site.register(Role)
admin.site.register(Utilisateur)
admin.site.register(Avoir)
admin.site.register(Fabricant)
admin.site.register(Fournisseur)
admin.site.register(Consommable)
admin.site.register(StockConsommable)
admin.site.register(ModeleEquipement)
admin.site.register(EstCompatible)
admin.site.register(Lieu)
admin.site.register(Equipement)
admin.site.register(Constituer)
admin.site.register(InformationMaintenance)
admin.site.register(DocumentTechnique)
admin.site.register(Correspondre)
admin.site.register(Defaillance)
admin.site.register(DocumentDefaillance)
admin.site.register(Intervention)
admin.site.register(DocumentIntervention)
