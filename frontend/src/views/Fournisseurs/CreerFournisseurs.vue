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
                      v-model="form.nomFournisseur"
                      label="Nom du Fournisseur"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Nom du Fournisseur requis', v => v.length <= 50 || 'Max 50 caractères']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.numRue"
                      label="Numéro de Rue"
                      type="number"
                      outlined
                      dense
                      :rules="[v => !!v || 'Numéro de Rue requis', v => Number.isInteger(Number(v)) || 'Doit être un nombre entier']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.nomRue"
                      label="Nom de la Rue"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Nom de la Rue requis', v => v.length <= 50 || 'Max 50 caractères']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.codePostal"
                      label="Code Postal"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Code Postal requis', v => v.length <= 50 || 'Max 50 caractères']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.ville"
                      label="Ville"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Ville requise', v => v.length <= 50 || 'Max 50 caractères']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.paysFournisseur"
                      label="Pays"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Pays requis', v => v.length <= 50 || 'Max 50 caractères']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.mailFournisseur"
                      label="Email"
                      type="email"
                      outlined
                      dense
                      :rules="[v => !v || isValidEmail(v) || 'Email invalide', v => !v || v.length <= 50 || 'Max 50 caractères']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.numTelephoneFournisseur"
                      label="Numéro de Téléphone"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !v || isValidPhone(v) || 'Numéro de Téléphone invalide', v => !v || v.length <= 15 || 'Max 15 caractères']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-checkbox
                      v-model="form.serviceApresVente"
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
      nomFournisseur: "",        
      numRue: "",              
      nomRue: "",             
      codePostal: "",   
      ville: "",          
      paysFournisseur: "",   
      mailFournisseur: "",    
      numTelephoneFournisseur: "",    
      serviceApresVente: false,    
    });

    const formulaireValide = ref(null);

    const isValidEmail = (email) => {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailPattern.test(email);
    };

    const isValidPhone = (phone) => {
      const phonePattern = /^\+?1?\d{9,15}$/;
      return phonePattern.test(phone);
    };

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
      isValidEmail,
      isValidPhone
    };
  },
};
</script>

<style scoped>
.v-card {
  background-color: #FFFFFF;
}
</style>
