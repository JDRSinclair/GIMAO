import { createRouter, createWebHistory } from 'vue-router'
import TableauDeBord from '@/views/TableauDeBord/TableauDeBord.vue'
import Equipements from '@/views/Equipements/Equipements.vue'
import Maintenances from '@/views/Maintenances/Maintenances.vue'
import Techniciens from '@/views/Techniciens/Techniciens.vue'
import GestionComptes from '@/views/GestionComptes/GestionComptes.vue'
import Commandes from '@/views/Commandes/Commandes.vue'
import Stocks from '@/views/Stocks/Stocks.vue'
import Signalements from '@/views/Signalements/Signalements.vue'


// ---------------------------------------------------------------
import AfficherIntervention from '@/views/Interventions/AfficherIntervention.vue'
import CreerIntervention from '@/views/Interventions/CreerIntervention.vue'

import AfficherEquipement from '@/views/Equipements/AfficherEquipement.vue'
import CreerEquipement from '@/views/Equipements/CreerEquipement.vue'


import CreerSignalement from '@/views/Signalements/CreerSignalement.vue'
import AfficherSignalement from '@/views/Signalements/AfficherSignalement.vue'

// ------------------------------------------------------------------
import CreerLieu from '@/views/Lieux/CreerLieu.vue'
import Lieux from '@/views/Lieux/Lieux.vue'


const routes = [
  {
    path: '/',
    name: 'TableauDeBord',
    component: TableauDeBord,
    meta: { title: 'Tableau de Bord' }
  },
  {
    path: '/equipements',
    name: 'Equipements',
    component: Equipements,
    meta: { title: 'Equipement' }
  },
  {
    path: '/maintenances',
    name: 'Maintenances',
    component: Maintenances,
    meta: { title: 'Maintenances' }
  },
  {
    path: '/signalements',
    name: 'Signalements',
    component: Signalements,
    meta: { title: 'Liste des signalements' }
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





// ---------------------------------------------------------------

// Interventions
  {
    path: '/intervention/:id',
    name: 'AfficherIntervention',
    component: AfficherIntervention,
    props: true, 
    meta: { title: 'Détailes de l\'intervention' }
  },

  {
    path: '/creerIntervention',
    name: 'CreerIntervention',
    component: CreerIntervention,
    meta: { title: 'Créer un bon de travail' }
  },

  // Equipements
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

  // Signalement
  {
    path: '/creerSignalement',
    name: 'CreerSignalement',
    component: CreerSignalement,
    meta: { title: 'Faire un signalement' }
  },

  {
    path: '/AfficherSignalement',
    name: 'AfficherSignalement',
    component: AfficherSignalement,
    meta: { title: 'Détailes du signalement' }
  },

  //Lieux
  {
    path: '/creerLieu',
    name: 'CreerLieu',
    component: CreerLieu,
    meta: { title: 'Creer un lieu' }
  },
  {
    path: '/lieux',
    name: 'Lieux',
    component: Lieux,
    meta: { title: 'Lieux' }
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router