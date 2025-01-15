<template>
  <v-app>
    <!-- Contenu principal -->
    <v-main>
      <v-container>
        <!-- Filtres et tableau -->
        <v-row>
          <!-- Colonne contenant les filtres -->
          <v-col cols="12">
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Gestion des Données</v-card-title>
              <v-divider></v-divider>
              <v-list dense>
                <v-list-item v-for="item in items" :key="item.name" @click="navigateTo(item.route)">
                  <v-list-item-title>{{ item.name }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'GestionDonnees',
  data() {
    return {
      items: [
        { name: "Lieux", route: "/lieux" },
        { name: "Consommables", route: "/consommables" },
        { name: "Fournisseurs", route: "/fournisseurs" },
        { name: "Fabricants", route: "/fabricants" },
        { name: "Modeles Equipements", route: "/modeles-equipements" },
        { name: "Interventions", route: "/interventions" }
      ],
    };
  },
  methods: {
    navigateTo(route) {
      this.$router.push(route);
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
</style>
