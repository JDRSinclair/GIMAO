<template>
  <v-dialog v-model="isOpen" max-width="600px">
    <v-card>
      <v-card-title class="font-weight-bold text-uppercase text-primary">
        Ajouter un consommable
      </v-card-title>
      <v-card-text>
        <!-- Designation Field -->
        <v-text-field
          v-model="DesignationConsommable"
          label="Désignation du consommable"
          outlined
          dense
        ></v-text-field>

        <!-- Image Upload Section -->
        <v-card elevation="1" class="rounded-lg pa-2 mb-4">
          <template v-if="imageSrc">
            <v-row justify="center" align="center" class="fill-height" no-gutters>
              <v-col cols="auto">
                <v-img
                  :src="imageSrc"
                  width="300px"
                  height="300px"
                  class="rounded-lg"
                  alt="Consommable Image"
                  @click="activerFichierImage"
                ></v-img>
              </v-col>
            </v-row>
          </template>

          <template v-else>
            <v-row justify="center" align="center" class="fill-height">
              <v-col cols="auto">
                <v-btn 
                  color="transparent"
                  @click="activerFichierImage" 
                  icon
                  class="rounded-circle"
                  style="border: none; box-shadow: none;"
                >
                  <img 
                    src="@/assets/images/iconPlus.svg" 
                    alt="Icone Plus"   
                  />
                </v-btn>
              </v-col>
            </v-row>
          </template>

          <!-- Hidden Input for Image Upload -->
          <input 
            ref="fileInputImage" 
            type="file" 
            style="display: none;" 
            accept="image/*"
            @change="changementImage" 
          />
        </v-card>

        <!-- Fabricant Selection -->
        <v-row align="center" no-gutters>
          <v-col cols="10">
            <v-select
              v-model="Fabricant"
              :items="fabricants" 
              label="Choisir un fabricant"
              outlined
              dense
            ></v-select>
          </v-col>
          <v-col cols="2" class="d-flex justify-center align-center" style="padding-bottom: 20px;">
            <v-btn 
              color="transparent"
              @click="ajouterFabricant" 
              icon
              small
              class="rounded-circle"
              style="border: none; box-shadow: none;"
            >
              <img 
                src="@/assets/images/iconPlus.svg" 
                alt="Icone Plus"   
              />
            </v-btn>
          </v-col>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="secondary" @click="closeModal">Annuler</v-btn>
        <v-btn color="primary" @click="confirmerAjout">Confirmer</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'AjouterConsommableModal',
  props: {
    value: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      DesignationConsommable: "", // Designation of the consommable
      imageSrc: null, // Image URL for the consommable
      Fabricant: null, // Selected fabricant
      fabricants: [ // List of fabricants
        'Fabricant1', 'Fabricant2', 'Fabricant3'
      ],
    };
  },
  computed: {
    isOpen: {
      get() {
        console.log("Getting isOpen value:", this.value);
        return this.value;
      },
      set(value) {
        console.log("Setting isOpen value:", value);
        this.$emit('input', value); // Emit the new value to the parent component
      },
    },
  },
  methods: {
    // Method to add a new fabricant
    ajouterFabricant() {
      console.log("Ajout d'un nouveau fabricant");
    },

    // Method to handle image upload
    changementImage(event) {
      const file = event.target.files[0];
      if (file && file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = () => {
          this.imageSrc = reader.result; // Set the image source
        };
        reader.readAsDataURL(file); // Read the file as a Data URL
      } else {
        alert('Veuillez sélectionner une image valide.');
      }
    },

    // Method to close the modal
    closeModal() {
      console.log("Closing modal");
      this.isOpen = false; // This will trigger the computed setter and emit 'input'
    },

    // Method to confirm the addition of a consommable
    confirmerAjout() {
      const consommableData = {
        designation: this.DesignationConsommable,
        lienImageConsommable: this.imageSrc,
        fabricant_id: this.Fabricant,
      };
      console.log("Consommable à ajouter:", consommableData);
      this.closeModal();
      // Here you can add logic to send the data to your backend
    },

    // Method to activate the file input for image upload
    activerFichierImage() {
      this.$refs.fileInputImage.click();
    },
  },
};
</script>