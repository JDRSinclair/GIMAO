# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RoleViewSet, AvoirViewSet, FabricantViewSet, FournisseurViewSet,
    ConsommableViewSet, StockConsommableViewSet, ModeleEquipementViewSet,
    EstCompatibleViewSet, LieuViewSet, EquipementViewSet, ConstituerViewSet,
    InformationStatutViewSet, DocumentTechniqueViewSet, CorrespondreViewSet,
    DefaillanceViewSet, DocumentDefaillanceViewSet, InterventionViewSet,
    DocumentInterventionViewSet, get_lieux_hierarchy, UserViewSet,
    EquipementCreateView, DocumentTechniqueCreateView, EquipementDocumentationCreateAPIView,
    get_dernier_document_technique,
  
)

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
router.register(r'informationStatus', InformationStatutViewSet)
router.register(r'documentstechniques', DocumentTechniqueViewSet)
router.register(r'correspondres', CorrespondreViewSet)
router.register(r'defaillances', DefaillanceViewSet)
router.register(r'documentdefaillances', DocumentDefaillanceViewSet)
router.register(r'interventions', InterventionViewSet)
router.register(r'documentinterventions', DocumentInterventionViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('lieux-hierarchy/', get_lieux_hierarchy, name='lieux-hierarchy'),
    path('dernier-document-technique/', get_dernier_document_technique, name='dernier-document-technique'),
    path('equipements/<str:reference>/detail/', EquipementViewSet.as_view({'get': 'retrieve'}), name='equipement-detail'),
    path('fournisseurs', FournisseurViewSet, name='fournisseurs'),
    
    path('creer-equipement/', EquipementCreateView.as_view(), name='creer-equipement'),
    path('creer-document-technique/', DocumentTechniqueCreateView.as_view(), name='creer-document-technique'),
    path('jointure-equipement-document/', EquipementDocumentationCreateAPIView.as_view(), name='jointure-equipement-document'),

]