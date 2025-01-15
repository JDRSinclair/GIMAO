<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <v-col>
            <v-btn color="primary" class="mb-4" @click="navigateToCreerFournisseurs">
              Ajouter Fournisseur
            </v-btn>
            <v-data-table
              :headers="headers"
              :items="fournisseurs"
              :items-per-page="5"
              class="elevation-1 rounded-lg"
            ></v-data-table>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'Fournisseurs',
  data() {
    return {
      headers: [
        { text: 'Nom', value: 'nom' },
        { text: 'Adresse', value: 'adresse' },
        { text: 'Ville', value: 'ville' },
        { text: 'Pays', value: 'pays' },
        { text: 'Email', value: 'email' },
        { text: 'Téléphone', value: 'telephone' },
      ],
      fournisseurs: [
        { nom: 'Leroy Merlin', adresse: '123 Rue de Paris', ville: 'Paris', pays: 'France', email: 'contact@leroymerlin.fr', telephone: '0123456789' },
        { nom: 'Castorama', adresse: '456 Avenue de Lyon', ville: 'Lyon', pays: 'France', email: 'contact@castorama.fr', telephone: '0987654321' },
        { nom: 'Bricorama', adresse: '789 Boulevard de Marseille', ville: 'Marseille', pays: 'France', email: 'contact@bricorama.fr', telephone: '0147258369' },
      ],
    };
  },
  methods: {
    navigateToCreerFournisseurs() {
      this.$router.push('/creer-fournisseurs');
    },
  },
};
</script>

<style scoped>
.v-card {
  background-color: #FFFFFF;
}
</style>
