<template>
  <v-app>
    <!-- Contenu principal -->
    <v-main>
      <v-container>
        <!-- Filtres et tableau -->
        <v-row>
          <!-- Colonne contenant le filtre de type de bon -->
          <v-col cols="3">
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Type de bon</v-card-title>
              <v-divider></v-divider>
              <v-list dense>
                <v-list-item v-for="(type, index) in typesDeBon" :key="index" link @click="filterByType(type)">
                  <v-list-item-title>{{ type }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>

          <!-- Tableau des bons de travail -->
          <v-col cols="9">
            <v-data-table
              :headers="headers"
              :items="filteredBonsDeTravail"
              :items-per-page="itemsPerPage"
              :page.sync="page"
              item-value="name"
              class="elevation-1 rounded-lg"
              @page-count="pageCount = $event"
            ></v-data-table>
            <div class="text-center pt-2">
              <v-pagination
                v-model="page"
                :length="pageCount"
              ></v-pagination>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { ref } from 'vue';
import '@/assets/css/global.css';

export default {
  name: 'BonsDeTravail',
  setup() {
    const page = ref(1);
    const pageCount = ref(0);
    const itemsPerPage = ref(5);

    return {
      page,
      pageCount,
      itemsPerPage
    };
  },
  data() {
    return {
      typesDeBon: ["Tous", "Demande d'intervention", "Bon de travail", "Bon de travail terminé"],
      headers: [
        { text: "Équipement", value: "equipement" },
        { text: "Date de début", value: "dateDebut" },
        { text: "Technicien", value: "technicien" },
        { text: "Type de bon", value: "typeDeBon" },
      ],
      bonsDeTravail: [
        { equipement: "Équipement 1", dateDebut: "09/02/2024", technicien: "Demande d'intervention", typeDeBon: "Demande d'intervention" },
        { equipement: "Équipement 2", dateDebut: "09/02/2024", technicien: "Demande d'intervention", typeDeBon: "Demande d'intervention" },
        { equipement: "Équipement 3", dateDebut: "07/02/2024", technicien: "Demande d'intervention", typeDeBon: "Demande d'intervention" },
        { equipement: "Équipement 4", dateDebut: "03/02/2024", technicien: "Tech 5", typeDeBon: "Bon de travail" },
        { equipement: "Équipement 5", dateDebut: "01/02/2024", technicien: "Tech 6", typeDeBon: "Bon de travail" },
        { equipement: "Équipement 6", dateDebut: "21/01/2024", technicien: "Tech 7", typeDeBon: "Bon de travail terminé" },
        { equipement: "Équipement 7", dateDebut: "14/01/2024", technicien: "Tech 8", typeDeBon: "Bon de travail terminé" },
        { equipement: "Équipement 8", dateDebut: "07/01/2024", technicien: "Tech 8", typeDeBon: "Bon de travail terminé" },
      ],
      filteredBonsDeTravail: [],
    };
  },
  methods: {
    filterByType(type) {
      if (type === "Tous") {
        this.filteredBonsDeTravail = this.bonsDeTravail;
      } else {
        this.filteredBonsDeTravail = this.bonsDeTravail.filter(bon => bon.typeDeBon === type);
      }
    },
  },
  mounted() {
    this.filteredBonsDeTravail = this.bonsDeTravail;
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
</style>