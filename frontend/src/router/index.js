import { createRouter, createWebHistory } from 'vue-router'

// ---------------------------------------------------------------
import TableauDeBord from '@/views/TableauDeBord/TableauDeBord.vue'
import Equipements from '@/views/Equipements/Equipements.vue'
import Maintenances from '@/views/Maintenances/Maintenances.vue'
import Techniciens from '@/views/Techniciens/Techniciens.vue'
import GestionComptes from '@/views/GestionComptes/GestionComptes.vue'
import Commandes from '@/views/Commandes/Commandes.vue'
import Stocks from '@/views/Stocks/Stocks.vue'
import Signalements from '@/views/Defaillances/Defaillances.vue'


// ---------------------------------------------------------------
import AfficherIntervention from '@/views/Interventions/AfficherIntervention.vue'
import CreerIntervention from '@/views/Interventions/CreerIntervention.vue'
import AjouterDocumentIntervention from '@/views/Interventions/AjouterDocumentIntervention.vue'

// ------------------------------------------------------------------
import AfficherEquipement from '@/views/Equipements/AfficherEquipement.vue'
import CreerEquipement from '@/views/Equipements/CreerEquipement.vue'

// ------------------------------------------------------------------
import CreerDefaillance from '@/views/Defaillances/CreerDefaillance.vue'
import AfficherDefaillance from '@/views/Defaillances/AfficherDefaillance.vue'
import AjouterDocumentDefaillance from '@/views/Defaillances/AjouterDocumentDefaillance.vue'

// ------------------------------------------------------------------

import GestionDonnees from '@/views/GestionDonnees/GestionDonnees.vue'

import CreerLieu from '@/views/GestionDonnees/Lieux/CreerLieu.vue'
import Lieux from '@/views/GestionDonnees/Lieux/Lieux.vue'
import AfficherLieu from '@/views/GestionDonnees/Lieux/AfficherLieu.vue'

import CreerFournisseur from '@/views/GestionDonnees/Fournisseurs/CreerFournisseur.vue'
import Fournisseurs from '@/views/GestionDonnees/Fournisseurs/Fournisseurs.vue'
import AfficherFournisseur from '@/views/GestionDonnees/Fournisseurs/AfficherFournisseur.vue'

import CreerFabricant from '@/views/GestionDonnees/Fabricants/CreerFabricant.vue'
import Fabricants from '@/views/GestionDonnees/Fabricants/Fabricants.vue'
import AfficherFabricant from '@/views/GestionDonnees/Fabricants/AfficherFabricant.vue'

import Consommables from '@/views/GestionDonnees/Consommables/Consommables.vue'
import CreerConsommable from '@/views/GestionDonnees/Consommables/CreerConsommable.vue'
import AfficherConsommable from '@/views/GestionDonnees/Consommables/AfficherConsommable.vue'




const routes = [
  {
    path: '/',
    name: 'TableauDeBord',
    component: TableauDeBord,
    meta: { title: 'Tableau de Bord' }
  },

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



  // Consommables ------------------------------------------------------------------

  {
    path: '/consommables',
    name: 'Consommables',
    component: Consommables,
    meta: { title: 'Consommables' }
  },
  
  {
    path: '/creer-consommable',
    name: 'CreerConsommable',
    component: CreerConsommable,
    meta: { title: 'Creer un Consommable' }
  },

  {
    path: '/afficher-consommable/:id',
    name: 'AfficherConsommable',
    component: AfficherConsommable,
    props: true,
    meta: { title: 'Détails d\'un consommable' }
  },


    // Fabricants ------------------------------------------------------------------

  {
    path: '/fabricants',
    name: 'Fabricants',
    component: Fabricants,
    meta: { title: 'Fabricants' }
  },
  
  {
    path: '/creer-fabricant',
    name: 'CreerFabricant',
    component: CreerFabricant,
    meta: { title: 'Creer un Fabricant' }
  },

  {
    path: '/afficher-fabricant/:id',
    name: 'AfficherFabricant',
    component: AfficherFabricant,
    props: true,
    meta: { title: 'Détails d\'un fabricant' }
  },


    // Fournisseurs ------------------------------------------------------------------

  {
    path: '/fournisseurs',
    name: 'Fournisseurs',
    component: Fournisseurs,
    meta: { title: 'Fournisseurs' }
  },

  {
    path: '/creer-fournisseur',
    name: 'CreerFournisseur',
    component: CreerFournisseur,
    meta: { title: 'Creer un Fournisseur' }
  },

  {
    path: '/afficher-fournisseur/:id',
    name: 'AfficherFournisseur',
    component: AfficherFournisseur,
    props: true,
    meta: { title: 'Détails d\'un Fournisseur' }
  },



  // GestionDonnees ---------------------------------------------------------------

  {
    path: '/gestion-donnees',
    name: 'GestionDonnees',
    component: GestionDonnees,
    meta: { title: 'Gestion des données' }
  },

  // Interventions ---------------------------------------------------------------

  {
    path: '/maintenances',
    name: 'Maintenances',
    component: Maintenances,
    meta: { title: 'Maintenances' }
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

  {
    path: '/signalements',
    name: 'Signalements',
    component: Signalements,
    meta: { title: 'Liste des signalements' }
  },

  // Equipements ---------------------------------------------------------------

  {
    path: '/equipements',
    name: 'Equipements',
    component: Equipements,
    meta: { title: 'Equipement' }
  },

  {
    path: '/equipement/:reference',
    name: 'AfficherEquipement',
    component: AfficherEquipement,
    props: true, 
    meta: { title: 'Afficher Equipement' }
  },

  {
    path: '/creerEquipement',
    name: 'CreerEquipement',
    component: CreerEquipement,
    meta: { title: 'Ajouter Equipement' }
  },

  // Defaillance ---------------------------------------------------------------
  {
    path: '/creerDefaillance/:equipementReference?',
    name: 'CreerDefaillance',
    component: CreerDefaillance,
    props: true,
    meta: { title: 'Signaler une défaillance' }
  },

  {
    path: '/defaillance/:id',
    name: 'AfficherDefaillance',
    component: AfficherDefaillance,
    props: true,
    meta: { title: 'Détails de la defaillance' }
  },

  {
    path: '/defaillance/:id/ajouterDocument',
    name: 'AjouterDocumentDefaillance',
    component: AjouterDocumentDefaillance,
    props: true,
    meta: { title: 'Ajouter un document à la défaillance' }
  },

  // Lieux ---------------------------------------------------------------

  {
    path: '/lieux',
    name: 'Lieux',
    component: Lieux,
    meta: { title: 'Lieux' }
  },
  
  {
    path: '/creerLieu',
    name: 'CreerLieu',
    component: CreerLieu,
    meta: { title: 'Creer un lieu' }
  },

  {
    path: '/afficherLieu/:id',
    name: 'AfficherLieu',
    component: AfficherLieu,
    props: true,
    meta: { title: 'Détails d\'un lieu' }
  },



  

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router