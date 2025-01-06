from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet, AvoirViewSet, FabricantViewSet, FournisseurViewSet, ConsommableViewSet, StockConsommableViewSet, ModeleEquipementViewSet, EstCompatibleViewSet, LieuViewSet, EquipementViewSet, ConstituerViewSet, InformationMaintenanceViewSet, DocumentTechniqueViewSet, CorrespondreViewSet, DefaillanceViewSet, DocumentDefaillanceViewSet, InterventionViewSet, DocumentInterventionViewSet

router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'avoirs', AvoirViewSet)
router.register(r'fabricants', FabricantViewSet)
router.register(r'fournisseurs', FournisseurViewSet)
router.register(r'consommables', ConsommableViewSet)
router.register(r'stockconsommables', StockConsommableViewSet)
router.register(r'modeleequipements', ModeleEquipementViewSet)
router.register(r'estcompatibles', EstCompatibleViewSet)
router.register(r'lieux', LieuViewSet)
router.register(r'equipements', EquipementViewSet)
router.register(r'constituers', ConstituerViewSet)
router.register(r'informationmaintenances', InformationMaintenanceViewSet)
router.register(r'documentstechniques', DocumentTechniqueViewSet)
router.register(r'correspondres', CorrespondreViewSet)
router.register(r'defaillances', DefaillanceViewSet)
router.register(r'documentdefaillances', DocumentDefaillanceViewSet)
router.register(r'interventions', InterventionViewSet)
router.register(r'documentinterventions', DocumentInterventionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lieux/<int:pk>/sous-lieux/', LieuViewSet.as_view({'get': 'sous_lieux'}), name='lieu-sous-lieux'),
    path('lieux/<int:pk>/types-equipements/', LieuViewSet.as_view({'get': 'types_equipements'}), name='lieu-types-equipements'),
    path('lieux/<int:pk>/equipements/', LieuViewSet.as_view({'get': 'equipements_by_lieu_and_type'}), name='lieu-equipements'),
]
