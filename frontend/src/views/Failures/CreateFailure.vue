<template>
  <v-app>
    <v-main>
      <v-container class="py-5">
        <v-card class="pa-4">
          <v-form ref="formulaire" v-model="formulaireValide">
            <v-row>
              <v-col cols="6">
                <!-- <v-select
                  v-model="form.equipement"
                  label="Équipement"
                  :items="equipements"
                  item-text="label"
                  item-value="reference"
                  outlined
                  dense
                  :rules="[v => !!v || (validationDeclenchee && 'Équipement requis')]"
                  :disabled="!!equipementReference"
                ></v-select> -->
                <v-select
                  v-model="form.niveau"
                  label="Niveau"
                  :items="niveaux"
                  outlined
                  dense
                  :rules="[v => !!v || (validationDeclenchee && 'Niveau requis')]"
                ></v-select>
              </v-col>
              <v-col cols="6">
                <v-textarea
                  v-model="form.commentaireDefaillance"
                  label="Commentaires"
                  rows="5"
                  outlined
                  :rules="[v => !!v || (validationDeclenchee && 'Commentaire requis')]"
                ></v-textarea>
              </v-col>
            </v-row>
            <v-row justify="center" class="mt-4">
              <v-btn color="primary" class="text-white mx-2" @click="retour">
                Retour
              </v-btn>
              <v-btn color="primary" class="text-white mx-2" @click="resetForm">
                Effacer
              </v-btn>
              <v-btn color="success" class="text-white mx-2" @click="validateForm">
                Valider
              </v-btn>
            </v-row>
          </v-form>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { useRouter } from 'vue-router';
import '@/assets/css/global.css';
import api from '@/services/api';

export default {
  setup() {
    const router = useRouter();
    return { router };
  },
  data() {
    return {
      equipements: [],
      niveaux: ['Mineur', 'Majeur', 'Critique'],
      form: {
        equipement: null,
        commentaireDefaillance: "",
        niveau: null,
      },
      formulaireValide: false,
      validationDeclenchee: false,
      equipementReference: null,
      utilisateurConnecte: {
        id: 1,
        username: "admin",
        first_name: "admin",
        last_name: "admin",
        email: "admin@a.com",
      },
    };
  },

  async created() {
    await this.fetchData();
    this.equipementReference = this.$route.params.equipementReference;
    if (this.equipementReference) {
      this.form.equipement = this.equipementReference;
    }
  },

  methods: {
    async fetchData() {
      try {
        const [equipementsResponse] = await Promise.all([
          api.getEquipements(),
        ]);
        this.equipements = equipementsResponse.data.map(eq => ({
          ...eq,
          label: `${eq.reference} - ${eq.designation}`
        }));
      } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
      }
    },

    

    resetForm() {
      this.form = {
        equipement: this.equipementReference || null,
        commentaireDefaillance: "",
        niveau: null,
      };
      this.validationDeclenchee = false;
      if (this.$refs.formulaire) {
        this.$refs.formulaire.resetValidation();
      }
    },

    retour(){
      this.router.go(-1); 
    },

    async validateForm() {
      this.validationDeclenchee = true;
      const formulaire = this.$refs.formulaire;

      if (formulaire) {
        formulaire.validate();
        if (this.formulaireValide) {
          try {
            const defaillanceData = {
              commentaireDefaillance: this.form.commentaireDefaillance,
              niveau: this.form.niveau,
              equipement: this.form.equipement,
              utilisateur: this.utilisateurConnecte.id,
              dateTraitementDefaillance: null
            };
            const response = await api.postDefaillance(defaillanceData);
            
            // Supposons que l'API renvoie l'ID de la défaillance créée
            const nouvelleDefaillanceId = response.data.id;
            
            alert("Défaillance signalée avec succès !");
            
            // Redirection vers la page de détails de la défaillance
            this.router.push({ name: 'FailureDetail', params: { id: nouvelleDefaillanceId } });
          } catch (error) {
            console.error('Erreur lors de la création de la défaillance:', error);
            alert("Une erreur est survenue lors de la création de la défaillance.");
          }
        } else {
          alert("Veuillez remplir tous les champs obligatoires.");
        }
      }
    },
  },
};
</script>