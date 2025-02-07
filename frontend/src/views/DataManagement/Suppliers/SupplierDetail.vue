<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card v-if="fournisseur">
          <v-card-title>Détails du fournisseur</v-card-title>
          <v-card-text>
            <v-alert v-if="errorMessage" type="error">
              {{ errorMessage }}
            </v-alert>
            <v-list>
              <v-list-item>
                <v-list-item-title>Nom du fournisseur:</v-list-item-title>
                <v-list-item-subtitle>{{ fournisseur.nomFournisseur }}</v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Adresse:</v-list-item-title>
                <v-list-item-subtitle>
                  {{ fournisseur.numRue }} {{ fournisseur.nomRue }}, {{ fournisseur.codePostal }} {{ fournisseur.ville }}
                </v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Pays:</v-list-item-title>
                <v-list-item-subtitle>{{ fournisseur.paysFournisseur }}</v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Email:</v-list-item-title>
                <v-list-item-subtitle>{{ fournisseur.mailFournisseur }}</v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Téléphone:</v-list-item-title>
                <v-list-item-subtitle>{{ fournisseur.numTelephoneFournisseur }}</v-list-item-subtitle>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>Service Après-Vente:</v-list-item-title>
                <v-list-item-subtitle>{{ fournisseur.serviceApresVente ? 'Oui' : 'Non' }}</v-list-item-subtitle>
              </v-list-item>
            </v-list>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click="go_back">
              Retour
            </v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
        <v-alert v-else-if="isLoading" type="info">
          Chargement du fournisseur...
        </v-alert>
        <v-alert v-else type="warning">
          Fournisseur non trouvé
        </v-alert>
      </v-col>
    </v-row>
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
    const fournisseur = ref(null);
    const errorMessage = ref('');
    const isLoading = ref(true);
    const showDeleteConfirmation = ref(false);

    const get_supplier = async () => {
      isLoading.value = true;
      errorMessage.value = '';
      try {
        const response = await api.getFournisseur(route.params.id);
        fournisseur.value = response.data;
      } catch (error) {
        console.error('Error fetching fournisseur:', error);
        errorMessage.value = 'Erreur lors de la récupération du fournisseur.';
      } finally {
        isLoading.value = false;
      }
    };

    const go_back = () => {
      router.go(-1);
    };

    onMounted(() => {
      get_supplier();
    });

    return {
      fournisseur,
      errorMessage,
      isLoading,
      go_back,
      showDeleteConfirmation
    };
  }
};
</script>