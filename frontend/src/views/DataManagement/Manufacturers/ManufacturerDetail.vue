<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card v-if="fabricant">
          <v-card-title>Détails du fabricant</v-card-title>
          <v-card-text>
            <v-alert v-if="errorMessage" type="error">
              {{ errorMessage }}
            </v-alert>
            <v-list>
              <v-list-item>
                <v-list-item-title>Nom du fabricant:</v-list-item-title>
                <v-list-item-subtitle>{{ fabricant.nomFabricant }}</v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Adresse:</v-list-item-title>
                <v-list-item-subtitle>
                  {{ fabricant.numRue }} {{ fabricant.nomRue }}, {{ fabricant.codePostal }} {{ fabricant.ville }}
                </v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Pays:</v-list-item-title>
                <v-list-item-subtitle>{{ fabricant.paysFabricant }}</v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Email:</v-list-item-title>
                <v-list-item-subtitle>{{ fabricant.mailFabricant }}</v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Téléphone:</v-list-item-title>
                <v-list-item-subtitle>{{ fabricant.numTelephoneFabricant }}</v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Service Après-Vente:</v-list-item-title>
                <v-list-item-subtitle>{{ fabricant.serviceApresVente ? 'Oui' : 'Non' }}</v-list-item-subtitle>
              </v-list-item>
            </v-list>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="goBack">
              Retour
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
        <v-alert v-else-if="isLoading" type="info">
          Chargement du fabricant...
        </v-alert>
        <v-alert v-else type="warning">
          Fabricant non trouvé
        </v-alert>
      </v-col>
    </v-row>
    <v-dialog v-model="showDeleteConfirmation" max-width="300">
      <v-card>
        <v-card-title>Confirmer la suppression</v-card-title>
        <v-card-text>
          Êtes-vous sûr de vouloir supprimer ce fabricant ?
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" text @click="showDeleteConfirmation = false">Annuler</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import api from '@/services/api';

export default {
  setup() {
    const router = useRouter();
    const route = useRoute();
    const fabricant = ref(null);
    const errorMessage = ref('');
    const isLoading = ref(true);
    const showDeleteConfirmation = ref(false);

    const getFabricant = async () => {
      isLoading.value = true;
      errorMessage.value = '';
      try {
        const response = await api.getFabricant(route.params.id);
        fabricant.value = response.data;
      } catch (error) {
        console.error('Error fetching fabricant:', error);
        errorMessage.value = 'Erreur lors de la récupération du fabricant.';
      } finally {
        isLoading.value = false;
      }
    };

    const goBack = () => {
      router.go(-1);
    };

    onMounted(() => {
      getFabricant();
    });

    return {
      fabricant,
      errorMessage,
      isLoading,
      goBack,
      showDeleteConfirmation
    };
  }
};
</script>