<template>
  <v-app>

    <!-- Contenu principal -->
    <v-main>
      <v-container>
        <!-- Filtres et tableau -->
        <v-row>
        <!-- Colonne contenant Liste des salles et Types d'équipements -->
        <v-col cols="3"> <!-- Réduit la largeur à 3/12 -->
          <v-card elevation="1" class="rounded-lg pa-2 mb-4">
            <v-card-title class="font-weight-bold text-uppercase text-primary">Liste des salles</v-card-title>
            <v-divider></v-divider>
            <v-list dense>
              <v-list-item v-for="(salle, index) in salles" :key="index" link>
                <v-list-item-title>{{ salle }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-card>

          <v-card elevation="1" class="rounded-lg pa-2">
            <v-card-title class="font-weight-bold text-uppercase text-primary">Types d'équipements</v-card-title>
            <v-divider></v-divider>
            <v-list dense>
              <v-list-item v-for="(type, index) in typesEquipements" :key="index" link>
                <v-list-item-title>{{ type }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>

        <v-col cols="9"> <!-- Augmente la largeur à 9/12 -->
          <!-- Bouton en haut du tableau pour appeler une autre page -->
          <v-btn
            color="primary"
            @click="goToAnotherPage"
            class="mb-4"
          >
            Aller à une autre page
          </v-btn>

          <v-data-table
            :headers="headers"
            :items="equipements"
            item-value="name"
            class="elevation-1 rounded-lg"
            hide-default-footer
          >
            <template v-slot:item="{ item }">
              <tr @click="changerEquipement(item)" style="cursor: pointer;">
                <!-- Contenu de chaque cellule -->
                <td>{{ item.equipement }}</td>
                <td>{{ item.salle }}</td>
                <td>{{ item.etat }}</td>
              </tr>
            </template>
          </v-data-table>
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
  name: 'Equipements',
  components: {
    NavigationDrawer,
    TopNavBar,
  },
  
  data() {
    return {
      menuItems: [
        { name: 'Tableau de bord', icon: require('@/assets/images/Graphe.svg') },
        { name: 'Equipements', icon: require('@/assets/images/Outils.svg') },
        { name: 'Maintenances', icon: require('@/assets/images/Maintenance.svg') },
        { name: 'Techniciens', icon: require('@/assets/images/Techniciens.svg') },
      ],
      salles: ["Tous", "Salle 1", "Salle 2", "Salle 3", "Salle 4"],
      typesEquipements: ["Tous", "Type 1", "Type 2", "Type 3", "Type 4"],
      headers: [
        { text: "Équipement", value: "equipement", align: "start" },
        { text: "Salle", value: "salle" },
        { text: "État", value: "etat" },
      ],
      equipements: [
        { equipement: "Équipement 1", salle: "Salle 1", etat: "À l'arrêt" },
        { equipement: "Équipement 2", salle: "Salle 1", etat: "Rebuté" },
        { equipement: "Équipement 3", salle: "Salle 1", etat: "Fonctionnel" },
        { equipement: "Équipement 4", salle: "Salle 2", etat: "Fonctionnel" },
        { equipement: "Équipement 5", salle: "Salle 2", etat: "Fonctionnel" },
        { equipement: "Équipement 6", salle: "Salle 3", etat: "À l'arrêt" },
        { equipement: "Équipement 7", salle: "Salle 4", etat: "Fonctionnel" },
        { equipement: "Équipement 8", salle: "Salle 4", etat: "Fonctionnel" },
      ],
    };
  },
  methods: {
    goToAnotherPage() {
      this.$router.push({ name: 'AjouterEquipement' });
    },
    handleItemSelected(item) {
      console.log('Selected item:', item);
    },
    changerEquipement(item) {
      console.log('Selected item:', item);
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

h1 {
  color: #05004E;
}
</style>