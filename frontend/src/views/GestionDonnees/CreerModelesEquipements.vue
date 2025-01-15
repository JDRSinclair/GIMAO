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
              <h1 class="text-primary text-center mb-4">Créer Modele Equipement</h1>
              <v-form ref="formulaire" v-model="formulaireValide" @submit.prevent="validateForm">
                <v-row>
                  <v-col cols="6">
                    <v-text-field
                      v-model="form.nomModeleEquipement"
                      label="Nom du Modele de l'equipement"
                      type="text"
                      outlined
                      dense
                      :rules="[v => !!v || 'Nom du modele de l equipement requis', v => v.length <= 50 || 'Max 50 caractères']"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="6">
                    <v-text-field
                      v-model="form.fabricant"
                      label="ID du fabricant"
                      type="number"
                      outlined
                      dense
                      :rules="[v => !!v || 'Fabricant', v => Number.isInteger(Number(v)) || 'Doit être un nombre entier']"
                    ></v-text-field>
                  </v-col>

                  <v-row justify="center" class="mt-4">
                    <v-spacer></v-spacer>
                    <v-btn color="primary" class="text-white mx-2" @click="backPreviousPage">
                      Annuler
                    </v-btn>
                    <v-btn color="success" class="text-white mx-2" @click="validateForm">
                      Valider
                    </v-btn>
                    <v-spacer></v-spacer>
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
  name: 'CreerModelesEquipements',
  
  setup() {
    const routeur = useRouter();

    const form = reactive({
      nomModeleEquipement: "",        
      fabricant: "",              
    });

    const formulaireValide = ref(null);

    const backPreviousPage = () => {
      routeur.push({ name: 'ModelesEquipements' });
    };

    const validateForm = async () => {
      if (formulaireValide.value) {
        try {
          await api.createFournisseur(form);
          alert("Modele Equipement créé avec succès !");
          backPreviousPage();
        } catch (error) {
          console.error('Erreur lors de la création du modele equipement:', error);
          alert("Erreur lors de la création du modele equipement.");
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
