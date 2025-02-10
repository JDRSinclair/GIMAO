<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title>Ajouter un nouveau fournisseur</v-card-title>
          <v-card-text>
            <v-alert v-if="errorMessage" type="error">
              {{ errorMessage }}
            </v-alert>
            <v-form @submit.prevent="submit_form">
              <v-text-field
                v-model="fournisseur.nomFournisseur"
                label="Nom du fournisseur"
                required
              ></v-text-field>
              
              <v-text-field
                v-model="fournisseur.numRue"
                label="Numéro de rue"
                type="number"
                required
              ></v-text-field>
              
              <v-text-field
                v-model="fournisseur.nomRue"
                label="Nom de rue"
                required
              ></v-text-field>
              
              <v-text-field
                v-model="fournisseur.codePostal"
                label="Code postal"
                required
              ></v-text-field>
              
              <v-text-field
                v-model="fournisseur.ville"
                label="Ville"
                required
              ></v-text-field>
              
              <v-text-field
                v-model="fournisseur.paysFournisseur"
                label="Pays"
                required
              ></v-text-field>
              
              <v-text-field
                v-model="fournisseur.mailFournisseur"
                label="Email"
                type="email"
                required
              ></v-text-field>
              
              <v-text-field
                v-model="fournisseur.numTelephoneFournisseur"
                label="Numéro de téléphone"
                required
              ></v-text-field>
              
              <v-switch
                v-model="fournisseur.serviceApresVente"
                label="Service Après-Vente"
              ></v-switch>
              
              <v-btn color="secondary" class="mt-4 mr-2" @click="go_back">
                Retour
              </v-btn>
              <v-btn type="submit" color="primary" class="mt-4" :disabled="!isFormValid">
                Ajouter le fournisseur
              </v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/services/api';

export default {
  setup() {
    const router = useRouter();
    const fournisseur = ref({
      nomFournisseur: '',
      numRue: '',
      nomRue: '',
      codePostal: '',
      ville: '',
      paysFournisseur: '',
      mailFournisseur: '',
      numTelephoneFournisseur: '',
      serviceApresVente: false
    });
    const errorMessage = ref('');

    const isFormValid = computed(() => {
      return fournisseur.value.nomFournisseur &&
             fournisseur.value.numRue &&
             fournisseur.value.nomRue &&
             fournisseur.value.codePostal &&
             fournisseur.value.ville &&
             fournisseur.value.paysFournisseur &&
             fournisseur.value.mailFournisseur &&
             fournisseur.value.numTelephoneFournisseur;
    });

    const submit_form = async () => {
      if (!isFormValid.value) {
        errorMessage.value = 'Veuillez remplir tous les champs requis.';
        return;
      }

      try {
        const response = await api.postFournisseur(fournisseur.value);
        console.log('Fournisseur créé:', response.data);
        go_back();
      } catch (error) {
        console.error('Error creating fournisseur:', error);
      }
    };

    const go_back = () => {
      router.go(-1);
    };

    return {
      fournisseur,
      errorMessage,
      isFormValid,
      submit_form,
      go_back
    };
  }
};
</script>