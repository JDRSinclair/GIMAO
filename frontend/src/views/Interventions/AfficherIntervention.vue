<template>
  <v-app>
    <v-main>
      <v-container class="py-5">
        <v-card class="pa-4">
          <v-row v-if="intervention">
            <!-- Colonne de gauche avec les informations -->
            <v-col cols="6">
              <v-row>
                <v-col cols="12" v-for="(value, key) in formatLabelIntervention" :key="key">
                  <p><strong>{{ key }} :</strong> {{ value }}</p>
                </v-col>
              </v-row>
            </v-col>

            <!-- Colonne de droite avec les informations supplémentaires -->
            <v-col cols="6">
              <v-row>
                <v-col cols="12">
                  <p><strong>Commentaire d'intervention :</strong></p>
                  <p>{{ intervention.commentaireIntervention || 'Aucun commentaire' }}</p>
                </v-col>
                <v-col cols="12" v-if="intervention.commentaireRefusCloture">
                  <p><strong>Commentaire de refus de clôture :</strong></p>
                  <p>{{ intervention.commentaireRefusCloture }}</p>
                </v-col>
                <v-col cols="12">
                  <v-card 
                    class="mt-4 pa-4" 
                    elevation="2" 
                    @click="toggleDefaillanceDetails"
                    :class="{ 'expanded': showDefaillanceDetails }"
                  >
                    <v-card-title class="text-h6 d-flex align-center">
                      Défaillance
                      <v-spacer></v-spacer>
                      <v-btn
                        color="primary"
                        class="ml-2"
                        @click.stop="ouvrirDefaillance"
                        :disabled="!defaillanceId"
                      >
                        Ouvrir
                      </v-btn> 
                     
                        <v-icon>
                          {{ showDefaillanceDetails ? 'mdi-chevron-up' : 'mdi-chevron-down' }}
                        </v-icon>
                    </v-card-title>
                    <v-expand-transition>
                      <div v-show="showDefaillanceDetails">
                        <v-divider class="my-2"></v-divider>
                        <v-card-text>
                          <v-row>
                            <v-col cols="12" v-for="(value, key) in formatLabelDefaillance" :key="key">
                              <p><strong>{{ key }} :</strong> {{ value }}</p>
                            </v-col>
                          </v-row>
                        </v-card-text> 
                      </div>
                    </v-expand-transition>
                  </v-card>
                </v-col>
                
                <!-- Section pour les Documents d'intervention -->
                <v-col cols="12">
                  <v-card 
                    class="mt-4 pa-4" 
                    elevation="2"
                  >
                    <v-card-title class="text-h6 d-flex align-center">
                      Documents de l'intervention
                      <v-spacer></v-spacer>
                      <v-btn
                        color="primary"
                        small
                        class="mr-2"
                        @click="ajouterDocument"
                      >
                        Ajouter
                      </v-btn>
                      <v-btn icon @click="toggleDocumentsDetails">
                        <v-icon>
                          {{ showDocumentsDetails ? 'mdi-chevron-up' : 'mdi-chevron-down' }}
                        </v-icon>
                      </v-btn>
                    </v-card-title>
                    <v-expand-transition>
                      <div v-show="showDocumentsDetails">
                        <v-divider class="my-2"></v-divider>
                        <v-card-text>
                          <v-data-table
                            :headers="headers"
                            :items="intervention.liste_documents_intervention || []"
                            class="elevation-1"
                            hide-default-footer
                            :items-per-page="-1"
                          >
                            <template v-slot:top>
                              <v-toolbar flat>
                                <v-spacer></v-spacer>
                                <v-btn color="primary" small @click="toggleActionMode">
                                  {{ actionMode === 'download' ? 'Mode suppression' : 'Mode téléchargement' }}
                                </v-btn>
                              </v-toolbar>
                            </template>

                            <template v-slot:item.actions="{ item }">
                              <v-btn
                                icon
                                small
                                :color="actionMode === 'download' ? 'primary' : 'error'"
                                @click="actionMode === 'download' ? telechargerDocument(item) : supprimerDocument(item)"
                              >
                                <v-icon small>
                                  {{ actionMode === 'download' ? 'mdi-download' : 'mdi-delete' }}
                                </v-icon>
                              </v-btn>
                            </template>
                          </v-data-table>
                        </v-card-text> 
                      </div>
                    </v-expand-transition>
                  </v-card>
                </v-col>
              </v-row>
            </v-col>
          </v-row>

          <!-- Boutons -->
          <v-row justify="center" class="mt-4">
            <v-btn color="primary" class="text-white mx-2" @click="retour">
              Retour
            </v-btn>

            <v-btn color="error" class="text-white mx-2" @click="supprimerIntervention" :disabled="!canSupprimer">
              Supprimer l'intervention
            </v-btn>
            
            <v-btn color="warning" class="text-white mx-2" @click="reouvrirIntervention" :disabled="!canSupprimer">
              Rouvrir l'intervention
            </v-btn>

            <v-btn color="success" class="text-white mx-2" @click="cloturerIntervention" :disabled="!canCloturer">
              Clôturer l'intervention
            </v-btn>
          </v-row>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import api , { BASE_URL } from '@/services/api';

