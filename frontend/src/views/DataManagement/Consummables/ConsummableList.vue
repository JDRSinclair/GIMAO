<template>
  <v-container>    
    <v-row class="mb-4">
      <!-- Barre de recherche -->
      <v-col cols="9">
        <v-text-field
          v-model="searchQuery"
          label="Rechercher un consommable"
          prepend-icon="mdi-magnify"
          clearable
        ></v-text-field>
      </v-col>
      <v-col cols="3" class="align-center">
        <v-btn 
          color="primary" 
          @click="$router.push('/CreateConsummable')"
          class="ml-2"
          height="50%"
        >
          Créer un consommable
        </v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-for="consommable in filteredConsommables" :key="consommable.id" cols="12" sm="6" md="4">
        <v-card @click="goToConsommableDetails(consommable.id)">
          <v-img
            :src="consommable.lienImageConsommable"
            height="200px"
            cover
          ></v-img>
          <v-card-title>{{ consommable.designation }}</v-card-title>
          <v-card-text>
            Fabricant: {{ consommable.fabricantNom }}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from '@/services/api';

export default {
  name: 'ConsummableList',
  data() {
    return {
      consommables: [],
      fabricants: [],
      searchQuery: ''
    };
  },
  computed: {
    consommablesWithFabricants() {
      return this.consommables.map(consommable => {
        const fabricant = this.fabricants.find(f => f.id === consommable.fabricant);
        return {
          ...consommable,
          fabricantNom: fabricant ? fabricant.nomFabricant : 'Inconnu'
        };
      });
    },
    filteredConsommables() {
      if (!this.searchQuery) {
        return this.consommablesWithFabricants;
      }
      const searchLower = this.searchQuery.toLowerCase();
      return this.consommablesWithFabricants.filter(consommable => 
        consommable.designation.toLowerCase().includes(searchLower)
      );
    }
  },
  methods: {
    async fetchConsommables() {
      try {
        const response = await api.getConsommables();
        this.consommables = response.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des consommables:', error);
      }
    },
    async fetchFabricants() {
      try {
        const response = await api.getFabricants();
        this.fabricants = response.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des fabricants:', error);
      }
    },
    goToConsommableDetails(id) {
      this.$router.push(`/afficher-consommable/${id}`);
    }
  },
  async created() {
    await Promise.all([this.fetchConsommables(), this.fetchFabricants()]);
  }
}
</script>