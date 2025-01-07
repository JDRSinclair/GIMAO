<template>
  <v-app>
    <!-- Main Content -->
    <v-main>
      <v-container>
        <v-row>
          <!-- Left Section: Equipment Details -->
          <v-col cols="6">
            <v-card elevation="1" class="rounded-lg pa-2">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Détails de l'équipement</v-card-title>

              <v-row class="pa-2">
                <v-col cols="12">
                  <p><strong>Réference de l'équipement (num série):</strong> {{ equipment.ref }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Désignation de l'équipement:</strong> {{ equipment.designation }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Type de l'équipement:</strong> {{ equipment.type }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Salle:</strong> {{ equipment.salle }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>État:</strong> {{ equipment.etat }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Mise en fonction:</strong> {{ equipment.miseEnFonction }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Prix de l'équipement (€):</strong> {{ equipment.prix }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Fournisseur:</strong> {{ equipment.fournisseur }}</p>
                </v-col>
                <v-col cols="12">
                  <p><strong>Modèle:</strong> {{ equipment.modele }}</p>
                </v-col>
              </v-row>

              <!-- Documentation Section -->
              <v-card elevation="1" class="rounded-lg pa-2">
                <v-card-title class="font-weight-bold text-uppercase text-primary">Documentation</v-card-title>

                <v-data-table
                  :headers="headers"
                  :items="documentations"
                  item-value="nomDocumentation"
                  class="elevation-1 rounded-lg"
                  hide-default-footer
                >
                  <template v-slot:item="{ item, index }">
                    <tr @click="telechargerDoc(item)" style="cursor: pointer;">
                      <td>
                        {{ item.nomDocumentation }}
                      </td>
                    </tr>
                  </template>
                </v-data-table>
              </v-card>
            </v-card>
          </v-col>

          <!-- Right Section: Image, Consumables, Maintenance, and Actions -->
          <v-col cols="6">
            <!-- Image Section -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-img
                :src="equipment.image"
                aspect-ratio="4/3"
                class="rounded-lg"
                style="max-height: 30vh;"
                alt="Equipment Image"
              ></v-img>
            </v-card>
            
            <!-- Consumables Section -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">
                Consommables
              </v-card-title>
              <v-data-table
                :headers="consumablesHeaders"
                :items="consumables"
                class="elevation-1 rounded-lg"
                hide-default-footer
              >
                <template v-slot:item.name="{ item }">
                  <span>{{ item.name }}</span>
                </template>
                <template v-slot:item.status="{ item }">
                  <span>{{ item.status }}</span>
                </template>
                <template v-slot:item.stock="{ item }">
                  <span>{{ item.stock }}</span>
                </template>
              </v-data-table>
            </v-card>

            <!-- Maintenance History Section -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">
                Maintenances effectuées
              </v-card-title>
              <v-data-table
                :headers="maintenanceHeaders"
                :items="maintenances"
                class="elevation-1 rounded-lg"
                hide-default-footer
              >
                <template v-slot:item.number="{ item }">
                  <span>{{ item.number }}</span>
                </template>
                <template v-slot:item.date="{ item }">
                  <span>{{ item.date }}</span>
                </template>
                <template v-slot:item.action="{ item }">
                  <v-btn icon @click="viewMaintenance(item)">
                    <v-icon color="primary">mdi-eye</v-icon>
                  </v-btn>
                </template>
              </v-data-table>
            </v-card>

            <!-- Action Button -->
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
import TopNavBar from "@/components/TopNavBar.vue";
import '@/assets/css/global.css'; // Importation du fichier CSS global

export default {
  name: 'VisualiserEquipement',
  components: {
    NavigationDrawer,
    TopNavBar,
  },
  
  data() {
    return {
      headers: [
        { text: "Document", value: "nomDocumentation", align: "start" }
      ],
      documentations: [
        { nomDocumentation: "Doc1" },
        { nomDocumentation: "Doc2" },
        { nomDocumentation: "Doc3" }
      ],
      consumablesHeaders: [
        { text: "Nom pièce", value: "name" },
        { text: "État de la pièce", value: "status" },
        { text: "En stock", value: "stock" }
      ],
      consumables: [
        { name: "Pièce 1", status: "Endommagée", stock: 20 },
        { name: "Pièce 2", status: "Normale", stock: 7 },
        { name: "Pièce 3", status: "Normale", stock: 9 }
      ],
      maintenanceHeaders: [
        { text: "Numéro", value: "number" },
        { text: "Date", value: "date" },
        { text: "", value: "action", align: "center" }
      ],
      maintenances: [
        { number: 1, date: "10/07/24" },
        { number: 2, date: "05/04/24" },
        { number: 3, date: "15/01/24" }
      ],
      equipment: {
        ref: "Ref12345",
        designation: "Equipement X",
        type: "Type Y",
        salle: "Salle1",
        etat: "En fonctionnement",
        miseEnFonction: "2023-01-01",
        prix: 1200.00,
        fournisseur: "Fournisseur1",
        modele: "Modèle1",
        image: require('@/assets/images/LogoGIMAO.png')
      }
    };
  },
  methods: {
    telechargerDoc(item) {
      console.log('Selected item:', item);
    },
    viewMaintenance(item) {
      console.log('Viewing maintenance:', item);
    }
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

h1 {
  color: #05004E;
}
</style>
