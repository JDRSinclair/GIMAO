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
                      :rules="[v => !!v || (validationDeclenchee && 'Lieu requis')]"
                    ></v-select>
                  </v-col>
                  <v-col cols="12">
                    <v-select
                      v-model="form.salle"
                      label="Salle"
                      :items="salles"
                      outlined
                      dense
                      :rules="[v => !!v || (validationDeclenchee && 'Salle requise')]"
                    ></v-select>
                  </v-col>
                  <v-col cols="12">
                    <v-select
                      v-model="form.equipement"
                      label="Équipement"
                      :items="equipements"
                      outlined
                      dense
                      :rules="[v => !!v || (validationDeclenchee && 'Équipement requis')]"
                    ></v-select>
                  </v-col>
              <!-- Groupe de boutons radio pour l'état -->
              <v-radio-group
                v-model="form.etat"
                class="mt-4"
                row
                :rules="[v => !!v || (validationDeclenchee && 'État requis')]"
              >
                <v-radio
                  label="Fonctionnel"
                  value="Fonctionnel"
                  color="primary"
                ></v-radio>
                <v-radio
                  label="À l'arrêt"
                  value="À l'arrêt"
                  color="primary"
                ></v-radio>
                <v-radio
                  label="Rebuté"
                  value="Rebuté"
                  color="primary"
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

          <!-- Boutons du bas -->
          <v-row justify="center" class="mt-4">
            <v-btn
              color="primary"
              class="text-white mx-2"
              @click="resetForm"
            >
              Effacer
            </v-btn>
            <v-btn
              color="success"
              class="text-white mx-2"
              @click="validateForm"
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
import '@/assets/css/global.css';

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
        etat: null,
      },
      formulaireValide: false,
      validationDeclenchee: false,
    };
  },

  methods: {
    /**
     * Réinitialise le formulaire en effaçant les valeurs des champs, 
     * en remettant la validation à zéro et en annulant la validation.
     */
    resetForm() {
      this.form = {
        lieu: null,
        salle: null,
        equipement: null,
        commentaire: "",
        etat: null,
      };
      this.validationDeclenchee = false;
      if (this.$refs.formulaire) {
        this.$refs.formulaire.resetValidation();
      }
    },

    /**
     * Valide le formulaire et le soumet si tous les champs sont valides.
     * Si le formulaire est valide, affiche un message de confirmation et
     * envoie le formulaire par console. Sinon, affiche un message d'erreur.
     */
    validateForm() {
      this.validationDeclenchee = true;
      const formulaire = this.$refs.formulaire;

      if (formulaire) {
        formulaire.validate();
        if (this.formulaireValide) {
          alert("Formulaire validé !");
          console.log("Formulaire soumis :", this.form);

          this.resetForm();
        } else {
          alert("Veuillez remplir tous les champs obligatoires.");
        }
      }
    },
  },
};
</script>
