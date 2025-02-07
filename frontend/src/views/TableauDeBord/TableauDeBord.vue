<template>
  <v-app>
    <!-- Contenu principal -->
    <v-main>
      <v-container>

        <!-- Filtres et tableau -->
        <v-row>
          <!-- Colonne contenant Liste des défaillances signalées et Liste des interventions terminées -->
          <v-col cols="6">
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">
                Listes des défaillances signalées
                <v-spacer></v-spacer>
                <v-btn color="success" @click="transformerEnBonDeTravail">
                  Transformer en bon de travail
                </v-btn>
              </v-card-title>
              <v-divider></v-divider>
              <v-data-table
                :headers="defaillancesHeaders"
                :items="defaillances"
                :items-per-page="5"
                :page.sync="defaillancesPage"
                item-value="nom"
                class="elevation-1 rounded-lg"
                hide-default-footer
              ></v-data-table>
              <v-pagination
                v-model="defaillancesPage"
                :length="Math.ceil(defaillances.length / 5)"
              ></v-pagination>
            </v-card>
          </v-col>

          <v-col cols="6">
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">
                Listes des interventions terminées
                <v-spacer></v-spacer>
                <v-btn color="success" @click="cloturerFicheIntervention">
                  Clôturer la fiche d'intervention
                </v-btn>
              </v-card-title>
              <v-divider></v-divider>
              <v-data-table
                :headers="interventionsHeaders"
                :items="interventions"
                :items-per-page="5"
                :page.sync="interventionsPage"
                item-value="nom"
                class="elevation-1 rounded-lg"
                hide-default-footer
                @click:row="cloturerIntervention"
              ></v-data-table>
              <v-pagination
                v-model="interventionsPage"
                :length="Math.ceil(interventions.length / 5)"
              ></v-pagination>
            </v-card>
          </v-col>
        </v-row>

        <!-- Nombre de demandes d'interventions -->
        <v-row>
          <v-col>
            <h2 class="text-primary">Nombre de demandes d'interventions : {{ nombreInterventions }}</h2>
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
  components: {
    NavigationDrawer,
    TopNavBar,
  },

<<<<<<< Updated upstream
=======
  setup() {
    const router = useRouter();

    const ouvrirAfficherDefaillance = (id) => {
      router.push({ name: 'FailureDetail', params: { id: id } });
    };

    const ouvrirAfficherIntervention = (id) => {
      router.push({ name: 'AfficherIntervention', params: { id: id } });
    };

    return {
      ouvrirAfficherDefaillance,
      ouvrirAfficherIntervention
    };
  },

>>>>>>> Stashed changes
  data() {
    return {
      menuItems: [
        { name: 'Tableau de bord', icon: require('@/assets/images/Graphe.svg') },
        { name: 'Equipements', icon: require('@/assets/images/Outils.svg') },
        { name: 'Maintenances', icon: require('@/assets/images/Maintenance.svg') },
        { name: 'Techniciens', icon: require('@/assets/images/Techniciens.svg') },
      ],
      defaillancesHeaders: [
        { text: 'Nom', value: 'nom' },
        { text: 'Date de signalement', value: 'dateSignalement' },
      ],
      defaillances: [
        { nom: 'Défaillance sur Équipement "Distributeur de Savon"', dateSignalement: '18/08/2024' },
        { nom: 'Défaillance sur Équipement "Ordinateur SN25458"', dateSignalement: '19/08/2024' },
        { nom: 'Défaillance sur Équipement "Vidéo projecteur SN25458"', dateSignalement: '25/05/2024' },
        { nom: 'Défaillance sur Équipement "Tableau Blanc"', dateSignalement: '13/10/2024' },
      ],
      interventionsHeaders: [
        { text: 'Nom', value: 'nom' },
        { text: 'Date de signalement', value: 'dateSignalement' },
      ],
      interventions: [
        { nom: 'Intervention sur Équipement "Distributeur de Savon"', dateSignalement: '18/08/2024' },
        { nom: 'Intervention sur Équipement "Vidéo projecteur SN25458"', dateSignalement: '25/05/2024' },
        { nom: 'Intervention sur Équipement "Vidéo projecteur SN25458"', dateSignalement: '25/05/2024' },
        { nom: 'Intervention sur Équipement "Tableau Blanc"', dateSignalement: '13/10/2024' },
      ],
      nombreInterventions: 7,
      defaillancesPage: 1,
      interventionsPage: 1,
    };
  },
  methods: {
    transformerEnBonDeTravail() {
      console.log('Transformer en bon de travail');
    },
    cloturerFicheIntervention() {
      console.log('Clôturer la fiche d\'intervention');
    },
    cloturerIntervention() {
      // Rediriger vers la page de clôture d'intervention sans paramètres
      this.$router.push({ name: 'CloturerIntervention' });
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