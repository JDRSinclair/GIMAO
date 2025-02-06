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
              </v-card-title>
              <v-divider></v-divider>
              <v-data-table
                :headers="defaillancesHeaders"
                :items="defaillances"
                :items-per-page="5"
                :page.sync="defaillancesPage"
                item-value="id"
                class="elevation-1 rounded-lg"
                hide-default-footer
                @click:row="(event, {item}) => ouvrirAfficherDefaillance(item.id)"
              >
                <template v-slot:item.niveau="{ item }">
                  <v-chip :color="getNiveauColor(item.niveau)" dark>
                    {{ item.niveau }}
                  </v-chip>
                </template>
              </v-data-table>

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
              </v-card-title>
              <v-divider></v-divider>
              <v-data-table
                :headers="interventionsHeaders"
                :items="interventions"
                :items-per-page="5"
                :page.sync="interventionsPage"
                item-value="id"
                class="elevation-1 rounded-lg"
                hide-default-footer
                @click:row="(event, {item}) => ouvrirAfficherIntervention(item.id)"
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
import { useRouter } from 'vue-router';
import NavigationDrawer from '@/components/BarreNavigation.vue';
import TopNavBar from "@/components/BarreNavigationHaut.vue";
import '@/assets/css/global.css';
import api from '@/services/api';

export default {
  components: {
    NavigationDrawer,
    TopNavBar,
  },

  setup() {
    const router = useRouter();

    const ouvrirAfficherDefaillance = (id) => {
      router.push({ name: 'AfficherDefaillance', params: { id: id } });
    };

    const ouvrirAfficherIntervention = (id) => {
      router.push({ name: 'AfficherIntervention', params: { id: id } });
    };

    return {
      ouvrirAfficherDefaillance,
      ouvrirAfficherIntervention
    };
  },

  data() {
    return {
      menuItems: [
        { name: 'Tableau de bord', icon: require('@/assets/images/Graphe.svg') },
        { name: 'Equipements', icon: require('@/assets/images/Outils.svg') },
        { name: 'Maintenances', icon: require('@/assets/images/Maintenance.svg') },
        { name: 'Techniciens', icon: require('@/assets/images/Techniciens.svg') },
      ],
      defaillancesHeaders: [
        { title: 'Commentaire', value: 'commentaireDefaillance' },
        { title: 'Niveau', value: 'niveau' },
        { title: 'Équipement', value: 'equipement' },
      ],
      defaillances: [],
      interventionsHeaders: [
        { title: 'Nom', value: 'nomIntervention' },
        { title: 'Date d\'assignation', value: 'dateAssignation' },
        { title: 'Temps estimé', value: 'tempsEstime' },
      ],
      interventions: [],
      nombreInterventions: 0,
      defaillancesPage: 1,
      interventionsPage: 1,
    };
  },

  methods: {
    handleItemSelected(item) {
      console.log('Selected item:', item);
    },

    formatDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      return date.toLocaleDateString('fr-FR', { day: '2-digit', month: '2-digit', year: 'numeric' });
    },

    async fetchDefaillances() {
      try {
        const response = await api.getDefaillances();
        this.defaillances = response.data.filter(defaillance => defaillance.dateTraitementDefaillance === null);
      } catch (error) {
        console.error('Erreur lors de la récupération des défaillances:', error);
      }
    },

    getNiveauColor(niveau) {
      switch (niveau) {
        case 'Critique':
          return 'red';
        case 'Majeur':
          return 'orange';
        default:
          return 'green';
      }
    },

    async fetchInterventions() {
      try {
        const response = await api.getInterventions();
        this.interventions = response.data
          // .filter(intervention => intervention.dateFinIntervention !== null)
          .map(intervention => ({
            ...intervention,
            dateAssignation: this.formatDate(intervention.dateAssignation)
          }));
        this.nombreInterventions = this.interventions.length; // Modifié ici
      } catch (error) {
        console.error('Erreur lors de la récupération des interventions:', error);
      }
    },
  },

  created() {
    this.fetchDefaillances();
    this.fetchInterventions();
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