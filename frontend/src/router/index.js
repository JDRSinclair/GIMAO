import { createRouter, createWebHistory } from 'vue-router'

// ---------------------------------------------------------------
import TableauDeBord from '@/views/TableauDeBord/TableauDeBord.vue'
import Equipements from '@/views/Equipements/Equipements.vue'
import Maintenances from '@/views/Maintenances/Maintenances.vue'
import Techniciens from '@/views/Techniciens/Techniciens.vue'
import GestionComptes from '@/views/GestionComptes/GestionComptes.vue'
import Commandes from '@/views/Commandes/Commandes.vue'
import Stocks from '@/views/Stocks/Stocks.vue'
<<<<<<< Updated upstream
<<<<<<< Updated upstream
import Signalements from '@/views/Signalements/Signalements.vue'
import CloturerIntervention from '@/views/TableauDeBord/CloturerIntervention.vue'
=======
=======
>>>>>>> Stashed changes
import Signalements from '@/views/Failures/Defaillances.vue'


// ---------------------------------------------------------------
import AfficherIntervention from '@/views/Interventions/AfficherIntervention.vue'
import CreerIntervention from '@/views/Interventions/CreerIntervention.vue'
import AjouterDocumentIntervention from '@/views/Interventions/AjouterDocumentIntervention.vue'

// ------------------------------------------------------------------
import AfficherEquipement from '@/views/Equipements/AfficherEquipement.vue'
import CreerEquipement from '@/views/Equipements/CreerEquipement.vue'

// ------------------------------------------------------------------
import CreateFailure from '@/views/Failures/CreateFailure.vue'
import FailureDetail from '@/views/Failures/FailureDetail.vue'
import AddDocumentFailure from '@/views/Failures/AddDocumentFailure.vue'

// ------------------------------------------------------------------

import DataManagement from '@/views/DataManagement/DataManagement.vue'

import CreateLocation from '@/views/DataManagement/Locations/CreateLocation.vue'
import LocationList from '@/views/DataManagement/Locations/LocationList.vue'
import LocationDetail from '@/views/DataManagement/Locations/LocationDetail.vue'

import CreateSupplier from '@/views/DataManagement/Suppliers/CreateSupplier.vue'
import SupplierList from '@/views/DataManagement/Suppliers/SupplierList.vue'
import SupplierDetail from '@/views/DataManagement/Suppliers/SupplierDetail.vue'

import CreateManufacturer from '@/views/DataManagement/Manufacturers/CreateManufacturer.vue'
import ManufacturerList from '@/views/DataManagement/Manufacturers/ManufacturerList.vue'
import ManufacturerDetail from '@/views/DataManagement/Manufacturers/ManufacturerDetail.vue'

<<<<<<< Updated upstream
import ConsummableList from '@/views/DataManagement/Consummables/ConsummableList.vue'
import CreateConsummable from '@/views/DataManagement/Consummables/CreateConsummable.vue'
import ConsummableDetail from '@/views/DataManagement/Consummables/ConsummableDetail.vue'

>>>>>>> Stashed changes
=======
import ConsumableList from '@/views/DataManagement/Consumables/ConsumableList.vue'
import CreateConsumable from '@/views/DataManagement/Consumables/CreateConsumable.vue'
import ConsumableDetail from '@/views/DataManagement/Consumables/ConsumableDetail.vue'

>>>>>>> Stashed changes



