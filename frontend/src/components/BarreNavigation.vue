<template>
    <v-navigation-drawer app permanent>
      <!-- En-tête du tiroir de navigation avec le logo -->
      <template v-slot:prepend>
      <v-list-item
        lines="two"
        :prepend-avatar="require('@/assets/images/LogoGIMAO.png')" 
        class="d-flex justify-center" 
        style="height: 100px;" 
      >
        <v-list-item-title class="font-weight-bold text-center" style="font-size: 24px;">GIMAO</v-list-item-title> <!-- Ajustez la taille de la police ici -->
      </v-list-item>
    </template>
  
      <v-divider></v-divider> <!-- Séparateur entre l'en-tête et la liste -->
  
      <v-list density="compact" nav class="d-flex flex-column align-center">
        
        <!-- Élément de navigation pour le tableau de bord -->
        <v-list-item 
          @click="selectItem('TableauDeBord')" 
          :class="{ 'active-item': selectedItem === 'TableauDeBord', 'no-hover': selectedItem === 'TableauDeBord', 'inner-shadow': true }"
          class="item-size"
        >
          <template v-slot:prepend>
            <img 
              src="@/assets/images/Graphe.svg" 
              alt="Icone Tableau de bord" 
              :class="{ 'active-icon': selectedItem === 'TableauDeBord', 'inner-shadow': true }" 
              style="width: 60%; height: auto; margin-right: 2%;" 
            />
          </template>
          <v-list-item-title class="font-weight-bold text-center">Tableau de bord</v-list-item-title>
        </v-list-item>
  
        <!-- Élément de navigation pour les équipements -->
        <v-list-item 
          @click="selectItem('Equipements')" 
          :class="{ 'active-item': selectedItem === 'Equipements', 'no-hover': selectedItem === 'Equipements', 'inner-shadow': true }"
          class="item-size"
        >
          <template v-slot:prepend>
            <img 
              src="@/assets/images/Outils.svg" 
              alt="Icone Equipements" 
              :class="{ 'active-icon': selectedItem === 'Equipements' }" 
              style="width: 50%; height: auto; margin-right: 2%;" 
            />
          </template>
          <v-list-item-title class="font-weight-bold text-center">Equipements</v-list-item-title>
        </v-list-item>
  
        <!-- Élément de navigation pour les maintenances -->
        <v-list-item 
          @click="selectItem('Maintenances')" 
          :class="{ 'active-item': selectedItem === 'Maintenances', 'no-hover': selectedItem === 'Maintenances', 'inner-shadow': true }"
          class="item-size"
        >
          <template v-slot:prepend>
            <img 
              src="@/assets/images/Maintenance.svg" 
              alt="Icone Maintenance" 
              :class="{ 'active-icon': selectedItem === 'Maintenances', 'inner-shadow': true }" 
              style="width: 50%; height: auto; margin-right: 2%;" 
            />
          </template>
          <v-list-item-title class="font-weight-bold text-center">Maintenances</v-list-item-title>
        </v-list-item>
  
        <!-- Élément de navigation pour les techniciens -->
        <v-list-item 
          @click="selectItem('Techniciens')" 
          :class="{ 'active-item': selectedItem === 'Techniciens', 'no-hover': selectedItem === 'Techniciens', 'inner-shadow': true }"
          class="item-size"
        >
          <template v-slot:prepend>
            <img 
              src="@/assets/images/Techniciens.svg" 
              alt="Icone Techniciens" 
              :class="{ 'active-icon': selectedItem === 'Techniciens' }" 
              style="width: 50%; height: auto; margin-right: 2%;" 
            />
          </template>
          <v-list-item-title class="font-weight-bold text-center">Techniciens</v-list-item-title>
        </v-list-item>

        <!-- Élément de navigation pour la gestion des comptes -->
        <v-list-item 
          @click="selectItem('GestionComptes')" 
          :class="{ 'active-item': selectedItem === 'GestionComptes', 'no-hover': selectedItem === 'GestionComptes', 'inner-shadow': true }"
          class="item-size"
        >
          <template v-slot:prepend>
            <img 
              src="@/assets/images/GestionComptes.svg" 
              alt="Icone GestionDesComptes" 
              :class="{ 'active-icon': selectedItem === 'GestionComptes' }" 
              style="width: 50%; height: auto; margin-right: 2%;" 
            />
          </template>
          <v-list-item-title class="font-weight-bold text-center">Gestion des <br>comptes</v-list-item-title>
        </v-list-item>

        <!-- Élément de navigation pour les commandes -->
        <v-list-item 
          @click="selectItem('Commandes')" 
          :class="{ 'active-item': selectedItem === 'Commandes', 'no-hover': selectedItem === 'Commandes', 'inner-shadow': true }"
          class="item-size"
        >
          <template v-slot:prepend>
            <img 
              src="@/assets/images/Commande.svg" 
              alt="Icone Commandes" 
              :class="{ 'active-icon': selectedItem === 'Commandes' }" 
              style="width: 50%; height: auto; margin-right: 2%;" 
            />
          </template>
          <v-list-item-title class="font-weight-bold text-center">Commandes</v-list-item-title>
        </v-list-item>

        <!-- Élément de navigation pour les stocks -->
        <v-list-item 
          @click="selectItem('Stocks')" 
          :class="{ 'active-item': selectedItem === 'Stocks', 'no-hover': selectedItem === 'Stocks', 'inner-shadow': true }"
          class="item-size"
        >
          <template v-slot:prepend>
            <img 
              src="@/assets/images/Stocks.svg" 
              alt="Icone Stocks" 
              :class="{ 'active-icon': selectedItem === 'Stocks' }" 
              style="width: 50%; height: auto; margin-right: 2%;" 
            />
          </template>
          <v-list-item-title class="font-weight-bold text-center">Stocks</v-list-item-title>
        </v-list-item>

      </v-list>
    </v-navigation-drawer>

  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedItem: null, // État pour garder la trace de l'élément sélectionné
      };
    },
    methods: {
      // Méthode appelée lors de la sélection d'un élément
      selectItem(item) {
        this.selectedItem = item; // Met à jour l'élément sélectionné
        this.$emit('item-selected', item); // Émet l'événement pour le parent
      },
    },
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
  
  body {
    font-family: 'Poppins', sans-serif; 
  }
  
  .v-list-item {
    color: #000; /* Couleur par défaut des éléments */
    display: flex; /* Utiliser flexbox pour l'alignement */
    justify-content: flex-start; /* Aligner à gauche */
    align-items: center; /* Centrer verticalement */
    padding: 5%; /* Ajouter du padding pour l'espacement */
    width: 80%; /* Largeur fixe pour tous les éléments */
    height: auto; /* Hauteur automatique pour les éléments */
  }
  
  .v-list-item:not(.no-hover):hover {
    background-color: #e0e0e0; /* Couleur de fond au survol */
  }
  
  .active-item {
    background-color: #5D5FEF; /* Couleur de fond lorsque l'élément est sélectionné */
    color: #fff; /* Couleur du texte lorsque l'élément est sélectionné */
  }
  
  .active-icon {
    filter: brightness(0) invert(1); /* Change la couleur du SVG en blanc */
  }
  
  .inner-shadow {
    box-shadow: inset 0 20px 50px rgba(55, 69, 87, 0.1); /* Ombre intérieure avec opacité de 10% */
  }

  
  </style>