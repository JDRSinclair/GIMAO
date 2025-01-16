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
              :items-per-page="itemsPerPage"
              :page.sync="page"
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
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/services/api';

export default {
  name: 'Fournisseurs',
  setup() {
    const router = useRouter();
    const page = ref(1);
    const pageCount = ref(0);
    const itemsPerPage = ref(5);
    const fournisseurs = ref([]);

    const headers = [
      { text: 'Nom', value: 'nomFournisseur' },
      { text: 'Ville', value: 'ville' },
      { text: 'Pays', value: 'paysFournisseur' },
      { text: 'Email', value: 'mailFournisseur' },
      { text: 'Téléphone', value: 'numTelephoneFournisseur' },
    ];

    const fetchFournisseurs = async () => {
      try {
        const response = await api.getFournisseurs();
        fournisseurs.value = response.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des fournisseurs:', error);
      }
    };

    onMounted(fetchFournisseurs);

    const navigateToCreerFournisseurs = () => {
      router.push('/creer-fournisseurs');
    };

    return {
      page,
      pageCount,
      itemsPerPage,
      fournisseurs,
      headers,
      navigateToCreerFournisseurs
    };
  },
};
</script>

<style scoped>
.v-card {
  background-color: #FFFFFF;
}
</style>