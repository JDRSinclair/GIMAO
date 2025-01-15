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
              <h1 class="text-primary text-center mb-4">Créer Fournisseur</h1>
              <v-form ref="formulaire" v-model="formulaireValide" @submit.prevent="validateForm">
                <v-row>
                  <v-col cols="6">
                    <v-text-field
                      v-model="form.NomFournisseur"
                      label="Nom du Fournisseur"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Nom du Fournisseur requis']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.NumRue"
                      label="Numéro de Rue"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Numéro de Rue requis']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.NomRue"
                      label="Nom de la Rue"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Nom de la Rue requis']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.CodePostal"
                      label="Code Postal"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Code Postal requis']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.Ville"
                      label="Ville"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Ville requise']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.PaysFournisseur"
                      label="Pays"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Pays requis']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.MailFournisseur"
                      label="Email"
                      type="email"
                      outlined
                      dense
                      :rules="[v => !!v || 'Email requis']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.NumTelephoneFournisseur"
                      label="Numéro de Téléphone"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Numéro de Téléphone requis']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-checkbox
                      v-model="form.ServiceApresVente"
                      label="Service Après Vente"
                      outlined
                      dense
                    ></v-checkbox>
                  </v-col>

                  <v-row justify="center" class="mt-4">
                    <v-btn color="primary" class="text-white mx-2" @click="backPreviousPage">
                      Annuler
                    </v-btn>
                    <v-btn color="success" class="text-white mx-2" @click="validateForm">
                      Valider
                    </v-btn>
                  </v-row>
                </v-row>
              </v-form>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import '@/assets/css/global.css'; 
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/services/api';

export default {
  name: 'CreerFournisseurs',
  
  setup() {
    const routeur = useRouter();

    const form = reactive({
      NomFournisseur: "",        
      NumRue: "",              
      NomRue: "",             
      CodePostal: "",   
      Ville: "",          
      PaysFournisseur: "",   
      MailFournisseur: "",    
      NumTelephoneFournisseur: "",    
      ServiceApresVente: false,    
    });

    const formulaireValide = ref(null);

    const backPreviousPage = () => {
      routeur.push({ name: 'Fournisseurs' });
    };

    const validateForm = async () => {
      if (formulaireValide.value) {
        try {
          await api.createFournisseur(form);
          alert("Fournisseur créé avec succès !");
          backPreviousPage();
        } catch (error) {
          console.error('Erreur lors de la création du fournisseur:', error);
          alert("Erreur lors de la création du fournisseur.");
        }
      } else {
        alert("Le formulaire n'est pas complet. Veuillez remplir les champs obligatoires.");
      }
    };

    return {
      form, 
      backPreviousPage,
      validateForm,
      formulaireValide,
    };
  },
};
</script>

<style scoped>
.v-card {
  background-color: #FFFFFF;
}
</style>
