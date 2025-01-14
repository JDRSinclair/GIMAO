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
  {
    path: '/signalements',
    name: 'Signalements',
    component: Signalements,
    meta: { title: 'Signalements' }
  },




// ---------------------------------------------------------------

  {
    path: '/intervention/:id',
    name: 'AfficherIntervention',
    component: AfficherIntervention,
    props: true, 
    meta: { title: 'Détailes de l\'intervention' }
  },

  {
    path: '/equipement/:reference',
    name: 'AfficherEquipement',
    component: AfficherEquipement,
    props: true, 
    meta: { title: 'Afficher Equipement' }
  },

  {
    path: '/creerIntervention',
    name: 'CreerIntervention',
    component: CreerIntervention,
    meta: { title: 'Créer un bon de travail' }
  },

  {
    path: '/creerEquipement',
    name: 'CreerEquipement',
    component: CreerEquipement,
    meta: { title: 'Ajouter Equipement' }
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router