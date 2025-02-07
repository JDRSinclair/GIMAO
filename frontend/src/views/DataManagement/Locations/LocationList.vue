<template>
  <v-container>
    <v-row>
      <v-card elevation="1" class="rounded-lg pa-4 mb-4" style="min-width: 800px; width: 100%; min-height: 400px;">
        <v-card-title class="font-weight-bold text-uppercase text-primary d-flex justify-space-between align-center">
          <span>Liste des lieux</span>
          <v-btn 
            color="primary"
            @click="go_to_add_location_page"
            small
            class="ml-4"
          >
            Ajouter un lieu
          </v-btn>
        </v-card-title>
        <v-divider></v-divider>
        <LieuxExplorer 
          :lieux="lieux" 
          @select-lieu="on_location_select"
        />
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import { ref, onMounted, reactive, toRefs } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/services/api';
import LieuxExplorer from '@/components/LieuxExplorer.vue';

export default {
  name: 'Lieux',
  components: {
    LieuxExplorer,
  },
  setup() {
    const router = useRouter();
    const state = reactive({
      lieux: [],
      selectedLieu: null,
    });

    const fetch_data = async () => {
      try {
        const { data } = await api.getLieuxHierarchy();
        state.lieux = data;
      } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
      }
    };

    const go_to_add_location_page = () => router.push('/CreateLocation');

    const on_location_select = (lieu) => {
      state.selectedLieu = lieu;
    };

    onMounted(fetch_data);

    return {
      ...toRefs(state),
      go_to_add_location_page,
      on_location_select,
    };
  }
};
</script>

<style scoped>
.pa-4 { padding: 32px; }
</style>