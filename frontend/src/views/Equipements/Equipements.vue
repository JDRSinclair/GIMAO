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
          <div>
            <p v-if="!lieuxAvecTous || lieuxAvecTous.length === 0">Aucune donnée disponible.</p>
            <v-treeview
              v-else
              :items="lieuxAvecTous"
              item-key="id"
              :open-on-click="false"
              item-text="nomLieu"
              rounded
              hoverable
              activatable
              dense
              @update:active="onSelectLieu"
            >
              <template v-slot:prepend="{ item, open }">
                <v-icon
                  v-if="item.children && item.children.length > 0 && item.nomLieu !== 'Tous'"
                  @click.stop="toggleNode(item)"
                  :class="{ 'rotate-icon': open }"
                >
                  {{ open ? 'mdi-triangle-down' : 'mdi-triangle-right' }}
                </v-icon>
                <span v-else class="tree-icon-placeholder"></span>
                {{ item.nomLieu }}
              </template>
              <template v-slot:label="{ item }">
                <span class="text-caption ml-2">{{ item.typeLieu }}</span>
              </template>
            </v-treeview>
          </div>
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
          <template v-slot:item="{ item }">
            <tr @click="ouvrirAfficherEquipement(item.reference)" style="cursor: pointer;">
              <td>{{ item.modeleEquipement.nomModeleEquipement }}</td>
              <td>{{ item.lieu.nomLieu }}</td>
              <td>{{ item.statut.statutEquipement }}</td>
            </tr>
          </template>
        </v-data-table>

        <v-pagination v-model="page" :length="pageCount" class="text-center pt-2"></v-pagination>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ref, computed, onMounted, reactive, toRefs } from 'vue';
import { useRouter } from 'vue-router';
import { VTreeview } from 'vuetify/labs/VTreeview';
import api from '@/services/api';

export default {
  name: 'Equipements',
  components: {
    VTreeview,
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
      openNodes: new Set(),
    });

    const fetchData = async () => {
      try {
        const [equipementsRes, lieuxRes, modeleEquipementsRes] = await Promise.all([
          api.getEquipementsVue(),
          api.getLieuxHierarchy(),
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

    const onSelectLieu = (items) => {
      if (items.length > 0) {
        const selectedItem = findItem(lieuxAvecTous.value, items[0]);
        if (selectedItem) {
          state.selectedLieu = selectedItem.nomLieu;
        }
      }
    };

    const findItem = (items, id) => {
      for (const item of items) {
        if (item.id === id) {
          return item;
        }
        if (item.children) {
          const found = findItem(item.children, id);
          if (found) {
            return found;
          }
        }
      }
      return null;
    };

    const toggleNode = (item) => {
      if (state.openNodes.has(item.id)) {
        state.openNodes.delete(item.id);
      } else {
        state.openNodes.add(item.id);
      }
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

    const ouvrirAfficherEquipement = (reference) => {
      router.push({ name: 'AfficherEquipement', params: { reference: reference } });
    };

    onMounted(fetchData);

    return {
      ...toRefs(state),
      lieuxAvecTous,
      filteredEquipements,
      onSelectLieu,
      handleTypeEquipementSelected,
      ouvrirPageAjoutEquipement,
      ouvrirAfficherEquipement,
      isTypeEquipementSelected,
      toggleNode,
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

.text-caption {
  color: #666;
  font-size: 0.75rem;
}

.tree-icon-placeholder {
  display: inline-block;
  width: 24px;
  height: 24px;
  margin-right: 4px;
}

.rotate-icon {
  transform: rotate(180deg);
}

.v-icon {
  transition: transform 0.3s ease;
}
</style>