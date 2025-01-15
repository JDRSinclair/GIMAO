<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <!-- Section gauche : Détails de l'équipement -->
          <v-col cols="12" md="6">
            <v-card elevation="1" class="rounded-lg pa-2">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Description de l'équipement</v-card-title>

              <v-row class="pa-2">
                <v-col cols="12">
                  <div class="grid-container">
                    <div class="grid-title"><strong>Référence de l'équipement (numéro de série) :</strong></div>
                    <div class="grid-data">{{ equipement.reference || 'N/A' }}</div>
                    <div class="grid-title"><strong>Désignation de l'équipement :</strong></div>
                    <div class="grid-data">{{ equipement.designation || 'N/A' }}</div>
                    <div class="grid-title"><strong>Salle :</strong></div>
                    <div class="grid-data">{{ equipement.lieu?.nomLieu || 'N/A' }}</div>
                    <div class="grid-title"><strong>État :</strong></div>
                    <div class="grid-data">{{ equipement.dernier_statut?.statutEquipement || 'N/A' }}</div>
                    <div class="grid-title"><strong>Mise en fonction :</strong></div>
                    <div class="grid-data">{{ equipement.miseEnFonction || 'N/A' }}</div>
                    <div class="grid-title"><strong>Prix de l'équipement (€) :</strong></div>
                    <div class="grid-data">{{ equipement.prix || 'N/A' }}</div>
                    <div class="grid-title"><strong>Fournisseur :</strong></div>
                    <div class="grid-data">{{ equipement.fournisseur?.nomFournisseur || 'N/A' }}</div>
                    <div class="grid-title"><strong>Modèle :</strong></div>
                    <div class="grid-data">{{ equipement.modeleEquipement?.nomModeleEquipement || 'N/A' }}</div>
                  </div>
                </v-col>
              </v-row>

              <!-- Section documentation -->
              <v-card elevation="1" class="rounded-lg pa-2">
                <v-card-title class="font-weight-bold text-uppercase text-primary">Documentation</v-card-title>

                <v-data-table
                  :headers="entetes"
                  :items="documents"
                  item-value="nomDocument"
                  class="elevation-1 rounded-lg"
                  hide-default-footer
                >
                  <template v-slot:item="{ item, index }">
                    <tr @click="telechargerDocument(item)" style="cursor: pointer;">
                      <td>
                        {{ item.nomDocument || 'N/A' }}
                      </td>
                    </tr>
                  </template>
                </v-data-table>
              </v-card>
            </v-card>
          </v-col>

          <!-- Section droite : Image, consommables, maintenance et actions -->
          <v-col cols="12" md="6">
            <!-- Section image -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-img
                :src="equipement.image"
                aspect-ratio="4/3"
                class="rounded-lg"
                style="max-height: 30vh;"
                alt="Image de l'équipement"
              ></v-img>
            </v-card>
            
            <!-- Section consommables -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">
                Consommables
              </v-card-title>
              <v-data-table
                :items="consommables"
                class="elevation-1 rounded-lg"
                hide-default-footer
              >
                <template v-slot:header>
                  <tr>
                    <th>Nom pièce</th>
                    <th>État de la pièce</th>
                    <th>En stock</th>
                  </tr>
                </template>
                <template v-slot:item="{ item }">
                  <tr>
                    <td>{{ item.nom || 'N/A' }}</td>
                    <td>{{ item.etat || 'N/A' }}</td>
                    <td>{{ item.stock || 'N/A' }}</td>
                  </tr>
                </template>
              </v-data-table>
            </v-card>

            <!-- Section historique de maintenance -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">
                Maintenances effectuées
              </v-card-title>
              <v-data-table
                :items="maintenances"
                class="elevation-1 rounded-lg"
                hide-default-footer
              >
                <template v-slot:header>
                  <tr>
                    <th>Numéro</th>
                    <th>Date</th>
                    <th>Action</th>
                  </tr>
                </template>
                <template v-slot:item="{ item }">
                  <tr>
                    <td>{{ item.numero || 'N/A' }}</td>
                    <td>{{ item.date || 'N/A' }}</td>
                    <td>
                      <v-btn icon @click="voirMaintenance(item)">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-eye eye-icon">
                          <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                          <circle cx="12" cy="12" r="3"></circle>
                        </svg>
                      </v-btn>
                    </td>
                  </tr>
                </template>
              </v-data-table>
            </v-card>

            <!-- Bouton d'action -->
            <v-row justify="end">
              <v-btn color="primary" class="mt-4" large>
                Modifier
              </v-btn>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import api from '@/services/api';

