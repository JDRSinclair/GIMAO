<template>
  <v-app>
    <v-main>
      <v-container class="py-5">
        <v-card class="pa-4">
          <v-row v-if="defaillance">
            <!-- Colonne de gauche avec les informations -->
            <v-col cols="6" class="column-offset">
              <v-row>
                <v-col cols="12" v-for="(value, key) in formatLabelDefaillance" :key="key">
                  <p>
                    <strong>{{ key }} : </strong>
                    <v-chip v-if="key === 'Niveau'" :color="getNiveauColor(value)" small>
                      {{ value }}
                    </v-chip>
                    <v-chip v-else-if="key === 'Traitée'" :color="getTypeColor(value)" small>
                      {{ value }}
                    </v-chip>
                    <span v-else>{{ value }}</span>
                  </p>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12">
                  <v-select
                    v-model="selectedStatut"
                    :items="statutOptions"
                    label="Changer le statut de l'équipement"
                  ></v-select>
                </v-col>
              </v-row>
                
              
            </v-col>

            <!-- Colonne de droite avec les informations supplémentaires -->
            <v-col cols="6">
              <v-row>
                <!-- Section pour l'équipement associé -->
                <v-col cols="12">
                  <v-card
                    class="mt-4 pa-4"
                    elevation="2"
                    @click="toggleEquipementDetails"
                    :class="{ 'expanded': showEquipementDetails }"
                  >
                    <v-card-title class="text-h6 d-flex align-center">
                      Équipement
                      <v-spacer></v-spacer>
                      <v-btn
                        color="primary"
                        class="ml-2"
                        @click.stop="ouvrirEquipement"
                        :disabled="!defaillance.equipement"
                      >
                        Détaile
                      </v-btn>
                      <v-icon class="ml-2">
                        {{ showEquipementDetails ? 'mdi-chevron-up' : 'mdi-chevron-down' }}
                      </v-icon>
                    </v-card-title>
                    <v-expand-transition>
                      <div v-show="showEquipementDetails">
                        <v-divider class="my-2"></v-divider>
                        <v-card-text>
                          <v-row>
                            <v-col cols="12" v-for="(value, key) in formatLabelEquipement" :key="key">
                              <p><strong>{{ key }} :</strong> {{ value }}</p>
                            </v-col>
                          </v-row>
                        </v-card-text>
                      </div>
                    </v-expand-transition>
                  </v-card>
                </v-col>

                <!-- Section pour les Documents de défaillance -->
                <v-col cols="12">
                  <v-card
                    class="mt-4 pa-4"
                    elevation="2"
                  >
                    <v-card-title class="text-h6 d-flex align-center">
                      Documents de la défaillance
                      <v-spacer></v-spacer>
                      <v-btn
                        color="primary"
                        small
                        class="mr-2"
                        @click.stop="ajouterDocument"
                      >
                        Ajouter
                      </v-btn>
                      <v-btn
                        @click.stop="toggleDocumentsDetails"
                      >
                        <v-icon class="ml-2">
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
                            :items="defaillance.liste_documents_defaillance || []"
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

            <v-btn color="error" class="text-white mx-2" @click="supprimerDefaillance" :disabled="!canSupprimer">
              Supprimer la défaillance
            </v-btn>

            <v-btn color="success" class="text-white mx-2" @click="traiterDefaillance" :disabled="!canTraiter">
              Traiter la défaillance
            </v-btn>

            <v-btn color="success" class="text-white mx-2" @click="creerIntervention" :disabled="canTraiter">
              Creer un bon de travail
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
  name: 'AfficherDefaillance',
  setup() {
    const router = useRouter();
    const route = useRoute();
    const defaillance = ref(null);
    const showEquipementDetails = ref(false);
    const showDocumentsDetails = ref(false);
    const actionMode = ref('download');
    const selectedStatut = ref("pas de changement");

    const retour = () => {
      router.go(-1);
    };

    const headers = [
      { title: 'Nom du document', value: 'nomDocumentDefaillance' },
      { title: 'Actions', value: 'actions', sortable: false }
    ];

    const toggleActionMode = () => {
      actionMode.value = actionMode.value === 'download' ? 'delete' : 'download';
    };

    const supprimerDocument = async (item) => {
    if (confirm(`Êtes-vous sûr de vouloir supprimer le document "${item.nomDocumentDefaillance}" ?`)) {
      try {
        console.log('Tentative de suppression du document:', item);
        await api.deleteDefaillanceDocument(item.id);
        console.log('Document supprimé avec succès');
        
        // Rafraîchir la liste des documents après la suppression
        await fetchData();
        
        // Afficher un message de succès
        alert(`Le document "${item.nomDocumentDefaillance}" a été supprimé avec succès.`);
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

  const fetchData = async () => {
    try {
      const response = await api.getDefaillanceAffichage(route.params.id);
      const defaillanceData = response.data;

      if (defaillanceData.equipement && typeof defaillanceData.equipement === 'object') {
        defaillanceData.equipement.dernier_statut = defaillanceData.equipement.dernier_statut || {};
      } else if (typeof defaillanceData.equipement === 'string') {
        const equipementResponse = await api.getEquipementAffichage(defaillanceData.equipement);
        defaillanceData.equipement = equipementResponse.data;
        defaillanceData.equipement.dernier_statut = defaillanceData.equipement.dernier_statut || {};
      } else {
        console.error('Les données de l\'équipement sont manquantes ou invalides');
        defaillanceData.equipement = { dernier_statut: {} };
      }

      // Mettre à jour defaillance.value avec les données complètes
      defaillance.value = defaillanceData;

      console.log('Données récupérées avec succès:', defaillance.value);
    } catch (error) {
      console.error('Erreur lors de la récupération des données:', error);
    }
  };

    const getNiveauColor = (niveau) => {
      switch (niveau) {
        case 'Critique':
          return 'red';
        case 'Majeur':
          return 'orange';
        default:
          return 'green';
      }
    };

    const getTypeColor = (couleur) => {
      switch (couleur) {
        case 'Oui':
          return 'green';
        default:
          return'red';
      }};


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

    const formatLabelDefaillance = computed(() => {
      if (!defaillance.value) return {};
      const label = {
        'Description': defaillance.value.commentaireDefaillance,
        'Niveau': defaillance.value.niveau,
        'Traitée': defaillance.value.dateTraitementDefaillance ? 'Oui' : 'Non',
        // 'Utilisateur': defaillance.value.utilisateur?.username || 'Non spécifié',
      };
          
      if (defaillance.value.dateTraitementDefaillance) {
        label['Date de traitement'] = formatDate(defaillance.value.dateTraitementDefaillance);
      }

      if (defaillance.value.intervention) {
        label['Intervention créée le '] = formatDate(defaillance.value.intervention.dateAssignation);
      }

      return label;
    });

    const formatLabelEquipement = computed(() => {
      if (!defaillance.value || !defaillance.value.equipement) return {};
      const equipement = defaillance.value.equipement;
      return {
        'Référence': equipement.reference || 'Non spécifié',
        'Désignation': equipement.designation || 'Non spécifié',
        'Statut': equipement.dernier_statut?.statutEquipement || 'Non spécifié',
        'Date de mise en service': equipement.dateMiseEnService ? formatDate(equipement.dateMiseEnService) : 'Non spécifié',
        'Prix d\'achat': equipement.prixAchat ? `${equipement.prixAchat} €` : 'Non spécifié',
        'Préventif glissant': equipement.preventifGlissant !== undefined ? (equipement.preventifGlissant ? 'Oui' : 'Non') : 'Non spécifié',
        'Intervalle de maintenance': equipement.joursIntervalleMaintenance ? `${equipement.joursIntervalleMaintenance} jours` : 'Non spécifié',
      };
    });
    
    const canSupprimer = computed(() => {
      return defaillance.value && !defaillance.value.intervention;
    });

    const canTraiter = computed(() => {
      return defaillance.value && !defaillance.value.dateTraitementDefaillance;
    });


    const supprimerDefaillance = async () => {
      if (!canSupprimer.value) {
        alert("Impossible de supprimer cette défaillance car une intervention est déjà associée.");
        return;
      }

      if (confirm('Êtes-vous sûr de vouloir supprimer cette défaillance et tous ses documents associés ?')) {
        try {
          // Supprimer d'abord tous les documents associés
          if (defaillance.value.documents && defaillance.value.documents.length > 0) {
            for (const document of defaillance.value.documents) {
              await api.deleteDefaillanceDocument(document.id);
              console.log(`Document ${document.nomDocumentDefaillance} supprimé.`);
            }
          }

          // Ensuite, supprimer la défaillance
          await api.deleteDefaillance(defaillance.value.id);
          console.log('Défaillance supprimée avec succès.');
          
          // Redirection vers la page des signalements
          router.push({ 
            name: 'AfficherEquipement', 
            params: { reference: defaillance.value.equipement.reference }
          });
        } catch (error) {
          console.error('Erreur lors de la suppression de la défaillance ou de ses documents:', error);
        }
      }
    };

    const traiterDefaillance = async () => {
      if (confirm('Êtes-vous sûr de vouloir traiter cette défaillance ?')) {
        try {
          const dateTraitementDefaillance = new Date().toISOString();
          const response = await api.patchDefaillance(defaillance.value.id, {
            dateTraitementDefaillance: dateTraitementDefaillance
          });
          
          defaillance.value = { 
            ...defaillance.value, 
            ...response.data,
            equipement: defaillance.value.equipement 
          };

          if (selectedStatut.value !== "pas de changement" || selectedStatut.value == defaillance.value.equipement?.dernier_statut.statutEquipement ) {
            const statutData = {
              statutEquipement: selectedStatut.value,
              dateChangement: new Date().toISOString(),
              equipement: defaillance.value.equipement?.reference,
              informationStatutParent: defaillance.value.equipement.dernier_statut.id,
              ModificateurStatut: 1
            };

            await api.postInformationStatut(statutData);
          }

          await fetchData();
          
        } catch (error) {
          console.error('Erreur lors du traitement de la défaillance:', error);
        }
      }
    };

    const creerIntervention = () => {
      if (defaillance.value && defaillance.value.id) {
        router.push({ 
          name: 'CreerIntervention', 
          params: { id: defaillance.value.id }
        });
      } else {
        console.error("ID de défaillance manquant");
        alert("Impossible de créer une intervention. Données de défaillance manquantes.");
      }
    };

    const toggleEquipementDetails = () => {
      showEquipementDetails.value = !showEquipementDetails.value;
    };

    const toggleDocumentsDetails = () => {
      showDocumentsDetails.value = !showDocumentsDetails.value;
    };

    const ajouterDocument = () => {
      router.push({ 
        name: 'AjouterDocumentDefaillance', 
        params: { id: defaillance.value.id }
      });
    };

    const ouvrirEquipement = () => {
      if (defaillance.value && defaillance.value.equipement) {
        router.push({ 
          name: 'AfficherEquipement', 
          params: { reference: defaillance.value.equipement.reference }
        });
      }
    };

    const telechargerDocument = (item) => {
      const cleanedLink = item.lienDocumentDefaillance.startsWith('/media/') 
        ? item.lienDocumentDefaillance 
        : `/media/${item.lienDocumentDefaillance.split('/media/').pop()}`;
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
          a.download = item.nomDocumentDefaillance;
          document.body.appendChild(a);
          a.click();
          window.URL.revokeObjectURL(url);
        })
        .catch(error => {
          console.error('Erreur lors du téléchargement:', error);
          alert('Erreur lors du téléchargement du fichier. Veuillez réessayer.');
        });
    };

  
  
  const statutOptions = [
    "pas de changement",
    "En fonctionnement",
    "Dégradé",
    "A l'arrêt"
  ];

    onMounted(fetchData);

    return {
      defaillance,
      formatLabelDefaillance,
      formatLabelEquipement,
      canSupprimer,
      canTraiter,
      supprimerDefaillance,
      traiterDefaillance,
      creerIntervention,
      showEquipementDetails,
      showDocumentsDetails,
      toggleEquipementDetails,
      toggleDocumentsDetails,
      ouvrirEquipement,
      headers,
      telechargerDocument,
      ajouterDocument,
      actionMode,
      toggleActionMode,
      supprimerDocument,
      getNiveauColor,
      getTypeColor,
      retour,
      selectedStatut,
      statutOptions,
    };
  }
};
</script>

<style scoped>
.expanded {
  background-color: #f5f5f5;
}

.column-offset {
  margin-top: 20px; 
}
</style>