export default {
  name: 'AfficherIntervention',
  setup() {
    const router = useRouter();
    const route = useRoute();
    const actionMode = ref('download');
    const intervention = ref(null);
    const showDefaillanceDetails = ref(false);
    const showDocumentsDetails = ref(false);

    const retour = () => {
      router.go(-1);
    };

    const headers = [
      { title: 'Nom du document', value: 'nomDocumentIntervention' },
      { title: 'Actions', value: 'actions', sortable: false }
    ];

    const defaillanceId = computed(() => {
      return intervention.value?.defaillance?.id;
    });

    const ouvrirDefaillance = () => {
      if (defaillanceId.value) {
        router.push({ name: 'AfficherDefaillance', params: { id: defaillanceId.value } });
      }
    };

    const fetchData = async () => {
      try {
        const response = await api.getInterventionAffichage(route.params.id);
        intervention.value = response.data;
      } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
      }
    };

    const formatDate = (dateString) => {
      if (!dateString) return 'Non spécifié';
      const date = new Date(dateString);
      return date.toLocaleString('fr-FR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    };

    const formatLabelIntervention = computed(() => {
      if (!intervention.value) return {};
      return {
        'Nom de l\'intervention': intervention.value.nomIntervention,
        'Date d\'assignation': formatDate(intervention.value.dateAssignation),
        'Date de clôture': formatDate(intervention.value.dateCloture),
        'Date du début de l\'intervention': formatDate(intervention.value.dateDebutIntervention),
        'Date de fin de l\'intervention': formatDate(intervention.value.dateFinIntervention),
        'Temps estimé': intervention.value.tempsEstime,
        'Intervention curative' : intervention.value.interventionCurative ? 'Oui' : 'Non',
      };
    });

    const formatLabelDefaillance = computed(() => {
      if (!intervention.value || !intervention.value.defaillance) return {};
      const defaillance = intervention.value.defaillance;
      return {
        'Nom de la défaillance': defaillance.commentaireDefaillance,
        'Date de la défaillance': formatDate(defaillance.dateDefaillance),
        'Commentaire': defaillance.commentaireDefaillance || 'Aucun commentaire'
      };
    });

    const canSupprimer = computed(() => {
      return intervention.value && !intervention.value.dateCloture;
    });

    const canCloturer = computed(() => {
      return intervention.value && !intervention.value.dateCloture;
    });

    const toggleActionMode = () => {
      actionMode.value = actionMode.value === 'download' ? 'delete' : 'download';
    };

    const supprimerIntervention = async () => {
      if (confirm('Êtes-vous sûr de vouloir supprimer cette intervention ?')) {
        try {
          await api.deleteIntervention(intervention.value.id);
          router.push({ name: 'ListeInterventions' });
        } catch (error) {
          console.error('Erreur lors de la suppression de l\'intervention:', error);
        }
      }
    };

    const reouvrirIntervention = async () => {
      if (confirm('Êtes-vous sûr de vouloir rouvrir cette intervention ?')) {
        try {
          await api.reouvrirIntervention(intervention.value.id);
          fetchData(); // Recharger les données après la réouverture
        } catch (error) {
          console.error('Erreur lors de la réouverture de l\'intervention:', error);
        }
      }
    };

    const telechargerDocument = (item) => {
      const cleanedLink = item.lienDocumentIntervention.startsWith('/media/') 
        ? item.lienDocumentIntervention 
        : `/media/${item.lienDocumentIntervention.split('/media/').pop()}`;
      const fullUrl = `${BASE_URL}${cleanedLink}`;

      fetch(fullUrl)
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          return response.blob();
        })
        .then(blob => {
          const url = window.URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.style.display = 'none';
          a.href = url;
          a.download = item.nomDocumentIntervention;
          document.body.appendChild(a);
          a.click();
          window.URL.revokeObjectURL(url);
        })
        .catch(error => {
          console.error('Erreur lors du téléchargement:', error);
          alert('Erreur lors du téléchargement du fichier. Veuillez réessayer.');
        });
    };

  const supprimerDocument = async (item) => {
      if (confirm(`Êtes-vous sûr de vouloir supprimer le document "${item.nomDocumentIntervention}" ?`)) {
        try {
          console.log('Tentative de suppression du document:', item);
          // await api.deleteInterventionDocument(item.id);
          console.log('Document supprimé avec succès');
          
          // Rafraîchir la liste des documents après la suppression
          await fetchData();
          
          // Afficher un message de succès
          alert(`Le document "${item.nomDocumentIntervention}" a été supprimé avec succès.`);
        } catch (error) {
          console.error('Erreur détaillée lors de la suppression du document:', error);
          let errorMessage = 'Une erreur est survenue lors de la suppression du document.';
          
          if (error.response) {
            console.error('Réponse d\'erreur du serveur:', error.response);
            if (error.response.data && error.response.data.message) {
              errorMessage = error.response.data.message;
            } else {
              errorMessage = `Erreur ${error.response.status}: ${error.response.statusText}`;
            }
          } else if (error.request) {
            console.error('Pas de réponse reçue:', error.request);
            errorMessage = "Le serveur ne répond pas. Veuillez réessayer plus tard.";
          } else {
            console.error('Erreur de configuration de la requête:', error.message);
          }
          
          // Afficher l'erreur à l'utilisateur
          alert(errorMessage);
        }
      }
    };

    const cloturerIntervention = async () => {
      if (confirm('Êtes-vous sûr de vouloir clôturer cette intervention ?')) {
        try {
          await api.cloturerIntervention(intervention.value.id);
          fetchData(); // Recharger les données après la clôture
        } catch (error) {
          console.error('Erreur lors de la clôture de l\'intervention:', error);
        }
      }
    };

    const toggleDefaillanceDetails = () => {
      showDefaillanceDetails.value = !showDefaillanceDetails.value;
    };

    const toggleDocumentsDetails = () => {
      showDocumentsDetails.value = !showDocumentsDetails.value;
    };

    const ajouterDocument = () => {
      router.push({ name: 'AjouterDocumentIntervention', params: { id: intervention.value.id } });
    };


    onMounted(fetchData);

    return {
      intervention,
      formatLabelIntervention,
      formatLabelDefaillance,
      canSupprimer,
      canCloturer,
      retour,
      supprimerIntervention,
      reouvrirIntervention,
      cloturerIntervention,
      showDefaillanceDetails,
      showDocumentsDetails,
      toggleDefaillanceDetails,
      toggleDocumentsDetails,
      ouvrirDefaillance,
      headers,
      telechargerDocument,
      ajouterDocument,
      defaillanceId,
      supprimerDocument,
      actionMode,
      toggleActionMode
    };
  }
};
</script>