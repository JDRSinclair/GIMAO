<template>
  <v-app>
    <!-- Contenu principal -->
    <v-main>
      <v-container>
        <v-row>
          <!-- Section gauche : Détails de l'équipement -->
          <v-col cols="6">
            <v-card elevation="1" class="rounded-lg pa-2">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Description de l'équipement</v-card-title>

              <v-row class="pa-2">
                <v-col cols="12">
                  <p><strong>Référence de l'équipement (numéro de série) :</strong> {{ equipement.reference }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Désignation de l'équipement :</strong> {{ equipement.designation }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Type de l'équipement :</strong> {{ equipement.type }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Salle :</strong> {{ equipement.salle }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>État :</strong> {{ equipement.etat }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Mise en fonction :</strong> {{ equipement.miseEnFonction }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Prix de l'équipement (€) :</strong> {{ equipement.prix }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Fournisseur :</strong> {{ equipement.fournisseur }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Modèle :</strong> {{ equipement.modele }}</p>
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
                        {{ item.nomDocument }}
                      </td>
                    </tr>
                  </template>
                </v-data-table>
              </v-card>
            </v-card>
          </v-col>

          <!-- Section droite : Image, consommables, maintenance et actions -->
          <v-col cols="6">
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
                    <td>{{ item.nom }}</td>
                    <td>{{ item.etat }}</td>
                    <td>{{ item.stock }}</td>
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
                    <td>{{ item.numero }}</td>
                    <td>{{ item.date }}</td>
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
import NavigationDrawer from '@/components/BarreNavigation.vue'; // Assurez-vous que le chemin est correct
import TopNavBar from "@/components/BarreNavigationHaut.vue";
import '@/assets/css/global.css'; // Importation du fichier CSS global

export default {
  name: 'VisualiserEquipement',
  components: {
    NavigationDrawer,
    TopNavBar,
  },
  
  data() {
    return {
      isLoadingEquipement: true,
      isLoadingDocuments: true,
      isLoadingConsommables: true,
      isLoadingMaintenances: true,
      equipement: {},
      documents: [],
      consommables: [],
      maintenances: [],
      entetes: [
        { text: "Document", value: "nomDocument", align: "start" }
      ],
    };
  },
  
  methods: {
    // Fetch equipment data
    fetchEquipementData(id) {
      // Simulate an API call
      setTimeout(() => {
        const mockEquipementData = {
          '1': {
            reference: "Ref12345",
            designation: "Equipement X",
            type: "Type Y",
            salle: "Salle1",
            etat: "En fonctionnement",
            miseEnFonction: "2023-01-01",
            prix: 1200.00,
            fournisseur: "Fournisseur1",
            modele: "Modèle1",
            image: require('@/assets/images/LogoGIMAO.png'),
          }
        };

        this.equipement = mockEquipementData[id] || {};
        this.isLoadingEquipement = false;
      }, 1000); // Simulate network delay
    },

    // Fetch documents data
    fetchDocumentsData(id) {
      // Simulate an API call
      setTimeout(() => {
        const mockDocumentsData = {
          '1': [
            { nomDocument: "Doc1" },
            { nomDocument: "Doc2" },
            { nomDocument: "Doc3" },
            { nomDocument: "Doc4" }
          ]
        };

        this.documents = mockDocumentsData[id] || [];
        this.isLoadingDocuments = false;
      }, 1200); // Simulate network delay
    },

    // Fetch consommables data
    fetchConsommablesData(id) {
      // Simulate an API call
      setTimeout(() => {
        const mockConsommablesData = {
          '1': [
            { nom: "Pièce 1", etat: "Endommagée", stock: 20 },
            { nom: "Pièce 2", etat: "Normale", stock: 7 },
            { nom: "Pièce 3", etat: "Normale", stock: 9 }
          ]
        };

        this.consommables = mockConsommablesData[id] || [];
        this.isLoadingConsommables = false;
      }, 800); // Simulate network delay
    },

    // Fetch maintenances data
    fetchMaintenancesData(id) {
      // Simulate an API call
      setTimeout(() => {
        const mockMaintenancesData = {
          '1': [
            { numero: 1, date: "10/07/24" },
            { numero: 2, date: "05/04/24" },
            { numero: 3, date: "15/01/24" }
          ]
        };

        this.maintenances = mockMaintenancesData[id] || [];
        this.isLoadingMaintenances = false;
      }, 1500); // Simulate network delay
    },

    // Other methods
    telechargerDocument(item) {
      console.log('Document sélectionné:', item);
    },
    voirMaintenance(item) {
      console.log('Maintenance en cours de visualisation:', item);
    },
  },

  
  created() {
    const equipementId = this.$route.params.id;
    this.fetchEquipementData(equipementId);
    this.fetchDocumentsData(equipementId);
    this.fetchConsommablesData(equipementId);
    this.fetchMaintenancesData(equipementId);
  }
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
</style>
