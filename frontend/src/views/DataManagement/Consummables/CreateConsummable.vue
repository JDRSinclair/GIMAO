<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title>Ajouter un nouveau consommable</v-card-title>
          <v-card-text>
            <v-alert v-if="errorMessage" type="error">
              {{ errorMessage }}
            </v-alert>
            <v-alert v-if="isLoading" type="info">
              Chargement des fabricants...
            </v-alert>
            <v-form @submit.prevent="submitForm">
              <v-text-field
                v-model="consommable.designation"
                label="Désignation"
                required
              ></v-text-field>
              
              <v-file-input
                v-model="consommable.lienImageConsommable"
                label="Image du consommable"
                accept="image/*"
                prepend-icon="mdi-camera"
              ></v-file-input>
              
              <v-select
                v-if="!isLoading && fabricants.length > 0"
                v-model="consommable.fabricant"
                :items="fabricants"
                item-title="nomFabricant"
                item-value="id"
                label="Fabricant"
                required
                return-object
              ></v-select>
              
              <v-btn color="secondary" class="mt-4 mr-2" @click="goBack">
                Retour
              </v-btn>
              <v-btn type="submit" color="primary" class="mt-4" :disabled="!isFormValid">
                Ajouter le consommable
              </v-btn>
            </v-form>
            
            
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/services/api';

export default {
  setup() {
    const router = useRouter();
    const consommable = ref({
      designation: '',
      lienImageConsommable: null,
      fabricant: null
    });
    const fabricants = ref([]);
    const errorMessage = ref('');
    const isLoading = ref(false);

    const isFormValid = computed(() => {
      return consommable.value.designation && 
             consommable.value.fabricant && 
             consommable.value.lienImageConsommable;
    });

    const getFabricants = async () => {
      isLoading.value = true;
      errorMessage.value = '';
      try {
        const response = await api.getFabricants();
        fabricants.value = response.data;
        console.log('Fabricants récupérés:', JSON.stringify(fabricants.value, null, 2));
      } catch (error) {
        console.error('Error fetching fabricants:', error);
        errorMessage.value = 'Erreur lors de la récupération des fabricants.';
      } finally {
        isLoading.value = false;
      }
    };

    const submitForm = async () => {
      if (!isFormValid.value) {
        errorMessage.value = 'Veuillez remplir tous les champs requis.';
        return;
      }

      try {
        const formData = new FormData();
        formData.append('designation', consommable.value.designation);
        formData.append('fabricant', consommable.value.fabricant.id);
        if (consommable.value.lienImageConsommable) {
          formData.append('lienImageConsommable', consommable.value.lienImageConsommable);
        }

        const response = await api.postConsommable(formData);
        console.log('Consommable créé:', response.data);
        
        goBack();
      } catch (error) {
        console.error('Error creating consommable:', error);

      }
    };

    const goBack = () => {
      router.go(-1);
    };

    const handleFileChange = (file) => {
      consommable.value.lienImageConsommable = file;
    };

    onMounted(() => {
      getFabricants();
    });

    return {
      consommable,
      fabricants,
      errorMessage,
      isLoading,
      isFormValid,
      submitForm,
      goBack,
      handleFileChange
    };
  }
};
</script>