export default {
  name: 'VisualiserEquipement',
  setup() {
    const route = useRoute();
    const equipementId = route.params.reference; // Assuming the route parameter is named 'reference'
    
    // Reactive state
    const equipement = ref({});
    const documents = ref([]);
    const consommables = ref([]);
    const maintenances = ref([]);
    const isLoading = ref(true);
    
    // Fetch equipment data
    const fetchEquipementData = async () => {
      try {
        // Fetch the specific equipment details
        const equipementResponse = await api.getEquipementById(equipementId);
        equipement.value = equipementResponse.data;
      
        // Fetch the full list of equipment to get dateMiseEnService and prixAchat
        const equipementsResponse = await api.getEquipements();
        const fullEquipementData = equipementsResponse.data.find(
          (eq) => eq.reference === equipementId
        );
      
        // If the equipment is found in the full list, merge the data
        if (fullEquipementData) {
          equipement.value = {
            ...equipement.value, // Existing data from getEquipementById
            miseEnFonction: fullEquipementData.dateMiseEnService, // Add dateMiseEnService
            prix: fullEquipementData.prixAchat, // Add prixAchat
          };
        }
      
        // Extract documents from the response
        documents.value = [
          ...equipementResponse.data.documents_techniques,
          ...equipementResponse.data.documents_defaillance,
          ...equipementResponse.data.documents_intervention,
        ];
      
        // Extract consumables from the response
        consommables.value = equipementResponse.data.consommables_compatibles;
      
        // Extract maintenances (if available)
        maintenances.value = []; // You can mock this if needed
      } catch (error) {
        console.error('Error fetching equipment data:', error);
      } finally {
        isLoading.value = false;
      }
    };
  
    // Fetch all data on component mount
    onMounted(fetchEquipementData);
  
    return {
      equipement,
      documents,
      consommables,
      maintenances,
      isLoading,
      entetes: [
        { text: "Document", value: "nomDocument", align: "start" }
      ],
    };
  },
  methods: {
    telechargerDocument(item) {
      console.log('Document sélectionné:', item);
    },
    voirMaintenance(item) {
      console.log('Maintenance en cours de visualisation:', item);
    },
  },
};
</script>

<style scoped>
.text-primary {
  color: #05004E;
}

.text-dark {
  color: #3C3C3C;
}

.v-card {
  background-color: #FFFFFF;
}

.v-btn {
  background-color: #F1F5FF;
  border-radius: 50%;
}

.eye-icon {
  width: 24px;
  height: 24px;
}

h1 {
  color: #05004E;
}

/* CSS Grid for aligning titles and data */
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr; /* Two columns: one for titles, one for data */
  gap: 8px; /* Space between rows */
  align-items: center; /* Vertically align items */
}

.grid-title {
  font-weight: bold;
  white-space: normal; /* Allow titles to wrap */
  word-break: break-word; /* Break long words if necessary */
}

.grid-data {
  white-space: nowrap; /* Prevent data from wrapping */
}

/* Responsive adjustments for small screens */
@media (max-width: 768px) {
  .grid-container {
    grid-template-columns: 1fr; /* Switch to a single column on small screens */
  }

  .grid-title {
    white-space: normal; /* Allow titles to wrap */
    word-break: normal; /* Prevent excessive line breaks */
  }

  .grid-data {
    white-space: normal; /* Allow data to wrap if needed */
  }
}
</style>