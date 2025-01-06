<template>
  <v-app>
    <!-- Contenu principal -->
    <v-main>
      <v-container>
        <!-- Filtres et tableau -->
        <v-row>
          <!-- Colonne contenant le filtre de type de bon -->
          <v-col cols="3"> <!-- Réduit la largeur à 3/12 -->
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
          <v-col cols="9"> <!-- Augmente la largeur à 9/12 -->
            <v-data-table
              :headers="headers"
              :items="bonsDeTravail"
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
import '@/assets/css/global.css'; // Importation du fichier CSS global

export default {
  name: 'BonsDeTravail',
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
