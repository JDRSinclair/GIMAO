import { createRouter, createWebHistory } from 'vue-router'
import TableauDeBord from '@/views/TableauDeBord.vue'
import Equipements from '@/views/Equipements.vue'
import Maintenances from '@/views/Maintenances.vue'
import Techniciens from '@/views/Techniciens.vue'
import GestionComptes from '@/views/GestionComptes.vue'
import Commandes from '@/views/Commandes.vue'
import Stocks from '@/views/Stocks.vue'

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
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router