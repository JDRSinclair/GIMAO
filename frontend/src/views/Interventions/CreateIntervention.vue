<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-card elevation="1" class="rounded-lg pa-2"> 
              <h1 class="text-primary text-center mb-4">Demande d'intervention</h1>
              <v-row>
                <v-col cols="6">
                  <v-row>
                    <v-col cols="12">
                      <p class="mb-4"><strong>Equipement:</strong> {{ infosRecuperes.designation }}</p>
                    </v-col>
                    <v-col cols="12">
                      <p class="mb-4"><strong>Salle:</strong> {{ infosRecuperes.nomLieu }}</p>
                    </v-col>
                    <v-col cols="12">
                      <p class="mb-4">
                        <v-row justify="start">
                          <v-col cols="auto">
                            <strong>Etat de la machine :</strong>
                            <v-chip :color="getNiveauColor(infosRecuperes.statutEquipement)" dark>
                              {{ infosRecuperes.statutEquipement }}
                            </v-chip>
                          </v-col>
                        </v-row>
                      </p>
                    </v-col>
                  </v-row>
                </v-col>

                <!-- Colonne de droite qui contient le champ commentaire -->
                <v-col cols="6">
                  <p><strong>Informations sur la defaillance</strong></p>
                  <p>{{ infosRecuperes.commentaireDefaillance }}</p>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>

        <v-container>
          <v-row>
            <v-col cols="12">
              <v-card elevation="1" class="rounded-lg pa-2">
                <h2 class="text-primary text-center mb-4">Informations du bon de travail</h2>
                <v-form ref="formulaire" v-model="formulaireValide" @submit.prevent="validateForm">
                  <v-row>
                    <v-col cols="6">
                      <p class="mb-4"><strong>Nom du bon de travail</strong></p>
                      <v-text-field
                        v-model="form.nomIntervention"
                        label="Nom du bon de travail"
                        type="text"
                        outlined
                        dense
                        :rules="[v => !!v || 'Nom du bon de travail requis']"
                      ></v-text-field>
                    </v-col>

                    <v-col cols="6">
                      <p class="mb-4"><strong>Date de début d'intervention</strong></p>
                      <v-text-field
                        v-model="form.dateDebut"
                        type="datetime-local"
                        outlined
                        dense
                        :rules="[v => !!v || 'Date de début requise']"
                      ></v-text-field>
                    </v-col>

                    <v-col cols="6">
                      <p class="mb-4"><strong>Intervention curative</strong></p>
                      <v-switch
                        v-model="form.interventionCurative"
                        label="Intervention Curative"
                        color="primary"
                        hide-details
                        inset
                      ></v-switch>
                      <!-- <p class="mb-4"><strong>Technicien</strong></p>
                      <v-select
                        v-model="form.technicien"
                        label="Technicien"
                        :items="techniciens"
                        outlined
                        dense
                        :rules="[v => !!v || 'Technicien requis']"
                      ></v-select> -->
                    </v-col>

                    <v-col cols="6">
                      <p class="mb-4"><strong>Temps estimé (en heures)</strong></p>
                      <v-text-field
                        v-model="form.tempsEstime"
                        label="Temps estimé (facultatif)"
                        type="number"
                        outlined
                        dense
                        min="0"
                        step="1"
                      ></v-text-field>
                    </v-col>

                    <v-col cols="6">
                      
                    </v-col>
                    <v-col cols="6"></v-col>

                    <v-row justify="center">
                      <v-col cols="10">
                        <v-row justify="center">
                          <p class="mb-4"><strong>Commentaire</strong></p> 
                        </v-row> 
                        <v-textarea
                          v-model="form.commentaireARentrer"
                          rows="10"
                          outlined
                          :rules="[v => !!v || 'Commentaire requis']"
                        ></v-textarea>
                      </v-col>
                    </v-row>
                  </v-row>
                </v-form>
              </v-card>
            </v-col>
          </v-row>

          <v-row justify="center" class="mt-4">
            <v-btn color="primary" class="text-white mx-2" @click="backPreviousPage">
              Annuler
            </v-btn>
            <v-btn color="success" class="text-white mx-2" @click="validateForm">
              Valider
            </v-btn>
          </v-row>
        </v-container>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import '@/assets/css/global.css'; 
