<template>
  <v-app>
    <NavigationDrawer 
      :logo="require('@/assets/images/LogoGIMAO.png')"
      :items="menuItems" 
      @item-selected="handleItemSelected"
    />
    <TopNavBar />

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
                        <v-row align="center" justify="start">
                          <v-col cols="auto">
                            <strong>Etat :</strong> {{ infosRecuperes.statutEquipement }}
                          </v-col>
                          <v-col cols="auto">
                            <svg width="11" height="11" viewBox="0 0 11 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                              <circle cx="5.5" cy="5.5" r="5.5" fill="#F0635D"/>
                            </svg>
                          </v-col>
                        </v-row>
                      </p>
                    </v-col>
                  </v-row>
                </v-col>

                <!-- Colonne de droite qui contient le champ commentaire -->
                <v-col cols="6">
                  <p><strong>Commentaire</strong></p>
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
                <!-- Lier formulaireValide avec v-model -->
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
                      <p class="mb-4"><strong>Technicien</strong></p>
                      <v-select
                        v-model="form.technicien"
                        label="Technicien"
                        :items="techniciens"
                        outlined
                        dense
                        :rules="[v => !!v || 'Technicien requis']"
                      ></v-select>
                    </v-col>

                    <v-col cols="6">
                      <p class="mb-4"><strong>Intervention curative</strong></p>
                      <v-select
                        v-model="form.interventionCurative"
                        label="Intervention Curative"
                        :items="interventionCurative"
                        outlined
                        dense
                        :rules="[v => !!v || 'Précision requise']"
                      ></v-select>
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
                      <p class="mb-4"><strong>Créateur bon de travail</strong></p>
                      <v-select
                        v-model="form.createurIntervention"
                        label="Créateur du bon de travail"
                        :items="createurInterventions"
                        outlined
                        dense
                        :rules="[v => !!v || 'Utilisateur requis']"
                      ></v-select>
                    </v-col>

                    <v-row justify="center">
                      <v-col cols="8">
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
            <v-btn color="error" class="text-white mx-2" @click="deleteInterventionRequest">
              Supprimer
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
import { useRouter } from 'vue-router';
import api from '@/services/api';

export default {
  name: 'CreerIntervention',
  
  setup() {
    const routeur = useRouter();
    
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
      interventionCurative: "",   
      tempsEstime: null,          
      createurIntervention: "",   
      commentaireARentrer: "",    
    });

    const techniciens = ["technicien1", "technicien2", "technicien3"];
    const createurInterventions = ["responsableGMAO", "respGMAO"];
    const interventionCurative = ["Oui", "Non"];

    const formulaireValide = ref(null);

    const fetchData = async () => {
      try {
        const interventionsRes = await api.getIntervention();
        if (interventionsRes && interventionsRes.data) {
          Object.assign(infosRecuperes, interventionsRes.data);
        } else {
          console.error('Aucune donnée reçue de l\'API');
        }
      } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
      }
    };

    const backPreviousPage = () => {
      routeur.push({ name: 'TableauDeBord' });
    };

    const deleteInterventionRequest = () => {
      routeur.push({ name: 'TableauDeBord' });
    };

    const validateForm = () => {
      if (formulaireValide.value) {
        alert("Formulaire validé avec succès !");
        backPreviousPage();
      } else {
        alert("Le formulaire n'est pas complet. Veuillez remplir les champs obligatoires.");
      }
    };

    onMounted(fetchData);

    return {
      form, 
      infosRecuperes,
      backPreviousPage,
      deleteInterventionRequest,
      validateForm,
      formulaireValide,
      techniciens,            
      createurInterventions,  
      interventionCurative  
    };
  },
};
</script>