const routes = [
  {
    path: '/',
    name: 'TableauDeBord',
    component: TableauDeBord,
    meta: { title: 'Tableau de Bord' }
  },
<<<<<<< Updated upstream
  {
    path: '/equipements',
    name: 'Equipements',
    component: Equipements,
    meta: { title: 'Equipement' }
  },
  {
    path: '/ajouterEquipement',
    name: 'AjouterEquipement',
    component: AjouterEquipement,
    meta: { title: 'AjouterEquipement' }
  },
  {
    path: '/equipement/:id',
    name: 'VisualiserEquipement',
    component: VisualiserEquipement,
    meta: { title: 'VisualiserEquipement' }
  },
  {
    path: '/maintenances',
    name: 'Maintenances',
    component: Maintenances,
    meta: { title: 'Maintenances' }
  },
=======

>>>>>>> Stashed changes
  {
    path: '/techniciens',
    name: 'Techniciens',
    component: Techniciens,
    meta: { title: 'Techniciens' }
  },
  
  {
    path: '/gestion-comptes',
    name: 'GestionComptes',
    component: GestionComptes,
    meta: { title: 'Gestion des Comptes' }
  },

  {
    path: '/commandes',
    name: 'Commandes',
    component: Commandes,
    meta: { title: 'Commandes' }
    
  },

  {
    path: '/stocks',
    name: 'Stocks',
    component: Stocks,
    meta: { title: 'Stocks' }
  },
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
=======
>>>>>>> Stashed changes



  // Consommables ------------------------------------------------------------------

  {
<<<<<<< Updated upstream
    path: '/ConsummableList',
    name: 'ConsummableList',
    component: ConsummableList,
=======
    path: '/ConsumableList',
    name: 'ConsumableList',
    component: ConsumableList,
>>>>>>> Stashed changes
    meta: { title: 'Consommables' }
  },
  
  {
<<<<<<< Updated upstream
    path: '/CreateConsummable',
    name: 'CreateConsummable',
    component: CreateConsummable,
=======
    path: '/CreateConsumable',
    name: 'CreateConsumable',
    component: CreateConsumable,
>>>>>>> Stashed changes
    meta: { title: 'Creer un Consommable' }
  },

  {
<<<<<<< Updated upstream
    path: '/ConsummableDetail/:id',
    name: 'ConsummableDetail',
    component: ConsummableDetail,
=======
    path: '/ConsumableDetail/:id',
    name: 'ConsumableDetail',
    component: ConsumableDetail,
>>>>>>> Stashed changes
    props: true,
    meta: { title: 'Détails d\'un consommable' }
  },


    // Fabricants ------------------------------------------------------------------

  {
    path: '/ManufacturerList',
    name: 'ManufacturerList',
    component: ManufacturerList,
    meta: { title: 'Fabricants' }
  },
  
  {
    path: '/CreateManufacturer',
    name: 'CreateManufacturer',
    component: CreateManufacturer,
    meta: { title: 'Creer un Fabricant' }
  },

  {
    path: '/ManufacturerDetail/:id',
    name: 'ManufacturerDetail',
    component: ManufacturerDetail,
    props: true,
    meta: { title: 'Détails d\'un fabricant' }
  },


    // Fournisseurs ------------------------------------------------------------------

  {
    path: '/SupplierList',
    name: 'SupplierList',
    component: SupplierList,
    meta: { title: 'Fournisseurs' }
  },

  {
    path: '/CreateSupplier',
    name: 'CreateSupplier',
    component: CreateSupplier,
    meta: { title: 'Creer un Fournisseur' }
  },

  {
    path: '/SupplierDetail/:id',
    name: 'SupplierDetail',
    component: SupplierDetail,
    props: true,
    meta: { title: 'Détails d\'un Fournisseur' }
  },



  // GestionDonnees ---------------------------------------------------------------

  {
    path: '/DataManagement',
    name: 'DataManagement',
    component: DataManagement,
    meta: { title: 'Gestion des données' }
  },

  // Interventions ---------------------------------------------------------------

  {
    path: '/maintenances',
    name: 'Maintenances',
    component: Maintenances,
    meta: { title: 'Bon de travail' }
  },

  {
    path: '/intervention/:id',
    name: 'AfficherIntervention',
    component: AfficherIntervention,
    props: true, 
    meta: { title: 'Détails de l\'intervention' }
  },

  {
    path: '/defaillance/:id/creer-intervention/',
    name: 'CreerIntervention',
    component: CreerIntervention,
    meta: { title: 'Créer un bon de travail' }
  },

  {
    path: '/intervention/:id/ajouterDocument',
    name: 'AjouterDocumentIntervention',
    component: AjouterDocumentIntervention,
    props: true,
    meta: { title: 'Détails de l\'intervention' }
  },



  // Signalements ---------------------------------------------------------------

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
  {
    path: '/signalements',
    name: 'Signalements',
    component: Signalements,
<<<<<<< Updated upstream
    meta: { title: 'Signalements' }
  },

  {
<<<<<<< Updated upstream
    path: '/cloturer-interventions',
    name: 'CloturerIntervention',
    component: CloturerIntervention,
    meta: { title: 'CloturerIntervention' }
  }
=======
=======
    meta: { title: 'Demandes de bon de travail' }
  },

  // Equipements ---------------------------------------------------------------

  {
    path: '/equipements',
    name: 'Equipements',
    component: Equipements,
    meta: { title: 'Équipements' }
  },

  {
>>>>>>> Stashed changes
    path: '/equipement/:reference',
    name: 'AfficherEquipement',
    component: AfficherEquipement,
    props: true, 
    meta: { title: 'Descriptif de l\'équipement' }
  },

  {
    path: '/creer-Equipement',
    name: 'CreerEquipement',
    component: CreerEquipement,
    meta: { title: 'Ajouter Equipement' }
  },

  // Defaillance ---------------------------------------------------------------
  {
    path: '/CreateFailure/:equipementReference?',
    name: 'CreateFailure',
    component: CreateFailure,
    props: true,
    meta: { title: 'Demande de bon de travail' }
  },

  {
    path: '/Failure/:id',
    name: 'FailureDetail',
    component: FailureDetail,
    props: true,
    meta: { title: 'Details de la demande ' }
  },

  {
    path: '/Failure/:id/addDocument',
    name: 'AddDocumentFailure',
    component: AddDocumentFailure,
    props: true,
    meta: { title: 'Ajouter un document à la défaillance' }
  },

  // Lieux ---------------------------------------------------------------

  {
    path: '/LocationList',
    name: 'LocationList',
    component: LocationList,
    meta: { title: 'Lieux' }
  },
  
  {
    path: '/CreateLocation',
    name: 'CreateLocation',
    component: CreateLocation,
    meta: { title: 'Creer un lieu' }
  },

  {
    path: '/LocationDetail/:id',
    name: 'LocationDetail',
    component: LocationDetail,
    props: true,
    meta: { title: 'Détails d\'un lieu' }
  },



  

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router