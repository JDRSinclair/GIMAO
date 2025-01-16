<template>
    <v-app>
      <v-main>
        <v-container>
          <v-form @submit.prevent="submitForm" ref="form" v-model="formValid">
  
            <!-- Champ Nom du Fabricant -->
            <v-text-field
              v-model="formData.nomFabricant"
              label="Nom du fabricant"
              :rules="[rules.required]"
              required
              outlined
              dense
              class="mb-4"
            ></v-text-field>
  
            <!-- Champ Pays du Fabricant -->
            <v-text-field
              v-model="formData.paysFabricant"
              label="Pays du fabricant"
              :rules="[rules.required]"
              required
              outlined
              dense
              class="mb-4"
            ></v-text-field>
  
            <!-- Champ Email du Fabricant -->
            <v-text-field
              v-model="formData.mailFabricant"
              label="Email du fabricant"
              :rules="[rules.required, rules.email]"
              required
              outlined
              dense
              type="email"
              class="mb-4"
            ></v-text-field>
  
            <!-- Champ Numéro de téléphone du Fabricant -->
            <v-text-field
              v-model="formData.numTelephoneFabricant"
              label="Numéro de téléphone"
              :rules="[rules.required, rules.phone, rules.phoneLength]"
              required
              outlined
              dense
              type="tel"
              class="mb-4"
            ></v-text-field>
  
            <!-- Champ Service Après Vente -->
            <v-checkbox
              v-model="formData.serviceApresVente"
              label="Service après-vente"
              class="mb-4"
            ></v-checkbox>
  
            <!-- Boutons de Soumission et Annulation -->
            <v-row justify="end">
              <v-btn
                color="secondary"
                class="mt-4 rounded"
                @click="goBack"
                style="border-radius: 0; margin-right: 35px;"
                large
              >
                Annuler
              </v-btn>
              <v-btn
                type="submit"
                color="primary"
                class="mt-4 rounded"
                style="border-radius: 0; margin-right: 35px;"
                large
              >
                Ajouter le fabricant
              </v-btn>
            </v-row>
          </v-form>
        </v-container>
      </v-main>
    </v-app>
  </template>
  
  <script>
  import api from '@/services/api';
  import { ref, reactive, toRefs } from 'vue';
  import { useRouter } from 'vue-router';
  
  export default {
    name: 'CreerFabricant',
    setup() {
      const router = useRouter();
      const formValid = ref(false); // Pour savoir si le formulaire est valide
      const state = reactive({
        formData: {
          nomFabricant: "",
          paysFabricant: "",
          mailFabricant: "",
          numTelephoneFabricant: "",
          serviceApresVente: false,
        },
      });
  
      const submitForm = async () => {
        const formData = new FormData();
        formData.append('nomFabricant', state.formData.nomFabricant);
        formData.append('paysFabricant', state.formData.paysFabricant);
        formData.append('mailFabricant', state.formData.mailFabricant);
        formData.append('numTelephoneFabricant', state.formData.numTelephoneFabricant);
        formData.append('serviceApresVente', state.formData.serviceApresVente);
  
        try {
          const responseFabricant = await api.createFabricant(formData);
          if (responseFabricant.status === 201) {
            console.log('Fabricant ajouté avec succès !');
            goBack();
          } else {
            console.log('Erreur lors de l’ajout du fabricant.');
          }
        } catch (error) {
          console.error('Erreur lors de la soumission du formulaire:', error);
        }
      };
  
      const rules = {
        required: (value) => !!value || "Ce champ est requis.",
        email: (value) => {
          const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          return emailRegex.test(value) || "Entrez une adresse e-mail valide.";
        },
        phone: (value) => {
          const phoneRegex = /^\+?[1-9]\d{1,14}$/; // Format E.164 (ex. +1234567890)
          return phoneRegex.test(value) || "Entrez un numéro de téléphone valide.";
        },
        // Nouvelle règle pour vérifier que le numéro contient exactement 10 chiffres
        phoneLength: (value) => {
          const phoneLengthRegex = /^\d{10}$/; // Vérifie exactement 10 chiffres
          return phoneLengthRegex.test(value) || "Le numéro de téléphone doit contenir exactement 10 chiffres.";
        }
      };
  
      const goBack = () => {
        router.go(-1);
      };
  
      return {
        ...toRefs(state),
        formValid,
        submitForm,
        rules,
        goBack,
      };
    },
  };
  </script>