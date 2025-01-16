<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title>Ajouter un nouveau fabricant</v-card-title>
          <v-card-text>
            <v-alert v-if="errorMessage" type="error">
              {{ errorMessage }}
            </v-alert>
            <v-form @submit.prevent="submitForm">
              <v-text-field
                v-model="fabricant.nomFabricant"
                label="Nom du fabricant"
                required
              ></v-text-field>
              
              <v-text-field
                v-model="fabricant.paysFabricant"
                label="Pays"
                required
              ></v-text-field>
              
              <v-text-field
                v-model="fabricant.mailFabricant"
                label="Email"
                type="email"
                required
              ></v-text-field>
              
              <v-text-field
                v-model="fabricant.numTelephoneFabricant"
                label="Numéro de téléphone"
                required
              ></v-text-field>
              
              <v-switch
                v-model="fabricant.serviceApresVente"
                label="Service Après-Vente"
              ></v-switch>
              
              <v-btn color="secondary" class="mt-4 mr-2" @click="goBack">
                Retour
              </v-btn>
              <v-btn type="submit" color="primary" class="mt-4" :disabled="!isFormValid">
                Ajouter le fabricant
              </v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/services/api';

export default {
  setup() {
    const router = useRouter();
    const fabricant = ref({
      nomFabricant: '',
      paysFabricant: '',
      mailFabricant: '',
      numTelephoneFabricant: '',
      serviceApresVente: false
    });
    const errorMessage = ref('');

    const isFormValid = computed(() => {
      return fabricant.value.nomFabricant &&
             fabricant.value.paysFabricant &&
             fabricant.value.mailFabricant &&
             fabricant.value.numTelephoneFabricant;
    });

    const submitForm = async () => {
      if (!isFormValid.value) {
        errorMessage.value = 'Veuillez remplir tous les champs requis.';
        return;
      }

      try {
        const response = await api.postFabricant(fabricant.value);
        console.log('Fabricant créé:', response.data);
        goBack();
      } catch (error) {
        console.error('Error creating fabricant:', error);
        errorMessage.value = 'Une erreur est survenue lors de la création du fabricant.';
      }
    };

    const goBack = () => {
      router.go(-1);
    };

    return {
      fabricant,
      errorMessage,
      isFormValid,
      submitForm,
      goBack
    };
  }
};
</script>