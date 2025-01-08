<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <v-col cols="3">
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
          <v-col cols="9">
            <v-data-table
              :headers="headers"
              :items="filteredEquipements"
              :items-per-page="itemsPerPage"
              :page.sync="page"
              item-value="name"
              class="elevation-1 rounded-lg"
              @page-count="pageCount = $event"
            >
            <template v-slot:item="{ item }">
              <tr>
                <td>{{ item.designation }}</td>
                <td>{{ item.lieu ? item.lieu.nomLieu : 'N/A' }}</td>
                <td>{{ item.statutEquipement }}</td>
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
import NavigationDrawer from '@/components/BarreNavigation.vue';
import TopNavBar from "@/components/TopNavBar.vue";
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
    const state = reactive({
      equipements: [],
      lieux: [],
      modeleEquipements: [],
      selectedLieu: null,
      page: 1,
      pageCount: 0,
      itemsPerPage: 5,
      typesEquipements: [],
      headers: [
        { text: 'Désignation', value: 'designation' },
        { text: 'Lieu', value: 'lieu.nomLieu' },
        { text: 'Statut', value: 'statutEquipement' },
      ],

    });

    const fetchData = async () => {
      try {
        const [equipementsRes, lieuxRes, modeleEquipementsRes] = await Promise.all([
          api.getEquipements(),
          api.getLieux(),
          api.getModeleEquipements()
        ]);
        
        state.equipements = equipementsRes.data;
        state.lieux = lieuxRes.data;
        state.modeleEquipements = modeleEquipementsRes.data;
        
        console.log('Modèles d\'équipements:', state.modeleEquipements);
        console.log('Données récupérées avec succès');
      } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
      }
    };

    const filteredEquipements = computed(() => {
      if (!state.selectedLieu) {
        return state.equipements;
      }
      return state.equipements.filter(e => e.lieu === state.selectedLieu);
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
    };
  }
};
</script>