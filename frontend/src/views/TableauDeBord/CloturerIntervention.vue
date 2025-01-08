<template>
  <v-app>
    <v-main>
      <v-container class="py-5">
        <v-card class="pa-4">
          <h1 class="text-primary text-center">Clôturer le bon de travail</h1>

          <v-row>
            <!-- Colonne de gauche avec les informations -->
            <v-col cols="6">
              <v-row>
                <!-- Champ NomIntervention  -->
                <v-col cols="12">
                  <p><strong>Nom Intervention :</strong> {{ form.nomIntervention }}</p>
                </v-col>
                <!-- Switch Champ interventionCurative  -->
                <v-col cols="12">
                  <p><strong>Intervention Curative :</strong></p>
                  <v-switch
                    :value="form.interventionCurative === 'OUI'"
                    activated
                  ></v-switch>
                   <!-- Champ DateAssignation  -->
                </v-col>
                <v-col cols="12">
                  <p><strong>Date Assignation :</strong> {{ form.dateAssignation }}</p>
                </v-col>
                <!-- Champ DateCloture  -->
                <v-col cols="12">
                  <p><strong>Date clôture :</strong> {{ form.dateCloture }}</p>
                </v-col>
                <!-- Champ DebutIntervention  -->
                <v-col cols="12">
                  <p><strong>Date début Intervention :</strong> {{ form.dateDebutIntervention }}</p>
                </v-col>
                <!-- Champ FinIntervention  -->
                <v-col cols="12">
                  <p><strong>Date fin Intervention :</strong> {{ form.dateFinIntervention }}</p>
                </v-col>
                <!-- Champ TempsEstime  -->
                <v-col cols="12">
                  <p><strong>Temps Estimé :</strong> {{ form.tempsEstime }}</p>
                </v-col>
              </v-row>
            </v-col>

            <!-- Colonne de droite avec le champ commentaire -->
            <v-col cols="6">
              <p><strong>Commentaire :</strong></p>
              <p>{{ form.commentaire }}</p>
            </v-col>
          </v-row>

          <!-- Boutons en bas -->
          <v-row justify="center" class="mt-4">
            <v-btn color="primary" class="text-white mx-2" @click="annulerFormulaire">
              Annuler
            </v-btn>
            <v-btn color="success" class="text-white mx-2" @click="validerFormulaire">
              Valider
            </v-btn>
          </v-row>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'CloturerIntervention',
  data() {
    return {
      form: {
        nomIntervention: "Lieu 1",
        interventionCurative: "OUI",
        dateAssignation: "01/01/2025", 
        dateCloture: "08/01/2025", 
        dateDebutIntervention: "2024-01-01", 
        dateFinIntervention: "2024-01-01",
        tempsEstime: "2h00",
        commentaire: "Ceci est un commentaire.",
      },
    };
  },

  methods: {
    
    annulerFormulaire() {
      this.$router.push({ name: 'TableauDeBord' });
    },
    
    validerFormulaire() {
      this.$router.push({ name: 'TableauDeBord' });
    },
  },
};
</script>

