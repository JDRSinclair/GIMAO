<template>
  <v-container>
    <v-row class="mb-4">
      <!-- Barre de recherche -->
      <v-col cols="9">
        <v-text-field
          v-model="searchQuery"
          label="Rechercher un fabricant"
          prepend-icon="mdi-magnify"
          clearable
        ></v-text-field>
      </v-col>
      <v-col cols="3" class="align-center">
        <v-btn 
          color="primary"
          @click="$router.push('/CreateManufacturer')"
          class="ml-2"
          height="50%"
        >
          Créer un fabricant
        </v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-for="fabricant in filteredFabricants" :key="fabricant.id" cols="12" sm="6" md="4">
        <v-card @click="go_to_manufacturer_detail(fabricant.id)">
          <v-card-title>{{ fabricant.nomFabricant }}</v-card-title>
          <v-card-text>
            <p>Pays: {{ fabricant.paysFabricant }}</p>
            <p>Email: {{ fabricant.mailFabricant }}</p>
            <p>Téléphone: {{ fabricant.numTelephoneFabricant }}</p>
            <p>Service Après-Vente: {{ fabricant.serviceApresVente ? 'Oui' : 'Non' }}</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from '@/services/api';

export default {
  name: 'ListeFabricants',
  data() {
    return {
      fabricants: [],
      searchQuery: ''
    };
  },
  computed: {
    filtered_manufacturer() {
      if (!this.searchQuery) {
        return this.fabricants;
      }
      const searchLower = this.searchQuery.toLowerCase();
      return this.fabricants.filter(fabricant => 
        fabricant.nomFabricant.toLowerCase().includes(searchLower) ||
        fabricant.paysFabricant.toLowerCase().includes(searchLower) ||
        fabricant.mailFabricant.toLowerCase().includes(searchLower)
      );
    }
  },
  methods: {
    async fetch_manufacturer() {
      try {
        const response = await api.getFabricants();
        this.fabricants = response.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des fabricants:', error);
      }
    },
    go_to_manufacturer_detail(id) {
      this.$router.push(`/ManufacturerDetail/${id}`);
    }
  },
  created() {
    this.fetch_manufacturer();
  }
}
</script>