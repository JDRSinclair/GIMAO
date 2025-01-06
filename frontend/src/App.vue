<template>
  <v-app>
    <NavigationDrawer
      :logo="require('@/assets/images/LogoGIMAO.png')"
      :items="menuItems"
      @item-selected="handleItemSelected"
    />
    <TopNavBar />

    <!-- Contenu principal -->
    <v-main>
      <v-container>
        <!-- Filtres et tableau -->
        <v-row>
          <!-- Colonne contenant Liste des salles et Types d'équipements -->
          <v-col cols="3"> <!-- Réduit la largeur à 3/12 -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Liste des salles</v-card-title>
              <v-divider></v-divider>
              <v-list dense>
                <v-list-item @click="toggleSalleSelection('tous')" :class="{'selected': isSalleSelected('tous')}">
                  <v-list-item-title>Tous</v-list-item-title>
                </v-list-item>
                <v-list-item v-for="salle in salles" :key="salle.id" @click="toggleSalleSelection(salle.id)" :class="{'selected': isSalleSelected(salle.id)}">
                  <v-list-item-title>{{ salle.nomLieu }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-card>

            <v-card elevation="1" class="rounded-lg pa-2">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Types d'équipements</v-card-title>
              <v-divider></v-divider>
              <v-list dense>
                <v-list-item @click="toggleTypeEquipementSelection('tous')" :class="{'selected': isTypeEquipementSelected('tous')}">
                  <v-list-item-title>Tous</v-list-item-title>
                </v-list-item>
                <v-list-item v-for="type in typesEquipements" :key="type.id" @click="toggleTypeEquipementSelection(type.id)" :class="{'selected': isTypeEquipementSelected(type.id)}">
                  <v-list-item-title>{{ type.nomModeleEquipement }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>

          <!-- Tableau des équipements -->
          <v-col cols="9"> <!-- Augmente la largeur à 9/12 -->
            <v-data-table
              :headers="headers"
              :items="equipements"
              item-value="name"
              class="elevation-1 rounded-lg"
              hide-default-footer
            ></v-data-table>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import NavigationDrawer from '@/components/BarreNavigation.vue';
import TopNavBar from "@/components/TopNavBar.vue";
import '@/assets/css/global.css'; // Importation du fichier CSS global
import { getAllLieux, getAllTypesEquipements, getAllEquipements, getEquipementsByLieuxAndTypes, getTypesEquipementsByLieu } from '@/services/api';

export default {
  components: {
    NavigationDrawer,
    TopNavBar,
  },

  data() {
    return {
      menuItems: [
        { name: 'Tableau de bord', icon: require('@/assets/images/Graphe.svg') },
        { name: 'Equipements', icon: require('@/assets/images/Outils.svg') },
        { name: 'Maintenances', icon: require('@/assets/images/Maintenance.svg') },
        { name: 'Techniciens', icon: require('@/assets/images/Techniciens.svg') },
      ],
      salles: [],
      typesEquipements: [],
      headers: [
        { text: "Équipement", value: "designation", align: "start" },
        { text: "Salle", value: "lieu.nomLieu" },
        { text: "État", value: "statutEquipement" },
      ],
      equipements: [],
      selectedSalles: new Set(['tous']),
      selectedTypes: new Set(['tous']),
    };
  },

  created() {
    this.fetchSalles();
    this.fetchTypesEquipements();
    this.fetchEquipements();
  },

  methods: {
    async fetchSalles() {
      const response = await getAllLieux();
      this.salles = response.data;
    },

    async fetchTypesEquipements() {
      if (this.selectedSalles.has('tous')) {
        const response = await getAllTypesEquipements();
        this.typesEquipements = response.data;
      } else {
        const lieuIds = Array.from(this.selectedSalles);
        const responses = await Promise.all(lieuIds.map(lieuId => getTypesEquipementsByLieu(lieuId)));
        this.typesEquipements = responses.flat().reduce((acc, type) => {
          if (!acc.find(t => t.id === type.id)) {
            acc.push(type);
          }
          return acc;
        }, []);
      }
    },

    async fetchEquipements() {
      if (this.selectedSalles.has('tous') && this.selectedTypes.has('tous')) {
        const response = await getAllEquipements();
        this.equipements = response.data;
      } else if (this.selectedSalles.size === 0 || this.selectedTypes.size === 0) {
        this.equipements = [];
      } else {
        const lieuIds = Array.from(this.selectedSalles);
        const typeIds = Array.from(this.selectedTypes);
        const responses = await getEquipementsByLieuxAndTypes(lieuIds, typeIds);
        this.equipements = responses.flat().reduce((acc, equipement) => {
          if (!acc.find(e => e.id === equipement.id)) {
            acc.push(equipement);
          }
          return acc;
        }, []);
      }
    },

    toggleSalleSelection(salleId) {
      if (salleId === 'tous') {
        this.selectedSalles = new Set(['tous']);
      } else {
        if (this.selectedSalles.has('tous')) {
          this.selectedSalles.delete('tous');
        }
        if (this.selectedSalles.has(salleId)) {
          this.selectedSalles.delete(salleId);
        } else {
          this.selectedSalles.add(salleId);
        }
      }
      this.fetchTypesEquipements();
      this.fetchEquipements();
    },

    toggleTypeEquipementSelection(typeId) {
      if (typeId === 'tous') {
        this.selectedTypes = new Set(['tous']);
      } else {
        if (this.selectedTypes.has('tous')) {
          this.selectedTypes.delete('tous');
        }
        if (this.selectedTypes.has(typeId)) {
          this.selectedTypes.delete(typeId);
        } else {
          this.selectedTypes.add(typeId);
        }
      }
      this.fetchEquipements();
    },

    isSalleSelected(salleId) {
      return this.selectedSalles.has(salleId);
    },

    isTypeEquipementSelected(typeId) {
      return this.selectedTypes.has(typeId);
    },

    handleItemSelected(item) {
      console.log('Selected item:', item);
    },
  },
};
</script>

<style scoped>
.text-primary {
  color: #05004E;
}

.text-dark {
  color: #3C3C3C;
}

.v-card {
  background-color: #FFFFFF;
}

.v-btn {
  background-color: #F1F5FF;
  border-radius: 50%;
}

h1 {
  color: #05004E;
}

.selected {
  background-color: #5D5FEF;
  color: #fff;
}
</style>
