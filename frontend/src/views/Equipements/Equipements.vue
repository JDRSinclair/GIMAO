<template>
  <v-container>
    <v-row>
      <v-col cols="4">
        <!-- Structure des lieux -->
        <v-card elevation="1" class="rounded-lg pa-2 mb-4">
          <v-card-title class="font-weight-bold text-uppercase text-primary">
            Structure des lieux
          </v-card-title>
          <v-divider></v-divider>
          <LieuxExplorer :lieux="lieuxAvecTous" @select-lieu="handleLieuSelected" />
        </v-card>

        <!-- Types d'équipements -->
        <v-card elevation="1" class="rounded-lg pa-2">
          <v-card-title class="font-weight-bold text-uppercase text-primary">Types d'équipements</v-card-title>
          <v-divider></v-divider>
          <v-list dense>
            <v-list-item 
              link 
              @click="handleTypeEquipementSelected(null)"
              :class="{ 'selected-item': selectedTypeEquipements.length === 0 }"
            >
              <v-list-item-title>Tous</v-list-item-title>
            </v-list-item>
            <v-list-item 
              v-for="(modele, index) in modeleEquipements" 
              :key="index" 
              link 
              @click="handleTypeEquipementSelected(modele)"
              :class="{ 'selected-item': isTypeEquipementSelected(modele) }"
            >
              <v-list-item-title>{{ modele.nomModeleEquipement }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-card>

      </v-col>

      <v-col cols="8">
        <!-- Bouton d'ajout d'équipement -->
        <v-btn color="primary" @click="ouvrirPageAjoutEquipement" class="mb-4">
          Aller à l'ajout d'équipement
        </v-btn>

        <!-- Table des équipements -->
        <v-data-table
          :headers="header"
          :items="filteredEquipements"
          :items-per-page="itemsPerPage"
          :page.sync="page"
          class="elevation-1 rounded-lg"
          @page-count="pageCount = $event"
          :sort-by="['designation']"
          :sort-desc="[false]"
        >
        </v-data-table>

        <v-pagination v-model="page" :length="pageCount" class="text-center pt-2"></v-pagination>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ref, computed, onMounted, reactive, toRefs } from 'vue';
import { useRouter } from 'vue-router';
import LieuxExplorer from '@/components/LieuxExplorer.vue';
import api from '@/services/api';

export default {
  name: 'Equipements',
  components: {
    LieuxExplorer,
  },
  setup() {
    const router = useRouter();

    const state = reactive({
      equipements: [],
      lieux: [],
      modeleEquipements: [],
      selectedLieu: null,
      selectedTypeEquipements: [],
      page: 1,
      pageCount: 0,
      itemsPerPage: 5,
      header: [
        { title: 'Désignation', value: 'modeleEquipement.nomModeleEquipement', sortable: true, align: 'center' },
        { title: 'Lieu', value: 'lieu.nomLieu', sortable: true, align: 'center' },
        { title: 'Statut', value: 'statut.statutEquipement', sortable: true, align: 'center',
          sort: (a, b) => {
            const order = ['Rebuté', 'En fonctionnement', 'Dégradé', 'A l\'arrêt'];
            return order.indexOf(a) - order.indexOf(b);
          }
        },
      ],
    });

    const fetchData = async () => {
      try {
        const [equipementsRes, lieuxRes, modeleEquipementsRes] = await Promise.all([
          api.getEquipementsVue(),
          api.getLieux(),
          api.getModeleEquipements()
        ]);

        state.equipements = equipementsRes.data;
        state.lieux = lieuxRes.data;
        state.modeleEquipements = modeleEquipementsRes.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
      }
    };

    const lieuxAvecTous = computed(() => {
      return [{ id: null, nomLieu: 'Tous' }, ...state.lieux];
    });

    const handleLieuSelected = (lieu) => {
      state.selectedLieu = lieu.nomLieu;
    };

    const handleTypeEquipementSelected = (modele) => {
      if (modele === null) {
        state.selectedTypeEquipements = [];
      } else {
        const index = state.selectedTypeEquipements.findIndex(m => m.nomModeleEquipement === modele.nomModeleEquipement);
        if (index > -1) {
          state.selectedTypeEquipements.splice(index, 1);
        } else {
          state.selectedTypeEquipements.push(modele);
        }
      }
    };

    const isTypeEquipementSelected = (modele) => {
      return state.selectedTypeEquipements.some(m => m.nomModeleEquipement === modele.nomModeleEquipement);
    };

    const filteredEquipements = computed(() => {
      return state.equipements.filter(e => {
        const lieuMatch = !state.selectedLieu || state.selectedLieu === 'Tous' || e.lieu.nomLieu === state.selectedLieu;
        const typeMatch = state.selectedTypeEquipements.length === 0 || 
                          state.selectedTypeEquipements.some(m => m.nomModeleEquipement === e.modeleEquipement.nomModeleEquipement);
        return lieuMatch && typeMatch;
      });
    });

    const ouvrirPageAjoutEquipement = () => {
      router.push('/ajouter-equipement');
    };

    onMounted(fetchData);

    return {
      ...toRefs(state),
      lieuxAvecTous,
      filteredEquipements,
      handleLieuSelected,
      handleTypeEquipementSelected,
      ouvrirPageAjoutEquipement,
      isTypeEquipementSelected,
    };
  }
};
</script>

<style scoped>
.v-data-table tr:hover {
  background-color: #e6f2ff;
  transition: background-color 0.3s ease;
}

.v-data-table tr:hover td {
  color: #0056b3;
}

.v-data-table th {
  color: black !important;
}

.selected-item {
  background-color: #7577e9 !important;
  color: white !important;
}

.selected-item:hover {
  background-color: #5658c7 !important;
}
</style>