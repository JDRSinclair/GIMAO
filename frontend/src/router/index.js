import { createRouter, createWebHistory } from 'vue-router'
import TableauDeBord from '@/views/TableauDeBord/TableauDeBord.vue'
import Equipements from '@/views/Equipements/Equipements.vue'
import AjouterEquipement from '@/views/Equipements/AjouterEquipement.vue'
import VisualiserEquipement from '@/views/Equipements/VisualiserEquipement.vue'
import Maintenances from '@/views/Maintenances/Maintenances.vue'
import Techniciens from '@/views/Techniciens/Techniciens.vue'
import GestionComptes from '@/views/GestionComptes/GestionComptes.vue'
import Commandes from '@/views/Commandes/Commandes.vue'
import Stocks from '@/views/Stocks/Stocks.vue'
import Signalements from '@/views/Signalements/Signalements.vue'
import CloturerIntervention from '@/views/TableauDeBord/CloturerIntervention.vue'



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

  {
    path: '/cloturer-interventions',
    name: 'CloturerIntervention',
    component: CloturerIntervention,
    meta: { title: 'CloturerIntervention' }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router