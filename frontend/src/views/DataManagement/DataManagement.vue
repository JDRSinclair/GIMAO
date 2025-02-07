<template>
  <v-app>
    <v-main>
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <h1 class="text-h3 font-weight-bold text-primary mb-6 text-center">Gestion des Données</h1>
          </v-col>
        </v-row>
        <v-row justify="center">
          <v-col v-for="item in items" :key="item.name" cols="12" sm="6" md="4" lg="3">
            <v-card elevation="2" class="rounded-lg pa-4 mb-4 data-card" @click="navigateTo(item.route)">
              <v-card-text class="text-center">
                <v-icon :color="item.color" size="64" class="mb-4">{{ item.icon }}</v-icon>
                <h2 class="text-h5 font-weight-medium">{{ item.name }}</h2>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'DataManagement',
  data() {
    return {
      items: [
        { name: "Lieux", route: "/LocationList", icon: "mdi-map-marker", color: "blue" },
        { name: "Consommables", route: "/ConsummableList", icon: "mdi-package-variant", color: "green" },
        { name: "Fournisseurs", route: "/SupplierList", icon: "mdi-truck", color: "orange" },
        { name: "Fabricants", route: "/ManufacturerList", icon: "mdi-factory", color: "red" },
        { name: "Modeles Equipements", route: "/modeles-equipements", icon: "mdi-cog", color: "purple" },
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

.data-card {
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
}

.data-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1) !important;
}

.v-icon {
  transition: transform 0.3s;
}

.data-card:hover .v-icon {
  transform: scale(1.1);
}
</style>