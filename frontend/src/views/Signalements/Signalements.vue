<template>
  <v-app>
    <v-main>
      <v-container class="py-5">
        <v-card class="pa-4">
          <h1 class="text-primary text-center">Signaler une défaillance</h1>

          <v-row>
            <!-- Colonne de gauche avec les champs -->
            <v-col cols="6">
              <v-form ref="formulaire" v-model="formulaireValide">
                <v-row>
                  <v-col cols="12">
                    <v-select
                      v-model="form.lieu"
                      label="Lieu"
                      :items="lieux"
                      outlined
                      dense
                      :rules="[v => !!v || (validationTriggered && 'Lieu requis')]"
                    ></v-select>
                  </v-col>
                  <v-col cols="12">
                    <v-select
                      v-model="form.salle"
                      label="Salle"
                      :items="salles"
                      outlined
                      dense
                      :rules="[v => !!v || (validationTriggered && 'Salle requise')]"
                    ></v-select>
                  </v-col>
                  <v-col cols="12">
                    <v-select
                      v-model="form.equipement"
                      label="Équipement"
                      :items="equipements"
                      outlined
                      dense
                      :rules="[v => !!v || (validationTriggered && 'Équipement requis')]"
                    ></v-select>
                  </v-col>
                                <!-- Groupe de boutons radio pour l'état -->
              <v-radio-group
                v-model="form.etat"
                class="mt-4"
                row
                :rules="[v => !!v || (validationTriggered && 'État requis')]"
              >
                <v-radio
                  label="Fonctionnel"
                  value="Fonctionnel"
                  color="black"
                ></v-radio>
                <v-radio
                  label="À l'arrêt"
                  value="À l'arrêt"
                  color="black"
                ></v-radio>
                <v-radio
                  label="Rebuté"
                  value="Rebuté"
                  color="black"
                ></v-radio>
              </v-radio-group>
                </v-row>
              </v-form>
            </v-col>

            <!-- Colonne de droite : Champ commentaire + Boutons radio -->
            <v-col cols="6">
              <v-textarea
                v-model="form.commentaire"
                label="Commentaires"
                rows="10"
                outlined
              ></v-textarea>


            </v-col>
          </v-row>

          <!-- Boutons en bas -->
          <v-row justify="center" class="mt-4">
            <v-btn
              color="primary"
              class="text-white mx-2"
              @click="reinitialiserFormulaire"
            >
              Annuler
            </v-btn>
            <v-btn
              color="success"
              class="text-white mx-2"
              @click="validerFormulaire"
            >
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
  data() {
    return {
      lieux: ["Lieu 1", "Lieu 2", "Lieu 3"],
      salles: ["Salle 1", "Salle 2", "Salle 3"],
      equipements: ["Equipement 1", "Equipement 2", "Equipement 3"],
      form: {
        lieu: null,
        salle: null,
        equipement: null,
        commentaire: "",
        etat: null, // Propriété pour stocker l'état sélectionné
      },
      formulaireValide: false,
      validationTriggered: false,
    };
  },

  methods: {
    reinitialiserFormulaire() {
      this.form = {
        lieu: null,
        salle: null,
        equipement: null,
        commentaire: "",
        etat: null, // Réinitialiser aussi l'état
      };
      this.validationTriggered = false;
      if (this.$refs.formulaire) {
        this.$refs.formulaire.resetValidation();
      }
    },

    validerFormulaire() {
      this.validationTriggered = true;
      const formulaire = this.$refs.formulaire;

      if (formulaire) {
        formulaire.validate();
        if (this.formulaireValide) {
          alert("Formulaire validé !");
          console.log("Formulaire soumis :", this.form);

          this.reinitialiserFormulaire();
        } else {
          alert("Veuillez remplir tous les champs obligatoires.");
        }
      }
    },
  },
};
</script>
