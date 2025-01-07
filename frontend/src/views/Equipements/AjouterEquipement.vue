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
          <v-col cols="6">
            <v-card elevation="1" class="rounded-lg pa-2"> 
              <v-card-title class="font-weight-bold text-uppercase text-primary">Ajouter un équipement</v-card-title>

              <v-text-field
                v-model="ReferenceEquipement"
                label="Réference de l'équipement (num série)"
                outlined
                dense
              ></v-text-field>

              <v-text-field
                v-model="DesignationEquipement"
                label="Désignation de l'équipement"
                outlined
                dense
              ></v-text-field>

              <v-text-field
                v-model="TypeEquipment"
                label="Type de l'équipement"
                outlined
                dense
              ></v-text-field>

              <v-row align="center" no-gutters>
                <v-col cols="10">
                  <v-select
                    v-model="Selectionlieu"
                    :items="lieux" 
                    label="Choisir un lieu"
                    outlined
                    dense
                  ></v-select>
                </v-col>
                <v-col cols="2" class="d-flex justify-center align-center" style="padding-bottom: 20px;">
                  <!-- Bouton invisible avec icône -->
                  <v-btn 
                    color="transparent"
                    @click="ajouterlieu" 
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
              
              <v-select
                v-model="SelectionEtat"
                :items="etats" 
                label="Choisir un etat"
                outlined
                dense
              ></v-select>

              <v-text-field
                v-model="miseEnFonctionDate"
                label="Mise en fonction"
                type="date"
                outlined
                dense
              ></v-text-field>

              <v-text-field
                v-model="prixEquipement"
                label="Prix de l'équipement (€)"
                type="number"
                outlined
                dense
                prefix="€"
                min="0"
                step="0.01"
              ></v-text-field>
              <v-row align="center" no-gutters>
                <v-col cols="10">
                  <v-select
                    v-model="Fournisseur"
                    :items="fournisseurs" 
                    label="Choisir un fournisseur"
                    outlined
                    dense
                  ></v-select>
                </v-col>
                <v-col cols="2" class="d-flex justify-center align-center" style="padding-bottom: 20px;">
                    <!-- Bouton invisible avec icône -->
                  <v-btn 
                      color="transparent"
                      @click="ajouterFournisseur" 
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
              <v-row align="center" no-gutters>
                <v-col cols="10">
                  <v-select
                    v-model="Modele"
                    :items="modeles" 
                    label="Choisir un modèle"
                    outlined
                    dense
                  ></v-select>
                </v-col>
                <v-col cols="2" class="d-flex justify-center align-center" style="padding-bottom: 20px;">
                    <!-- Bouton invisible avec icône -->
                    <v-btn 
                      color="transparent"
                      @click="ajouterModele" 
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
              <v-card elevation="1" class="rounded-lg pa-2">
                <v-card-title class="font-weight-bold text-uppercase text-primary">
                  Documentation
                  <!-- Bouton pour ajouter une ligne -->
                  <v-btn 
                    color="transparent"
                    @click="triggerFileInputDocumentation" 
                    icon
                    class="rounded-circle"
                    style="border: none; box-shadow: none;"
                  >
                    <img 
                      src="@/assets/images/iconPlus.svg" 
                      alt="Icone Plus"   
                    />
                  </v-btn>

                </v-card-title>

                <!-- Table des documents -->
                <v-data-table
                  :headers="headers"
                  :items="documentations"
                  item-value="nomDocumentation"
                  class="elevation-1 rounded-lg"
                  hide-default-footer
                >
                  <!-- Personnaliser la ligne entière pour être cliquable -->
                  <template v-slot:item="{ item, index }">
                    <tr @click="telechargerDoc(item)" style="cursor: pointer;">
                      <td>
              
                        {{ item.nomDocumentation }}
        
                      </td>
                      <td class="text-right">
                        <!-- Bouton de suppression -->
                        <v-btn
                          color="transparent"
                          icon
                          @click.stop="effacerLigneDocumentation(index)"
                          style="border: none; box-shadow: none;"
                        >
                          <img 
                            src="@/assets/images/iconEffacer.svg" 
                            alt="Icone Effacer"   
                          />
                        </v-btn>
                      </td>
                    </tr>
                  </template>
                </v-data-table>

                <!-- Input invisible pour choisir un fichier -->
                <input 
                  ref="fileInputDocumentation" 
                  type="file" 
                  style="display: none;" 
                  @change="handleFileChange" 
                />
              </v-card>
            </v-card>
          </v-col>
          <v-col cols="6">
            <!-- Image Section -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <!-- Vérifier si une image a été sélectionnée -->
              <template v-if="imageSrc">
                <v-row justify="center" align="center" class="fill-height" no-gutters>
                  <v-col cols="auto">
                    <v-img
                      :src="imageSrc"
                      width="300px"
                      height="300px"
                      class="rounded-lg"
                      alt="Equipment Image"
                      @click="triggerFileInputImage"
                    ></v-img>
                  </v-col>
                </v-row>
              </template>

              <!-- Si aucune image n'est sélectionnée, afficher le bouton -->
              <template v-else>
                <v-row justify="center" align="center" class="fill-height">
                  <v-col cols="auto">
                    <v-btn 
                      color="transparent"
                      @click="triggerFileInputImage" 
                      icon
                      class="rounded-circle"
                      style="border: none; box-shadow: none; ;"
                    >
                      <img 
                        src="@/assets/images/iconPlus.svg" 
                        alt="Icone Plus"   
                      />
                    </v-btn>
                  </v-col>
                </v-row>
              </template>

              <!-- Input invisible pour choisir une image -->
              <input 
                ref="fileInputImage" 
                type="file" 
                style="display: none;" 
                accept="image/*"
                @change="changementImage" 
              />

            </v-card>
            
            <!-- consommables Section -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-row align="center">
                <v-card-title class="font-weight-bold text-uppercase text-primary">
                  Consommables
                </v-card-title>

                <!-- Liste déroulante pour la sélection d'un consommable -->
                <v-col cols="auto">
                  <v-select
                    v-model="selectedConsommable"
                    :items="listeConsommable"
                    item-text="name"
                    item-value="id"
                    label="Choisir un consommable"
                    return-object
                    @change="ajouterConsommable"
                    class="mt-0"
                    dense
                    style="font-size: 18px; min-width: 250px; height: 50px;"
                  ></v-select>
                </v-col>
                <v-btn
                  color="transparent"
                  @click="ajouterConsommable"
                  icon
                  class="rounded-circle"
                  style="border: none; box-shadow: none;"
                >
                  <img
                    src="@/assets/images/iconPlus.svg"
                    alt="Icone Plus"
                  />
                </v-btn>
              </v-row>
                <v-data-table
                  :headers="headers"
                  :items="consommables"
                  item-key="id"
                  class="elevation-1 rounded-lg"
                  hide-default-footer
                >
                  <!-- Personnaliser la ligne entière pour être cliquable -->
                  <template v-slot:item="{ item, index }">
                    <tr>
                      <!-- Colonne Nom -->
                      <td>{{ item.name }}</td>

                      <!-- Colonne État -->
                      <td>{{ item.status }}</td>

                      <!-- Colonne Stock -->
                      <td>{{ item.stock }}</td>

                      <!-- Colonne Action : Bouton de suppression -->
                      <td class="text-right">
                        <v-btn
                          color="transparent"
                          icon
                          @click.stop="effacerConsommable(index)"
                          style="border: none; box-shadow: none;"
                        >
                          <img
                            src="@/assets/images/iconEffacer.svg"
                            alt="Icone Effacer"
                          />
                        </v-btn>
                      </td>
                    </tr>
                  </template>

                  <!-- Définir l'en-tête des colonnes -->
                  <template v-slot:columns="{ columns }">
                    <tr>
                      <th v-for="column in columns" :key="column.text" class="text-center pa-1">
                        {{ column.text }}
                      </th>
                    </tr>
                  </template>
                </v-data-table>
            </v-card>



            <!-- Maintenance History Section -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">
                Maintenances effectuées
              </v-card-title>
              <v-data-table
                :headers="[
                  { text: 'Numéro', value: 'number' },
                  { text: 'Date', value: 'date' },
                  { text: '', value: 'action', align: 'center' }
                ]"
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
              <v-btn color="secoundary" class="mt-4 rounded" @click="$router.go(-1)" style="border-radius: 0; margin-right: 35px;" large>
                Annuler
              </v-btn>
              <v-btn color="primary" class="mt-4 rounded" style="border-radius: 0 ;margin-right: 35px;" large>
                Confirmer
              </v-btn>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

