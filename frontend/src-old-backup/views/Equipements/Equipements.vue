<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <!-- Colonne de gauche : Structure des lieux et Types d'équipements -->
          <v-col cols="4">
            <!-- Carte pour explorer la structure des lieux -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Structure des lieux</v-card-title>
              <v-divider></v-divider>
              <!-- Composant LieuxExplorer pour afficher la hiérarchie des lieux -->
              <LieuxExplorer :lieux="lieux" @select-lieu="handleLieuSelected" />
            </v-card>

            <!-- Carte pour afficher les types d'équipements -->
            <v-card elevation="1" class="rounded-lg pa-2">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Types d'équipements</v-card-title>
              <v-divider></v-divider>
              <!-- Liste des modèles d'équipements -->
              <v-list dense>
                <v-list-item v-for="(modele, index) in modeleEquipements" :key="index" link>
                  <v-list-item-title>{{ modele.nomModeleEquipement }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>

          <!-- Colonne de droite : Tableau des équipements -->
          <v-col cols="8">
            <!-- Bouton pour naviguer vers la page d'ajout d'équipement -->
            <v-btn color="primary" @click="ouvrirPageAjoutEquipement" class="mb-4">
              Aller à l'ajout d'équipement
            </v-btn>

            <!-- Tableau des équipements avec pagination -->
            <v-data-table
              :headers="headers"
              :items="filteredEquipements"
              :items-per-page="itemsPerPage"
              :page.sync="page"
              class="elevation-1 rounded-lg"
              @page-count="pageCount = $event"
            >
              <!-- Template personnalisé pour chaque ligne du tableau -->
              <template v-slot:item="{ item }">
                <tr @click="ouvrirPageVoirEquipement(item.reference)" style="cursor: pointer;">
                  <td>{{ item.designation }}</td>
                  <td>{{ item.nomLieu || 'N/A' }}</td>
                  <td>{{ item.statutEquipement || 'N/A' }}</td>
                </tr>
              </template>
            </v-data-table>

            <!-- Pagination -->
            <div class="text-center pt-2">
              <v-pagination v-model="page" :length="pageCount"></v-pagination>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { ref, computed, onMounted, reactive, toRefs } from 'vue';
import { useRouter } from 'vue-router';
import LieuxExplorer from '@/components/LieuxExplorer.vue';
import api from '@/services/api';

export default {
  name: 'Equipements',
  components: { LieuxExplorer },
  setup() {
    const router = useRouter();

    // État réactif pour stocker les données et les états de l'application
    const state = reactive({
      equipements: [], // Liste des équipements
      lieux: [], // Liste des lieux
      modeleEquipements: [], // Liste des modèles d'équipements
      informationStatus: [], // Liste des statuts des équipements
      selectedLieu: null, // Lieu sélectionné
      page: 1, // Page actuelle de la pagination
      pageCount: 0, // Nombre total de pages
      itemsPerPage: 5, // Nombre d'éléments par page
      headers: [ // En-têtes du tableau des équipements
        { text: 'Désignation', value: 'designation' },
        { text: 'Lieu', value: 'nomLieu' },
        { text: 'Statut', value: 'statutEquipement' },
      ],
    });

    // Fonction pour récupérer les données depuis l'API
    const fetchData = async () => {
      try {
        // Récupération simultanée des données des équipements, lieux, modèles et statuts
        const [equipementsRes, lieuxRes, modeleEquipementsRes, informationStatusRes] = await Promise.all([
          api.getEquipements(),
          api.getLieux(),
          api.getModeleEquipements(),
          api.getInformationStatus(),
        ]);

        // Mise à jour de l'état avec les données récupérées
        state.equipements = equipementsRes.data;
        state.lieux = lieuxRes.data;
        state.modeleEquipements = modeleEquipementsRes.data;
        state.informationStatus = informationStatusRes.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
      }
    };

    // Fonction récursive pour trouver un lieu par son ID dans la hiérarchie des lieux
    const findLieuById = (lieux, id) => {
      for (const lieu of lieux) {
        if (lieu.id === id) return lieu; // Retourne le lieu si l'ID correspond
        if (lieu.children) {
          const found = findLieuById(lieu.children, id); // Recherche récursive dans les enfants
          if (found) return found;
        }
      }
      return null; // Retourne null si le lieu n'est pas trouvé
    };

    // Propriété calculée pour mapper les équipements avec leur lieu et statut
    const filteredEquipements = computed(() => {
      return state.equipements.map(equipement => {
        const lieu = findLieuById(state.lieux, equipement.lieu); // Trouve le lieu associé
        const statut = state.informationStatus.find(status => status.equipement === equipement.reference); // Trouve le statut associé
        return {
          ...equipement,
          nomLieu: lieu ? lieu.nomLieu : 'N/A', // Ajoute le nom du lieu ou 'N/A' si non trouvé
          statutEquipement: statut ? statut.statutEquipement : 'N/A', // Ajoute le statut ou 'N/A' si non trouvé
        };
      });
    });

    // Gestion de la sélection d'un lieu
    const handleLieuSelected = (lieu) => {
      state.selectedLieu = lieu.nomLieu;
    };

    // Navigation vers la page d'ajout d'équipement
    const ouvrirPageAjoutEquipement = () => {
      router.push({ name: 'AjouterEquipement' });
    };

    // Navigation vers la page de visualisation d'un équipement
    const ouvrirPageVoirEquipement = (reference) => {
      if (!reference) return console.error('Reference is missing');
      router.push({ name: 'VisualiserEquipement', params: { reference } });
    };

    // Récupération des données au montage du composant
    onMounted(fetchData);

    // Retour des propriétés et méthodes exposées au template
    return {
      ...toRefs(state),
      filteredEquipements,
      handleLieuSelected,
      ouvrirPageAjoutEquipement,
      ouvrirPageVoirEquipement,
    };
  },
};
</script>

<style scoped>
/* Style pour le survol des lignes du tableau */
.v-data-table tr:hover {
  background-color: #e6f2ff;
  transition: background-color 0.3s ease;
}

.v-data-table tr:hover td {
  color: #0056b3;
}
</style>