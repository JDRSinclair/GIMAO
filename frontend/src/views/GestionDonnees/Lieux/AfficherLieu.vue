<template>
    <v-app>
      <v-main>
        <v-container>
          <v-card v-if="lieu">
            <v-card-title>Détails du lieu</v-card-title>
            <v-card-text>
              <v-list>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Nom du lieu</v-list-item-title>
                    <v-list-item-subtitle>{{ lieu.nomLieu }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item>
                  <v-list-item-content>
                    <v-list-item-title>Type de lieu</v-list-item-title>
                    <v-list-item-subtitle>{{ lieu.typeLieu }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item v-if="lieu.lieuParent">
                  <v-list-item-content>
                    <v-list-item-title>Lieu parent</v-list-item-title>
                    <v-list-item-subtitle>{{ lieu.lieuParent.nomLieu }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
          <v-alert v-else type="error">Lieu non trouvé</v-alert>
          <v-btn color="primary" class="mt-4" @click="retour">Retour</v-btn>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  import api from '@/services/api';
  import { ref, onMounted } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  
  export default {
    name: 'AfficherLieu',
    setup() {
      const router = useRouter();
      const route = useRoute();
      const lieu = ref(null);
  
      const fetchLieu = async () => {
        try {
          const response = await api.getLieu(route.params.id);
          lieu.value = response.data;
        } catch (error) {
          console.error('Erreur lors du chargement du lieu :', error);
        }
      };
  
      const retour = () => {
        router.go(-1);
      };
  
      onMounted(() => {
        fetchLieu();
      });
  
      return {
        lieu,
        retour,
      };
    },
  };
  </script>