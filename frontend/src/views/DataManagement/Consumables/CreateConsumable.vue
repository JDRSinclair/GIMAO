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
            <v-form @submit.prevent="submit_form">
              <v-text-field
                v-model="consumable.designation"
                label="Désignation"
                required
              ></v-text-field>
              
              <v-file-input
                v-model="consumable.lienImageConsommable"
                label="Image du consommable"
                accept="image/*"
                prepend-icon="mdi-camera"
              ></v-file-input>
              
              <v-select
                v-if="!isLoading && fabricants.length > 0"
                v-model="consumable.fabricant"
                :items="fabricants"
                item-title="nomFabricant"
                item-value="id"
                label="Fabricant"
                required
                return-object
              ></v-select>
              
              <v-btn color="secondary" class="mt-4 mr-2" @click="go_back">
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
    const consumable = ref({
      designation: '',
      lienImageConsommable: null,
      fabricant: null
    });
    const fabricants = ref([]);
    const errorMessage = ref('');
    const isLoading = ref(false);

    const isFormValid = computed(() => {
      return consumable.value.designation && 
             consumable.value.fabricant && 
             consumable.value.lienImageConsommable;
    });

    const get_manufacturers = async () => {
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

    const submit_form = async () => {
      if (!isFormValid.value) {
        errorMessage.value = 'Veuillez remplir tous les champs requis.';
        return;
      }

      try {
        const formData = new FormData();
        formData.append('designation', consumable.value.designation);
        formData.append('fabricant', consumable.value.fabricant.id);
        if (consumable.value.lienImageConsommable) {
          formData.append('lienImageConsommable', consumable.value.lienImageConsommable);
        }

        const response = await api.postConsommable(formData);
        console.log('Consommable créé:', response.data);
        
        go_back();
      } catch (error) {
        console.error('Error creating consommable:', error);

      }
    };

    const go_back = () => {
      router.go(-1);
    };

    const handle_file_change = (file) => {
      consumable.value.lienImageConsommable = file;
    };

    onMounted(() => {
      get_manufacturers();
    });

    return {
      consumable,
      fabricants,
      errorMessage,
      isLoading,
      isFormValid,
      submit_form,
      go_back,
      handle_file_change
    };
  }
};
</script>