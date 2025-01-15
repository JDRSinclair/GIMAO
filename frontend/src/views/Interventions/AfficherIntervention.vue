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
                      @click.stop="toggleDefaillanceDetails"
                      class="ml-2"
                    >
                      Détails
                    </v-btn> 
                    <v-icon class="ml-2">
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
              </v-row>
            </v-col>
          </v-row>

          <!-- Boutons -->
          <v-row justify="center" class="mt-4">
            <v-btn color="primary" class="text-white mx-2" @click="goBack">
              Retour
            </v-btn>
            
            <v-btn color="error" class="text-white mx-2" @click="supprimerIntervention" :disabled="!canSupprimer">
              Reouvrir l'intervention
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
import api from '@/services/api';

export default {
  name: 'AfficherIntervention',
  setup() {
    const router = useRouter();
    const route = useRoute();
    const intervention = ref(null);
    const showDefaillanceDetails = ref(false);

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
      return new Date(dateString).toLocaleString('fr-FR');
    };

    const getFullName = (user) => {
      return user ? `${user.first_name} ${user.last_name}` : 'Non spécifié';
    };

    const goBack = () => {
      router.go(-1);
    };

    const cloturerIntervention = () => {
      console.log("Clôturer l'intervention");
    };

    const supprimerIntervention = () => {
      console.log("Reouvrir l'intervention");
    };

    const toggleDefaillanceDetails = () => {
      showDefaillanceDetails.value = !showDefaillanceDetails.value;
    };

    const canCloturer = computed(() => {
      return intervention.value && !intervention.value.dateCloture;
    });

    const canSupprimer = computed(() => {
      return intervention.value && intervention.value.dateCloture;
    });

    const formatLabelIntervention = computed(() => {
      if (!intervention.value) return {};
      return {
        'Nom Intervention': intervention.value.nomIntervention,
        'Intervention Curative': intervention.value.interventionCurative ? 'Oui' : 'Non',
        'Date Assignation': formatDate(intervention.value.dateAssignation),
        'Date début Intervention': formatDate(intervention.value.dateDebutIntervention),
        'Date fin Intervention': formatDate(intervention.value.dateFinIntervention),
        'Temps estimé': intervention.value.tempsEstime,
        // 'Responsable': getFullName(intervention.value.responsable),
        'Créateur de l\'intervention': getFullName(intervention.value.createurIntervention)
      };
    });

    const formatLabelDefaillance = computed(() => {
      if (!intervention.value || !intervention.value.defaillance) return {};
      return {
        'Commentaire': intervention.value.defaillance.commentaireDefaillance,
        'Niveau de défaillance': intervention.value.defaillance.niveau,
        'Équipement concerné': intervention.value.defaillance.equipement
      };
    });

    onMounted(fetchData);

    return {
      intervention,
      formatDate,
      getFullName,
      goBack,
      cloturerIntervention,
      supprimerIntervention,
      canCloturer,
      canSupprimer,
      formatLabelIntervention,
      formatLabelDefaillance,
      showDefaillanceDetails,
      toggleDefaillanceDetails
    };
  },
};
</script>

<style scoped>
.expanded {
  background-color: #f5f5f5;
}
</style>