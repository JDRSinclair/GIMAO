<template>
  <v-container>
    <v-row>
<<<<<<< Updated upstream
      <v-col cols="4">
        <!-- Structure des lieux -->
=======
      <!-- Colonne de gauche -->
      <v-col cols="4">
        <!-- Carte : Structure des lieux -->
>>>>>>> Stashed changes
        <v-card elevation="1" class="rounded-lg pa-2 mb-4">
          <v-card-title class="font-weight-bold text-uppercase text-primary">
            Structure des lieux
          </v-card-title>
          <v-divider></v-divider>
<<<<<<< Updated upstream
          <LieuxExplorer :lieux="lieuxAvecTous" @select-lieu="handleLieuSelected" />
        </v-card>

        <!-- Types d'équipements -->
        <v-card elevation="1" class="rounded-lg pa-2">
          <v-card-title class="font-weight-bold text-uppercase text-primary">Types d'équipements</v-card-title>
          <v-divider></v-divider>
          <v-list dense>
            <v-list-item link @click="handleTypeEquipementSelected(null)">
              <v-list-item-title>Tous</v-list-item-title>
            </v-list-item>
            <v-list-item v-for="(modele, index) in modeleEquipements" :key="index" link @click="handleTypeEquipementSelected(modele)">
=======
          <div>
            <!-- Message si aucune donnée n'est disponible -->
            <p v-if="!lieuxAvecTous || lieuxAvecTous.length === 0">Aucune donnée disponible.</p>
            <!-- Arborescence des lieux -->
            <v-treeview
              v-else
              v-model:selected="selectedTreeNodes"
              :items="lieux"
              item-title="nomLieu"
              item-value="id"
              select-strategy="selectionType"
              selectable
              dense
              @update:selected="onSelectLieu"
            >
              <!-- Slot pour l'icône de préfixe (flèche pour ouvrir/fermer les nœuds) -->
              <template v-slot:prepend="{ item, open }">
                <v-icon
                  v-if="item.children && item.children.length > 0 && item.nomLieu !== 'Tous'"
                  @click.stop="toggleNode(item)"
                  :class="{ 'rotate-icon': open }"
                >
                  {{ open ? 'mdi-triangle-down' : 'mdi-triangle-right' }}
                </v-icon>
                <!-- Espace réservé pour les éléments sans enfants -->
                <span v-else class="tree-icon-placeholder"></span>
              </template>
              <!-- Slot pour le label personnalisé (affichage du type de lieu) -->
              <template v-slot:label="{ item }">
                <span class="text-caption ml-2">{{ item.typeLieu }}</span>
              </template>
            </v-treeview>
          </div>
        </v-card>
        
        <!-- Carte : Types d'équipements -->
        <v-card elevation="1" class="rounded-lg pa-2">
          <v-card-title class="font-weight-bold text-uppercase text-primary">
            Types d'équipements
          </v-card-title>
          <v-divider></v-divider>
          <!-- Liste des types d'équipements -->
          <v-list dense>
            <!-- Option "Tous" pour sélectionner tous les types d'équipements -->
            <v-list-item
              link
              @click="handleTypeEquipementSelected(null)"
              :class="{ 'selected-item': selectedTypeEquipements.length === 0 }"
            >
              <v-list-item-title>Tous</v-list-item-title>
            </v-list-item>
            <!-- Boucle pour afficher chaque type d'équipement -->
            <v-list-item
              v-for="(modele, index) in modeleEquipements"
              :key="index"
              link
              @click="handleTypeEquipementSelected(modele)"
              :class="{ 'selected-item': isTypeEquipementSelected(modele) }"
            >
>>>>>>> Stashed changes
              <v-list-item-title>{{ modele.nomModeleEquipement }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
<<<<<<< Updated upstream

      <v-col cols="8">
        <!-- Bouton d'ajout d'équipement -->
=======
      
      <!-- Colonne de droite -->
      <v-col cols="8">
        <!-- Bouton pour rediriger vers la page d'ajout d'équipement -->
>>>>>>> Stashed changes
        <v-btn color="primary" @click="ouvrirPageAjoutEquipement" class="mb-4">
          Aller à l'ajout d'équipement
        </v-btn>

<<<<<<< Updated upstream
        <!-- Table des équipements -->
=======
        <!-- Tableau des équipements -->
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        </v-data-table>

        <v-pagination v-model="page" :length="pageCount" class="text-center pt-2"></v-pagination>
=======
        
          <!-- Template personnalisé pour chaque ligne du tableau -->
          <template v-slot:item="{ item }">
            <!-- Ligne cliquable pour afficher les détails de l'équipement -->
            <tr @click="ouvrirAfficherEquipement(item.reference)" style="cursor: pointer;">
              <td>{{ item.modeleEquipement.nomModeleEquipement }}</td>
              <td>{{ item.lieu.nomLieu }}</td>
              <td>
                <v-chip
                  :color="getStatusColor(item.statut.statutEquipement)"
                  text-color="white"
                  small
                >
                  {{ item.statut.statutEquipement }}
                </v-chip>
              </td>
            </tr>
          </template>
        </v-data-table>

>>>>>>> Stashed changes
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ref, computed, onMounted, reactive, toRefs } from 'vue';
import { useRouter } from 'vue-router';
<<<<<<< Updated upstream
import LieuxExplorer from '@/components/LieuxExplorer.vue';
=======
import { VTreeview } from 'vuetify/labs/VTreeview';
>>>>>>> Stashed changes
import api from '@/services/api';

