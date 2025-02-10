<template>
    <v-container>
      <v-card>
        <v-card-title>Ajouter des documents à l'intervention</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="submitForm">
            <v-container>
              <v-row v-for="(document, index) in documents" :key="index">
                <v-col cols="5">
                  <v-text-field
                    v-model="document.nom"
                    label="Nom du document"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="5">
                  <v-file-input
                    v-model="document.fichier"
                    label="Fichier du document"
                    required
                  ></v-file-input>
                </v-col>
                <v-col cols="2">
                  <v-btn color="error" @click="removeDocument(index)" icon>
                    <v-icon>mdi-delete</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
            <v-btn color="secondary" @click="retour" class="mb-4 mr-2">
              Retour
            </v-btn>
            
            <v-btn color="secondary" @click="addDocument" class="mb-4">
              Ajouter un autre document
            </v-btn>
            <v-btn type="submit" color="primary" block>Enregistrer tous les documents</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
      <v-snackbar v-model="snackbar.show" :color="snackbar.color">
        {{ snackbar.message }}
      </v-snackbar>
    </v-container>
  </template>
  
  <script>
  import { ref, reactive } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import api from '@/services/api';
  
  export default {
    name: 'AjouterDocumentIntervention',
    setup() {
      const route = useRoute();
      const router = useRouter();
      const documents = ref([{ nom: '', fichier: null }]);
      const snackbar = reactive({
        show: false,
        message: '',
        color: 'success'
      });
  
      const addDocument = () => {
        documents.value.push({ nom: '', fichier: null });
      };

      const retour = () => {
      router.go(-1);
      };
  
      const removeDocument = (index) => {
        documents.value.splice(index, 1);
      };
  
      const showSnackbar = (message, color = 'success') => {
        snackbar.message = message;
        snackbar.color = color;
        snackbar.show = true;
      };
  
      const submitForm = async () => {
        try {
          const interventionId = route.params.id;
          let allSuccess = true;
  
          for (const doc of documents.value) {
            if (doc.nom && doc.fichier) {
              const formData = new FormData();
              formData.append('nomDocumentIntervention', doc.nom);
              formData.append('lienDocumentIntervention', doc.fichier);
              formData.append('intervention', interventionId);
  
              try {
                const response = await api.postInterventionDocument(formData);
                console.log('Document enregistré:', response.data);
              } catch (error) {
                console.error('Erreur lors de l\'ajout du document:', error);
                allSuccess = false;
              }
            }
          }
  
          if (allSuccess) {
            showSnackbar('Tous les documents ont été enregistrés avec succès');
            router.push({ name: 'AfficherIntervention', params: { id: interventionId } });
          } else {
            showSnackbar('Certains documents n\'ont pas pu être enregistrés', 'warning');
          }
        } catch (error) {
          console.error('Erreur générale lors de l\'ajout des documents:', error);
          showSnackbar('Erreur lors de l\'ajout des documents. Veuillez réessayer.', 'error');
        }
      };
  
      return {
        documents,
        addDocument,
        removeDocument,
        submitForm,
        snackbar,
        retour
      };
    },
  };
  </script>
  
  <style scoped>
  /* ajouter des styles spécifiques ici si nécessaire */
  </style>