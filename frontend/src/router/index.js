import { createRouter, createWebHistory } from 'vue-router';
import TableauDeBord from '@/views/TableauDeBord/TableauDeBord.vue';
import Equipements from '@/views/Equipements/Equipements.vue';
import Maintenances from '@/views/Maintenances/Maintenances.vue';
import Techniciens from '@/views/Techniciens/Techniciens.vue';
import GestionComptes from '@/views/GestionComptes/GestionComptes.vue';
import GestionDonnees from '@/views/GestionDonnees/GestionDonnees.vue';
import Commandes from '@/views/Commandes/Commandes.vue';
import Stocks from '@/views/Stocks/Stocks.vue';
import Signalements from '@/views/Signalements/Signalements.vue';
import Fournisseurs from '@/views/GestionDonnees/Fournisseurs.vue';
import CreerFournisseurs from '@/views/GestionDonnees/CreerFournisseurs.vue';
import Fabricants from '@/views/GestionDonnees/Fabricants.vue';
import Consommables from '@/views/GestionDonnees/Consommables.vue';
import ModelesEquipements from '@/views/GestionDonnees/ModelesEquipements.vue';
import CreerFabricants from '@/views/GestionDonnees/CreerFabricants.vue';
import CreerConsommables from '@/views/GestionDonnees/CreerConsommables.vue';
import CreerModelesEquipements from '@/views/GestionDonnees/CreerModelesEquipements.vue';
import CreerIntervention from '@/views/Interventions/CreerIntervention.vue';
import AfficherIntervention from '@/views/Interventions/AfficherIntervention.vue';
import AfficherEquipement from '@/views/Equipements/AfficherEquipement.vue';
import CreerEquipement from '@/views/Equipements/CreerEquipement.vue';


// ------------------------------------------------------------------
import CreerLieu from '@/views/Lieux/CreerLieu.vue'
import Lieux from '@/views/Lieux/Lieux.vue'


const routes = [
  // Tableau de Bord
  {
    path: '/',
    name: 'TableauDeBord',
    component: TableauDeBord,
    meta: { title: 'Tableau de Bord' }
  },
  
  // Equipements
  {
    path: '/equipements',
    name: 'Equipements',
    component: Equipements,
    meta: { title: 'Equipement' }
  },
  {
    path: '/creer-equipement',
    name: 'CreerEquipement',
    component: CreerEquipement,
    meta: { title: 'Ajouter Equipement' }
  },
  {
    path: '/equipement/:reference',
    name: 'AfficherEquipement',
    component: AfficherEquipement,
    props: true,
    meta: { title: 'Afficher Equipement' }
  },
  
  // Maintenances
  {
    path: '/maintenances',
    name: 'Maintenances',
    component: Maintenances,
    meta: { title: 'Maintenances' }
  },
  
  // Techniciens
  {
    path: '/techniciens',
    name: 'Techniciens',
    component: Techniciens,
    meta: { title: 'Techniciens' }
  },
  
  // Gestion des Comptes
  {
    path: '/gestion-comptes',
    name: 'GestionComptes',
    component: GestionComptes,
    meta: { title: 'Gestion des Comptes' }
  },
  
  // Gestion des Données
  {
    path: '/gestion-donnees',
    name: 'GestionDonnees',
    component: GestionDonnees,
    meta: { title: 'Gestion des Données' }
  },
  {
    path: '/fournisseurs',
    name: 'Fournisseurs',
    component: Fournisseurs,
    meta: { title: 'Fournisseurs' }
  },
  {
    path: '/creer-fournisseurs',
    name: 'CreerFournisseurs',
    component: CreerFournisseurs,
    meta: { title: 'Créer Fournisseurs' }
  },
  {
    path: '/fabricants',
    name: 'Fabricants',
    component: Fabricants,
    meta: { title: 'Fabricants' }
  },
  {
    path: '/creer-fabricants',
    name: 'CreerFabricants',
    component: CreerFabricants,
    meta: { title: 'Créer Fabricants' }
  },
  {
    path: '/consommables',
    name: 'Consommables',
    component: Consommables,
    meta: { title: 'Consommables' }
  },
  {
    path: '/creer-consommables',
    name: 'CreerConsommables',
    component: CreerConsommables,
    meta: { title: 'Créer Consommables' }
  },
  {
    path: '/modeles-equipements',
    name: 'ModelesEquipements',
    component: ModelesEquipements,
    meta: { title: 'Modèles Équipements' }
  },
  {
    path: '/creer-modeles-equipements',
    name: 'CreerModelesEquipements',
    component: CreerModelesEquipements,
    meta: { title: 'Créer Modèles Équipements' }
  },
  
  // Interventions
  {
    path: '/creer-intervention',
    name: 'CreerIntervention',
    component: CreerIntervention,
    meta: { title: 'Créer Intervention' }
  },
  {
    path: '/intervention/:id',
    name: 'AfficherIntervention',
    component: AfficherIntervention,
    props: true,
    meta: { title: 'Détails de l\'intervention' }
  },
  
  // Commandes
  {
    path: '/commandes',
    name: 'Commandes',
    component: Commandes,
    meta: { title: 'Commandes' }
  },
  
  // Stocks
  {
    path: '/stocks',
    name: 'Stocks',
    component: Stocks,
    meta: { title: 'Stocks' }
  },
  
  // Signalements
  {
    path: '/signalements',
    name: 'Signalements',
    component: Signalements,
    meta: { title: 'Liste des signalements' }
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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;