import '@/assets/css/global.css'; 

export default {
  name: 'AjouterEquipement',

  
  data() {
    return {
      ReferenceEquipement: "",
      DesignationEquipement: "",         // Variable pour le nom de l'équipement
      TypeEquipment: "",         // Variable pour le type de l'équipement
      Selectionlieu: null,        // Variable pour la lieu sélectionnée
      lieux: [                   // Liste des lieux disponibles
        'lieu1','lieu2','lieu3'
        // Ajouter d'autres lieux si nécessaire
      ],
      SelectionEtat: null,        // Variable pour la lieu sélectionnée
      etats: [                   // Liste des lieux disponibles
        'En fonctionnement','Fonctionnement en mode dégradé',"A l'arrêt", 'Rebuté'
        // Ajouter d'autres lieux si nécessaire
      ],
      miseEnFonctionDate: '',
      prixEquipement: '',
      Fournisseur: null,
      Fabricant: null,
      fournisseurs: [                   // Liste des lieux disponibles
        'Fournisseur1','Fournisseur2','Fournisseur3'
        // Ajouter d'autres lieux si nécessaire
      ],
      modeles: [                   // Liste des lieux disponibles
        'Modèle1','Modèle2','Modèle3'
        // Ajouter d'autres lieux si nécessaire
      ],
      headers: [
        {text: "Document", value: "nomDocumentation", align: "start" }
      ],
      documentations: [
        // { nomDocumentation: "Doc1"},
        // { nomDocumentation: "Doc2"},
        // { nomDocumentation: "Doc3"},
      ],
      imageSrc: null,
      // Liste des consommables disponibles
      listeConsommable: [
        { id: 1, name: 'Consommable A', status: 'Disponible', stock: 20 },
        { id: 2, name: 'Consommable B', status: 'En rupture', stock: 0 },
        { id: 3, name: 'Consommable C', status: 'Disponible', stock: 50 },
      ],
      // Tableau pour stocker les consommables sélectionnés
      consommables: [],
      // Données du consommable sélectionné dans la liste déroulante
      selectedConsommable: null,
      // En-têtes du tableau
      headers: [
        { text: 'Nom pièce', value: 'name' },
        { text: 'État de la pièce', value: 'status' },
        { text: 'En stock', value: 'stock' }
      ],
    };
  },
  methods: {
    ajouterlieu() {
      console.log("Ajout d'une nouvelle lieu");
    },
    ajouterFournisseur() {
      console.log("Ajout d'un nouveau fournisseur");
    },
    ajouterModele() {
      console.log("Ajout d'un nouveau modèle");
    },
    telechargerDoc(item) {
      console.log('Selected item:', item);
    },
    effacerLigneDocumentation(index) {
      this.documentations.splice(index, 1);
      console.log("Ligne supprimée à l'index:", index);
    },
    effacerConsommable(index) {
      this.consommables.splice(index, 1);
      console.log("Ligne supprimée à l'index:", index);
    },
    
    // Ouvrir l'input de fichier pour la documentation
    triggerFileInputDocumentation() {
      this.$refs.fileInputDocumentation.click(); // Ouvre l'input pour un document
    },

    // Ouvrir l'input de fichier pour l'image
    triggerFileInputImage() {
      this.$refs.fileInputImage.click(); // Ouvre l'input pour une image
    },

    // Cette méthode gère le changement de fichier (documents)
    handleFileChange(event) {
      const file = event.target.files[0]; // Récupère le fichier sélectionné
      if (file) {
        // Si le fichier est une image, on appelle la méthode changementImage
        if (file.type.startsWith('image/')) {
          this.changementImage(event);
        } else {
          // Sinon, on traite le fichier comme un document
          console.log("Fichier sélectionné:", file.name);
          this.addDocument(file.name); // Ajouter le fichier à la table de documents
        }
      }
    },

    // Ajouter le fichier comme document
    addDocument(fileName) {
      this.documentations.push({ nomDocumentation: fileName });
    },

    // Cette méthode gère la sélection de l'image
    changementImage(event) {
      console.log("2");
      const file = event.target.files[0];
      if (file && file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = () => {
          this.imageSrc = reader.result; // Met l'image dans imageSrc
        };
        reader.readAsDataURL(file); // Lire le fichier en tant que Data URL
      } else {
        alert('Veuillez sélectionner une image valide.');
      }
    },
    ajouterConsommable() {
      if (this.selectedConsommable) {
        // Ajouter le consommable sélectionné à la table
        this.consommables.push(this.selectedConsommable);
        // Réinitialiser la sélection après ajout
        this.selectedConsommable = null;
      }
    },
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

h1 {
  color: #05004E;
}
</style>
