<template>
    <v-app>
      <v-main>
        <v-container>
          <v-card v-if="modelEquipment">
            <v-card-title>Détails du modele equipement</v-card-title>
            <v-card-text>
              <v-list>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Nom du modele equipement</v-list-item-title>
                    <v-list-item-subtitle>{{ modelEquipment.nomModeleEquipement }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Fabricant</v-list-item-title>
                    <v-list-item-subtitle>{{ modelEquipment.fabricant }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
          <v-alert v-else type="error">Modele Equipement non trouvé</v-alert>
          <v-btn color="primary" class="mt-4" @click="go_back">Retour</v-btn>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  import api from '@/services/api';
  import { ref, onMounted } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  
  export default {
    name: 'ModelEquipmentDetail',
    setup() {
      const router = useRouter();
      const route = useRoute();
      const modelEquipment = ref(null);
  
      const fetch_modelEquipment = async () => {
        try {
          const response = await api.getLieu(route.params.id);
          modelEquipment.value = response.data;
        } catch (error) {
          console.error('Error loading the modelEquipment:', error);
        }
      };
  
      const go_back = () => {
        router.go(-1);
      };
  
      onMounted(() => {
        fetch_modelEquipment();
      });
  
      return {
        modelEquipment,
        go_back,
      };
    },
  };
  </script>