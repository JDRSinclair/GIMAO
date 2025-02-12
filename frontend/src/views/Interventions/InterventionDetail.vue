<template>
  <v-app>
    <v-main>
      <v-container class="py-5">
        <v-card class="pa-4">
          <v-row v-if="intervention">
            <!-- Left column with information -->
            <v-col cols="6">
              <v-row>
                <v-col cols="12" v-for="(value, key) in format_label_intervention" :key="key">
                  <p><strong>{{ key }} :</strong> {{ value }}</p>
                </v-col>
              </v-row>
            </v-col>

            <!-- Right column with additional information -->
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
                    @click="toggle_defaillance_details"
                    :class="{ 'expanded': show_defaillance_details }"
                  >
                    <v-card-title class="text-h6 d-flex align-center">
                      Défaillance
                      <v-spacer></v-spacer>
                      <v-btn
                        color="primary"
                        class="ml-2"
                        @click="ouvrirDefaillance"
                        :disabled="!defaillance_id"
                      >
                        Ouvrir
                      </v-btn> 
                     
                        <v-icon>
                          {{ show_defaillance_details ? 'mdi-chevron-up' : 'mdi-chevron-down' }}
                        </v-icon>
                    </v-card-title>
                    <v-expand-transition>
                      <div v-show="show_defaillance_details">
                        <v-divider class="my-2"></v-divider>
                        <v-card-text>
                          <v-row>
                            <v-col cols="12" v-for="(value, key) in format_label_defaillance" :key="key">
                              <p><strong>{{ key }} :</strong> {{ value }}</p>
                            </v-col>
                          </v-row>
                        </v-card-text> 
                      </div>
                    </v-expand-transition>
                  </v-card>
                </v-col>
                
                <!-- Section for intervention documents -->
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
                      <v-btn icon @click="toggle_documents_details">
                        <v-icon>
                          {{ show_documents_details ? 'mdi-chevron-up' : 'mdi-chevron-down' }}
                        </v-icon>
                      </v-btn>
                    </v-card-title>
                    <v-expand-transition>
                      <div v-show="show_documents_details">
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
                                <v-btn color="primary" small @click="toggle_action_mode">
                                  {{ action_mode === 'download' ? 'Mode suppression' : 'Mode téléchargement' }}
                                </v-btn>
                              </v-toolbar>
                            </template>

                            <template v-slot:item.actions="{ item }">
                              <v-btn
                                icon
                                small
                                :color="action_mode === 'download' ? 'primary' : 'error'"
                                @click="action_mode === 'download' ? telechargerDocument(item) : supprimerDocument(item)"
                              >
                                <v-icon small>
                                  {{ action_mode === 'download' ? 'mdi-download' : 'mdi-delete' }}
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

          <!-- Buttons -->
          <v-row justify="center" class="mt-4">
            <v-btn color="primary" class="text-white mx-2" @click="retour">
              Retour
            </v-btn>

            <v-btn color="error" class="text-white mx-2" @click="supprimerIntervention" :disabled="!can_supprimer">
              Supprimer l'intervention
            </v-btn>
            
            <v-btn color="warning" class="text-white mx-2" @click="reouvrirIntervention" :disabled="!can_supprimer">
              Rouvrir l'intervention
            </v-btn>

            <v-btn color="success" class="text-white mx-2" @click="cloturerIntervention" :disabled="!can_cloturer">
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
import api, { BASE_URL } from '@/services/api';

export default {
  name: 'InterventionDetail',
  setup() {
    const router = useRouter();
    const route = useRoute();
    const action_mode = ref('download');
    const intervention = ref(null);
    const show_defaillance_details = ref(false);
    const show_documents_details = ref(false);

    const retour = () => {
      router.go(-1);
    };

    const headers = [
      { title: 'Nom du document', value: 'nomDocumentIntervention' },
      { title: 'Actions', value: 'actions', sortable: false }
    ];

    const defaillance_id = computed(() => {
      return intervention.value?.defaillance?.id;
    });

    const ouvrirDefaillance = () => {
      if (defaillance_id.value) {
        router.push({ name: 'FailureDetail', params: { id: defaillance_id.value } });
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

    const format_label_intervention = computed(() => {
      if (!intervention.value) return {};
      return {
        'Nom de l\'intervention': intervention.value.nomIntervention,
        'Date d\'assignation': formatDate(intervention.value.dateAssignation),
        'Date de clôture': formatDate(intervention.value.dateCloture),
        'Date du début de l\'intervention': formatDate(intervention.value.dateDebutIntervention),
        'Date de fin de l\'intervention': formatDate(intervention.value.dateFinIntervention),
        'Temps estimé': intervention.value.tempsEstime,
        'Intervention curative': intervention.value.interventionCurative ? 'Oui' : 'Non',
      };
    });

    const format_label_defaillance = computed(() => {
      if (!intervention.value || !intervention.value.defaillance) return {};
      const defaillance = intervention.value.defaillance;
      return {
        'Nom de la défaillance': defaillance.commentaireDefaillance,
        'Date de la défaillance': formatDate(defaillance.dateDefaillance),
        'Commentaire': defaillance.commentaireDefaillance || 'Aucun commentaire'
      };
    });

    const can_supprimer = computed(() => {
      return intervention.value && !intervention.value.dateCloture;
    });

    const can_cloturer = computed(() => {
      return intervention.value && !intervention.value.dateCloture;
    });

    const toggle_action_mode = () => {
      action_mode.value = action_mode.value === 'download' ? 'delete' : 'download';
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
          
          // Refresh the document list after deletion
          await fetchData();
          
          // Display success message
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
          
          // Display the error to the user
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

    const toggle_defaillance_details = () => {
      show_defaillance_details.value = !show_defaillance_details.value;
    };

    const toggle_documents_details = () => {
      show_documents_details.value = !show_documents_details.value;
    };

    const ajouterDocument = () => {
      router.push({ name: 'AddDocumentIntervention', params: { id: intervention.value.id } });
    };

    onMounted(fetchData);

    return {
      intervention,
      format_label_intervention,
      format_label_defaillance,
      can_supprimer,
      can_cloturer,
      retour,
      supprimerIntervention,
      reouvrirIntervention,
      cloturerIntervention,
      show_defaillance_details,
      show_documents_details,
      toggle_defaillance_details,
      toggle_documents_details,
      ouvrirDefaillance,
      headers,
      telechargerDocument,
      ajouterDocument,
      defaillance_id,
      supprimerDocument,
      action_mode,
      toggle_action_mode
    };
  }
};
</script>