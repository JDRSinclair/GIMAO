<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card v-if="consommable">
          <v-card-title>Détails du consommable</v-card-title>
          <v-card-text>
            <v-alert v-if="errorMessage" type="error">
              {{ errorMessage }}
            </v-alert>
            <v-img
              v-if="consommable.lienImageConsommable"
              :src="consommable.lienImageConsommable"
              height="200"
              contain
            ></v-img>
            <v-list>
              <v-list-item>
                <v-list-item-title>Désignation:</v-list-item-title>
                <v-list-item-subtitle>{{ consommable.designation }}</v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Fabricant:</v-list-item-title>
                <v-list-item-subtitle>{{ fabricantNom }}</v-list-item-subtitle>
              </v-list-item>
            </v-list>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="goBack">
              Retour
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn color="error" @click="confirmDelete">
              Supprimer
            </v-btn>
          </v-card-actions>
        </v-card>
        <v-alert v-else-if="isLoading" type="info">
          Chargement du consommable...
        </v-alert>
        <v-alert v-else type="warning">
          Consommable non trouvé
        </v-alert>
      </v-col>
    </v-row>
    <v-dialog v-model="showDeleteConfirmation" max-width="300">
      <v-card>
        <v-card-title>Confirmer la suppression</v-card-title>
        <v-card-text>
          Êtes-vous sûr de vouloir supprimer ce consommable ?
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" text @click="showDeleteConfirmation = false">Annuler</v-btn>
          <v-btn color="error" text @click="deleteConsommable">Supprimer</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import api from '@/services/api';

export default {
  setup() {
    const router = useRouter();
    const route = useRoute();
    const consommable = ref(null);
    const fabricant = ref(null);
    const errorMessage = ref('');
    const isLoading = ref(true);
    const showDeleteConfirmation = ref(false);

    const fabricantNom = computed(() => {
      return fabricant.value ? fabricant.value.nomFabricant : 'Non spécifié';
    });

    const getConsommable = async () => {
      isLoading.value = true;
      errorMessage.value = '';
      try {
        const response = await api.getConsommable(route.params.id);
        consommable.value = response.data;
        if (consommable.value.fabricant) {
          await getFabricant(consommable.value.fabricant);
        }
      } catch (error) {
        console.error('Error fetching consommable:', error);
        errorMessage.value = 'Erreur lors de la récupération du consommable.';
      } finally {
        isLoading.value = false;
      }
    };

    const getFabricant = async (id) => {
      try {
        const response = await api.getFabricant(id);
        fabricant.value = response.data;
      } catch (error) {
        console.error('Error fetching fabricant:', error);
        errorMessage.value = 'Erreur lors de la récupération du fabricant.';
      }
    };

    const goBack = () => {
      router.go(-1);
    };

    const confirmDelete = () => {
      showDeleteConfirmation.value = true;
    };

    const deleteConsommable = async () => {
      try {
        await api.deleteConsommable(consommable.value.id);
        showDeleteConfirmation.value = false;
        router.push({ name: 'ListeConsommables' }); 
      } catch (error) {
        console.error('Error deleting consommable:', error);
      }
      goBack();
    };

    onMounted(() => {
      getConsommable();
    });

    return {
      consommable,
      fabricantNom,
      errorMessage,
      isLoading,
      goBack,
      confirmDelete,
      deleteConsommable,
      showDeleteConfirmation
    };
  }
};
</script>