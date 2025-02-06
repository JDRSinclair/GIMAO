<template>
  <v-container>
    <v-row class="mb-4">
      <!-- Barre de recherche -->
      <v-col cols="9">
        <v-text-field
          v-model="searchQuery"
          label="Rechercher un fournisseur"
          prepend-icon="mdi-magnify"
          clearable
        ></v-text-field>
      </v-col>
      <v-col cols="3" class="align-center">
        <v-btn 
          color="primary"
          @click="$router.push('/creer-fournisseur')"
          class="ml-2"
          height="50%"
        >
          Créer un fournisseur
        </v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-for="fournisseur in filteredFournisseurs" :key="fournisseur.id" cols="12" sm="6" md="4">
        <v-card @click="goToFournisseurDetails(fournisseur.id)">
          <v-card-title>{{ fournisseur.nomFournisseur }}</v-card-title>
          <v-card-text>
            <p>Ville: {{ fournisseur.ville }}</p>
            <p>Pays: {{ fournisseur.paysFournisseur }}</p>
            <p>Email: {{ fournisseur.mailFournisseur }}</p>
            <p>Service Après-Vente: {{ fournisseur.serviceApresVente ? 'Oui' : 'Non' }}</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from '@/services/api';

export default {
  name: 'ListeFournisseurs',
  data() {
    return {
      fournisseurs: [],
      searchQuery: ''
    };
  },
  computed: {
    filteredFournisseurs() {
      if (!this.searchQuery) {
        return this.fournisseurs;
      }
      const searchLower = this.searchQuery.toLowerCase();
      return this.fournisseurs.filter(fournisseur => 
        fournisseur.nomFournisseur.toLowerCase().includes(searchLower) ||
        fournisseur.ville.toLowerCase().includes(searchLower) ||
        fournisseur.paysFournisseur.toLowerCase().includes(searchLower)
      );
    }
  },
  methods: {
    async fetchFournisseurs() {
      try {
        const response = await api.getFournisseurs();
        this.fournisseurs = response.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des fournisseurs:', error);
      }
    },
    goToFournisseurDetails(id) {
      this.$router.push(`/afficher-fournisseur/${id}`);
    }
  },
  created() {
    this.fetchFournisseurs();
  }
}
</script>