export default {
  name: 'Equipements',
  components: {
<<<<<<< Updated upstream
    LieuxExplorer,
  },
  setup() {
    const router = useRouter();
=======
    VTreeview,
  },
  setup() {
    const router = useRouter();

    // État réactif pour gérer les données et l'état du composant
>>>>>>> Stashed changes
    const state = reactive({
      equipements: [],
      lieux: [],
      modeleEquipements: [],
<<<<<<< Updated upstream
      selectedLieu: null,
      selectedTypeEquipement: null,
      page: 1,
      pageCount: 0,
      itemsPerPage: 5,
=======
      selectedLieu: [],
      selectedTypeEquipements: [],
      selectedTreeNodes: [],
      page: 1,
      pageCount: 0,
      itemsPerPage: 10,
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
=======
      openNodes: new Set(),
>>>>>>> Stashed changes
    });

    // Fonction pour récupérer les données depuis l'API
    const fetchData = async () => {
      try {
        const [equipementsRes, lieuxRes, modeleEquipementsRes] = await Promise.all([
          api.getEquipementsVue(),
<<<<<<< Updated upstream
          api.getLieux(),
=======
          api.getLieuxHierarchy(),
>>>>>>> Stashed changes
          api.getModeleEquipements()
        ]);

        state.equipements = equipementsRes.data;
        state.lieux = lieuxRes.data;
        state.modeleEquipements = modeleEquipementsRes.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
      }
    };

<<<<<<< Updated upstream
    const lieuxAvecTous = computed(() => {
      return [{ id: null, nomLieu: 'Tous', children: [] }, ...state.lieux];
    });

    const filteredEquipements = computed(() => {
      return state.equipements.filter(e => {
        const lieuMatch = !state.selectedLieu || state.selectedLieu === 'Tous' || e.lieu.nomLieu === state.selectedLieu;
        const typeMatch = !state.selectedTypeEquipement || e.modeleEquipement.nomModeleEquipement === state.selectedTypeEquipement;
        return lieuMatch && typeMatch;
      });
    });

    const handleLieuSelected = (lieu) => {
      state.selectedLieu = lieu.nomLieu;
    };

    const handleTypeEquipementSelected = (modele) => {
      state.selectedTypeEquipement = modele ? modele.nomModeleEquipement : null;
    };

    const ouvrirPageAjoutEquipement = () => {
      router.push('/ajouter-equipement');
    };

    onMounted(fetchData);
=======
    const getStatusColor = (statut) => {
      switch (statut) {
        case 'En fonctionnement':
          return 'green';
        case 'Dégradé':
          return 'orange';
        case 'À l\'arrêt':
          return 'red';
        default:
          return 'black';
      }
    };

    // Calcul des lieux avec l'option "Tous"
    const lieuxAvecTous = computed(() => {
      return [{ id: null, nomLieu: 'Tous' }, ...state.lieux];
    });
>>>>>>> Stashed changes

    // Gestion de la sélection d'un lieu dans l'arborescence
    const onSelectLieu = (items) => {
      if (items.length > 0) {
        state.selectedLieu = items.map(id => {
          const selectedItem = findItem(lieuxAvecTous.value, id);
          return selectedItem?.nomLieu;
        }).filter(Boolean);
      } else {
        state.selectedLieu = [];
      }
    };

    // Fonction pour trouver un élément dans l'arborescence
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

    // Fonction pour basculer l'état d'un nœud dans l'arborescence
    const toggleNode = (item) => {
      if (state.openNodes.has(item.id)) {
        state.openNodes.delete(item.id);
      } else {
        state.openNodes.add(item.id);
      }
    };

    // Gestion de la sélection d'un type d'équipement
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

    // Vérifie si un type d'équipement est sélectionné
    const isTypeEquipementSelected = (modele) => {
      return state.selectedTypeEquipements.some(m => m.nomModeleEquipement === modele.nomModeleEquipement);
    };

    // Filtrage des équipements en fonction des sélections
    const filteredEquipements = computed(() => {
      return state.equipements.filter(e => {
        const lieuMatch = state.selectedLieu.length === 0 || 
                         state.selectedLieu.includes('Tous') || 
                         state.selectedLieu.includes(e.lieu.nomLieu);
        const typeMatch = state.selectedTypeEquipements.length === 0 ||
                         state.selectedTypeEquipements.some(m => 
                           m.nomModeleEquipement === e.modeleEquipement.nomModeleEquipement
                         );
        return lieuMatch && typeMatch;
      });
    });

    // Redirection vers la page d'ajout d'équipement
    const ouvrirPageAjoutEquipement = () => {
      router.push('/creer-equipement');
    };

    // Redirection vers la page d'affichage d'un équipement
    const ouvrirAfficherEquipement = (reference) => {
      router.push({ name: 'AfficherEquipement', params: { reference: reference } });
    };

    // Chargement des données au montage du composant
    onMounted(fetchData);

    return {
      ...toRefs(state),
      lieuxAvecTous,
      filteredEquipements,
<<<<<<< Updated upstream
      handleLieuSelected,
      handleTypeEquipementSelected,
      ouvrirPageAjoutEquipement,
=======
      onSelectLieu,
      handleTypeEquipementSelected,
      ouvrirPageAjoutEquipement,
      ouvrirAfficherEquipement,
      isTypeEquipementSelected,
      toggleNode,
      getStatusColor,
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
=======
}

.v-treeview-node--active {
  background-color: #7577e9 !important;
  color: white !important;
}

.v-treeview-node--active:hover {
  background-color: #5658c7 !important;
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
>>>>>>> Stashed changes
}
</style>