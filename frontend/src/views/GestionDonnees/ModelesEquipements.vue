<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <v-col>
            <v-btn color="primary" class="mb-4" @click="navigateToCreerModeleEquipement">
              Ajouter Modele Equipement
            </v-btn>
            <v-data-table
              :headers="headers"
              :items="modelesEquipements"
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
  name: 'ModelesEquipements',
  setup() {
    const router = useRouter();
    const page = ref(1);
    const pageCount = ref(0);
    const itemsPerPage = ref(5);
    const modelesEquipements = ref([]);

    const headers = ref([
      { text: 'Nom', value: 'nomModeleEquipement' },
      { text: 'Fabricant', value: 'fabricant' },
    ]);

    const fetchModelesEquipements = async () => {
      try {
        const response = await api.getModeleEquipements();
        modelesEquipements.value = response.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des modeles equipements:', error);
      }
    };

    onMounted(fetchModelesEquipements);

    const navigateToCreerModeleEquipement = () => {
      router.push('/creer-modeles-equipements');
    };

    return {
      page,
      pageCount,
      itemsPerPage,
      modelesEquipements,
      headers,
      navigateToCreerModeleEquipement
    };
  },
};
</script>

<style scoped>
.v-card {
  background-color: #FFFFFF;
}
</style>
