<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <v-col cols="4">
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Structure des lieux</v-card-title>
              <v-divider></v-divider>
              <LieuxExplorer :lieux="lieux" @select-lieu="handleLieuSelected" />
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
          <v-col cols="8">
            <v-btn
              color="primary"
              @click="ouvrirPageAjoutEquipement"
              class="mb-4"
            >
              Aller à l'ajout d'équipement
            </v-btn>
            <v-data-table
              :headers="headers"
              :items="filteredEquipements"
              :items-per-page="itemsPerPage"
              :page.sync="page"
              item-value="name"
              class="elevation-1 rounded-lg"
              @page-count="pageCount = $event"
              hover
            >
              <template v-slot:item="{ item }">
                <tr @click="ouvrirPageVoirEquipement(item.equipement)" style="cursor: pointer;">
                  <td>{{ item.equipement }}</td>
                  <td>{{ item.lieu }}</td>
                  <td>{{ item.etat }}</td>
                </tr>
              </template>
            </v-data-table>
            <div class="text-center pt-2">
              <v-pagination
                v-model="page"
                :length="pageCount"
              ></v-pagination>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import NavigationDrawer from '@/components/BarreNavigation.vue';
import TopNavBar from "@/components/BarreNavigationHaut.vue";
import LieuxExplorer from '@/components/LieuxExplorer.vue';
import '@/assets/css/global.css';

export default {
  name: 'Equipements',
  components: {
    NavigationDrawer,
    TopNavBar,
    LieuxExplorer,
  },
  setup() {
    const router = useRouter();

    const typesEquipements = ref(["Tous", "Type 1", "Type 2", "Type 3", "Type 4"]);
    const headers = ref([
      { text: "Équipement", value: "equipement", align: "start" },
      { text: "Lieu", value: "lieu" },
      { text: "État", value: "etat" },
    ]);
    const equipements = ref([
      { equipement: "Équipement 1", lieu: "Ligne d'Assemblage 1", etat: "À l'arrêt" },
      { equipement: "Équipement 2", lieu: "Ligne d'Assemblage 1", etat: "Rebuté" },
      { equipement: "Équipement 3", lieu: "Ligne d'Assemblage 2", etat: "Fonctionnel" },
      { equipement: "Équipement 4", lieu: "Poste de Soudure", etat: "Fonctionnel" },
      { equipement: "Équipement 5", lieu: "Zone de Test", etat: "Fonctionnel" },
      { equipement: "Équipement 6", lieu: "Unité de Moulage", etat: "À l'arrêt" },
      { equipement: "Équipement 7", lieu: "Unité de Peinture", etat: "Fonctionnel" },
      { equipement: "Équipement 8", lieu: "Zone d'Emballage", etat: "Fonctionnel" },
    ]);
    const lieux = ref([
      {
        id: 1,
        nomLieu: 'Bâtiment Principal',
        children: [
          {
            id: 5,
            nomLieu: 'Zone de Production A',
            children: [
              { id: 9, nomLieu: 'Ligne d\'Assemblage 1' },
              { id: 10, nomLieu: 'Ligne d\'Assemblage 2' },
              { id: 11, nomLieu: 'Poste de Soudure' },
              { id: 12, nomLieu: 'Zone de Test' },
            ]
          },
          {
            id: 6,
            nomLieu: 'Zone de Production B',
            children: [
              { id: 13, nomLieu: 'Unité de Moulage' },
              { id: 14, nomLieu: 'Unité de Peinture' },
              { id: 15, nomLieu: 'Zone d\'Emballage' },
            ]
          },
          { id: 7, nomLieu: 'Atelier de Maintenance' },
          { id: 8, nomLieu: 'Salle de Contrôle Qualité' },
        ]
      },
    ]);
    const selectedLieu = ref(null);
    const page = ref(1);
    const pageCount = ref(0);
    const itemsPerPage = ref(5);

    const ouvrirPageAjoutEquipement = () => {
      router.push({ name: 'AjouterEquipement' });
    };

    const ouvrirPageVoirEquipement = (id) => {
      if (!id) {
        console.error('ID is missing');
        return;
      }
      router.push({ name: 'VisualiserEquipement', params: { id } });
    };

    const filteredEquipements = computed(() => {
      if (!selectedLieu.value) {
        return equipements.value;
      }
      return equipements.value.filter(e => e.lieu === selectedLieu.value);
    });

    const handleLieuSelected = (lieu) => {
      selectedLieu.value = lieu.nomLieu;
    };

    return {
      typesEquipements,
      headers,
      equipements,
      lieux,
      selectedLieu,
      handleLieuSelected,
      filteredEquipements,
      page,
      pageCount,
      itemsPerPage,
      ouvrirPageAjoutEquipement,
      ouvrirPageVoirEquipement,
    };
  }
};
</script>

<style scoped>
/* Effet de survol personnalisé */
.v-data-table tr:hover {
  background-color: #e6f2ff; /* Fond bleu clair au survol */
  transition: background-color 0.3s ease; /* Transition fluide */
}

.v-data-table tr:hover td {
  color: #0056b3; /* Couleur du texte en bleu foncé au survol */
}
</style>