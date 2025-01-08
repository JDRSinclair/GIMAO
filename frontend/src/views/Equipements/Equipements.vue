<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <v-col cols="4">
            <!-- Affichage de lieux  -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Structure des lieux</v-card-title>
              <v-divider></v-divider>
              <LieuxExplorer :lieux="lieux" @select-lieu="handleLieuSelected" />
            </v-card>

            <!-- Affichage de Types d'équipements -->
            <v-card elevation="1" class="rounded-lg pa-2">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Types d'équipements</v-card-title>
              <v-divider></v-divider>
              <v-list dense>
                <v-list-item v-for="(modele, index) in modeleEquipements" :key="index" link>
                  <v-list-item-title>{{ modele.nomModeleEquipement }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>

          <!-- Affichage des équipements choisis -->
          <v-col cols="8">
            <v-btn
              color="primary"
              @click="ouvrirPageAjoutEquipement"
              class="mb-4"
            >
              Aller à l'ajout d'équipement
            </v-btn>
            <v-data-table
              :headers="headers"
              :items="filteredEquipements"
              :items-per-page="itemsPerPage"
              :page.sync="page"
              class="elevation-1 rounded-lg"
              @page-count="pageCount = $event"
            >
              <template v-slot:item="{ item }">
                <tr @click="ouvrirPageVoirEquipement(item.reference)" style="cursor: pointer;">
                  <td>{{ item.designation }}</td>
                  <td>{{ item.nomLieu || 'N/A' }}</td>
                  <td>{{ item.statutEquipement || 'N/A' }}</td>
                </tr>
              </template>
            </v-data-table>
            <div class="text-center pt-2">
              <v-pagination
                v-model="page"
                :length="pageCount">
              </v-pagination>
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
import NavigationDrawer from '@/components/BarreNavigation.vue';
import TopNavBar from "@/components/BarreNavigationHaut.vue";
import LieuxExplorer from '@/components/LieuxExplorer.vue';
import '@/assets/css/global.css';
import api from '@/services/api';

export default {
  name: 'Equipements',
  components: {
    NavigationDrawer,
    TopNavBar,
    LieuxExplorer,
  },
  setup() {
    const router = useRouter();
    const state = reactive({
      equipements: [],
      lieux: [],
      modeleEquipements: [],
      informationStatus: [], // Add informationStatus
      selectedLieu: null,
      page: 1,
      pageCount: 0,
      itemsPerPage: 5,
      headers: [
        { text: 'Désignation', value: 'designation' },
        { text: 'Lieu', value: 'nomLieu' },
        { text: 'Statut', value: 'statutEquipement' },
      ],
    });

    const fetchData = async () => {
      try {
        const [equipementsRes, lieuxRes, modeleEquipementsRes, informationStatusRes] = await Promise.all([
          api.getEquipements(),
          api.getLieux(),
          api.getModeleEquipements(),
          api.getInformationStatus() // Fetch informationStatus data
        ]);
        
        state.equipements = equipementsRes.data;
        state.lieux = lieuxRes.data;
        state.modeleEquipements = modeleEquipementsRes.data;
        state.informationStatus = informationStatusRes.data; // Store informationStatus data
        
        console.log('Equipements:', state.equipements);
        console.log('Lieux:', state.lieux);
        console.log('Information Status:', state.informationStatus);
      } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
      }
    };


    const ouvrirPageAjoutEquipement = () => {
      router.push({ name: 'AjouterEquipement' });
    };

    const ouvrirPageVoirEquipement = (reference) => {
      if (!reference) {
        console.error('Reference is missing');
        return;
      }
      router.push({ name: 'VisualiserEquipement', params: { reference } });
    };

    const findLieuById = (lieux, id) => {
      for (const lieu of lieux) {
        if (lieu.id === id) {
          return lieu; // Return the matching lieu object
        }
        if (lieu.children && lieu.children.length > 0) {
          const found = findLieuById(lieu.children, id); // Recursively search children
          if (found) {
            return found; // Return the matching lieu object from children
          }
        }
      }
      return null; // Return null if no match is found
    };
    
    const filteredEquipements = computed(() => {
      return state.equipements.map(equipement => {
        const lieu = findLieuById(state.lieux, equipement.lieu); // Find lieu in the hierarchy
        console.log('Mapping lieu:', { equipementLieu: equipement.lieu, foundLieu: lieu }); // Debug mapping
        return {
          ...equipement,
          nomLieu: lieu ? lieu.nomLieu : 'N/A', // Add nomLieu
        };
      });
    });

    const handleLieuSelected = (lieu) => {
      state.selectedLieu = lieu.nomLieu;
    };

    onMounted(() => {
      fetchData();
    });

    return {
      ...toRefs(state),
      filteredEquipements,
      handleLieuSelected,
      ouvrirPageAjoutEquipement,
      ouvrirPageVoirEquipement,
    };
  }
};
</script>

<style scoped>
/* Effet de survol personnalisé */
.v-data-table tr:hover {
  background-color: #e6f2ff; /* Fond bleu clair au survol */
  transition: background-color 0.3s ease; /* Transition fluide */
}

.v-data-table tr:hover td {
  color: #0056b3; /* Couleur du texte en bleu foncé au survol */
}
</style>