import { reactive, onMounted, ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import api from '@/services/api';

export default {
  name: 'CreateIntervention',
  
  setup() {
    const routeur = useRouter();
    const route = useRoute();

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
    
    const infosRecuperes = reactive({
      designation: "",
      nomLieu: "",
      commentaireDefaillance: "",
      statutEquipement: "",
    });

    const form = reactive({
      nomIntervention: "",        
      dateDebut: "",              
      technicien: "",             
      interventionCurative: false,   
      tempsEstime: null,          
      createurIntervention: 1,   
      commentaireARentrer: "",    
    });

    const techniciens = ref([]);
    const interventionCurative = [
      { text: 'Oui', value: true },
      { text: 'Non', value: false }
    ];

    const formulaireValide = ref(false);

    const fetchData = async () => {
      try {
        const defaillanceId = route.params.id;
        if (!defaillanceId) {
          throw new Error('ID de défaillance manquant');
        }

        const [defaillanceRes, utilisateursRes] = await Promise.all([
          api.getDefaillanceAffichage(defaillanceId),
          api.getUtilisateur()
        ]);

        if (defaillanceRes && defaillanceRes.data) {
          Object.assign(infosRecuperes, {
            designation: defaillanceRes.data.equipement.designation,
            nomLieu: defaillanceRes.data.equipement.lieu.nomLieu,
            commentaireDefaillance: defaillanceRes.data.commentaireDefaillance,
            statutEquipement: defaillanceRes.data.equipement.dernier_statut.statutEquipement
          });
        } else {
          console.error('Aucune donnée de défaillance reçue de l\'API');
        }

        if (utilisateursRes && utilisateursRes.data) {
          techniciens.value = utilisateursRes.data
            .filter(user => user.role === 'Technicien')
            .map(tech => ({
              text: `${tech.prenom} ${tech.nom}`,
              value: tech.id
            }));
        } else {
          console.error('Aucune donnée d\'utilisateurs reçue de l\'API');
        }
      } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
        alert('Erreur lors de la récupération des données. Veuillez réessayer.');
      }
    };

    const backPreviousPage = () => {
      routeur.go(-1);
    };

    const deleteInterventionRequest = () => {
      routeur.push({ name: 'Dashboard' });
    };

    const validateForm = async () => {
      if (formulaireValide.value) {
        try {
          const interventionData = {
            nomIntervention: form.nomIntervention,
            interventionCurative: form.interventionCurative,
            dateAssignation: new Date().toISOString(),
            dateCloture: null,
            dateDebutIntervention: form.dateDebut,
            dateFinIntervention: null,
            tempsEstime: form.tempsEstime ? `${form.tempsEstime.toString().padStart(2, '0')}:00:00` : null,
            commentaireIntervention: form.commentaireARentrer,
            commentaireRefusCloture: null,
            defaillance: parseInt(route.params.id),
            createurIntervention: 1,
            responsable: 1
          };

          const response = await api.postIntervention(interventionData);
          
          if (response && response.data) {
            alert("Intervention créée avec succès !");
            // Redirection vers la page d'affichage de l'intervention
            routeur.push({ name: 'InterventionDetail', params: { id: response.data.id } });
          } else {
            throw new Error('Réponse invalide du serveur');
          }
        } catch (error) {
          console.error('Erreur lors de la création de l\'intervention:', error);
          alert("Erreur lors de la création de l'intervention. Veuillez réessayer.");
        }
      } else {
        alert("Le formulaire n'est pas complet. Veuillez remplir les champs obligatoires.");
      }
    };
    onMounted(fetchData);

    return {
      form,
      infosRecuperes,
      techniciens,
      interventionCurative,
      formulaireValide,
      backPreviousPage,
      deleteInterventionRequest,
      validateForm,
      getNiveauColor,
      menuItems: [
        { title: 'Tableau de bord', icon: 'mdi-view-dashboard', route: '/tableau-de-bord' },
        { title: 'Interventions', icon: 'mdi-wrench', route: '/interventions' },
        { title: 'Equipements', icon: 'mdi-laptop', route: '/equipements' },
        { title: 'Gestion des données', icon: 'mdi-database', route: '/gestion-donnees' },
        { title: 'Commandes', icon: 'mdi-cart', route: '/Orders' },
      ],
      handleItemSelected(route) {
        routeur.push(route);
      },
    };
  },
};
</script>

<style scoped>
/* Ajoutez ici vos styles spécifiques si nécessaire */
</style>