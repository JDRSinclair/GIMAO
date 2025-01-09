<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <v-col cols="4">
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Structure des lieux</v-card-title>
              <v-divider></v-divider>
              <ExplorateurLieux
             :lieux="lieux" @select-lieu="gererLieuSelectione" />
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
              :items="equipementsFiltres"
              :items-per-page="itemsParPage"
              :page.sync="page"
              item-value="name"
              class="elevation-1 rounded-lg"
              @page-count="nbPage = $event"
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
                :length="nbPage"
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
import ExplorateurLieux from '@/components/ExplorateurLieux.vue';
import '@/assets/css/global.css';

export default {
  name: 'Equipements',
  components: {
    NavigationDrawer,
    TopNavBar,
    ExplorateurLieux
  ,
  },
  /**
   * Setup de la page des équipements.
   * 
   * Cette fonction est appelée une seule fois, au moment de l'instanciation
   * du composant. Elle renvoie un objet qui sera injecté dans le composant
   * comme propriétés.
   * 
   * Les propriétés et les méthodes suivantes sont mises à disposition :
   * 
   * - typesEquipements : un tableau des types d'équipements (par exemple, "Tous", "Type 1", "Type 2", etc.)
   * - headers : un tableau des en-têtes de la table des équipements
   * - equipements : un tableau des équipements (au format { id, nom, lieu, etat })
   * - lieux : un tableau des lieux dans l'entreprise (au format { id, nomLieu, children: [{ id, nomLieu, children: [ ... ] }] })
   * - lieuSelectione : la valeur du lieu selectionné par l'utilisateur
   * - gererLieuSelectione : une fonction qui met à jour la valeur de lieuSelectione
   *   en fonction du lieu qui a été selectionné dans l'arbre
   * - equipementsFiltres : un computed qui filtre les équipements en fonction
   *   du lieu selectionné
   * - page : la page actuelle de la pagination
   * - nbPage : le nombre de pages de la pagination
   * - itemsParPage : le nombre d'éléments par page
   * - ouvrirPageAjoutEquipement : une fonction qui ouvre la page d'ajout d'un équipement
   * - ouvrirPageVoirEquipement : une fonction qui ouvre la page de visualisation
   *   d'un équipement en fonction de son ID
   * 
   */
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
    const lieuSelectione = ref(null);

    const page = ref(1);

    const nbPage = ref(0);
    
    const itemsParPage = ref(5);

    /**
     * Ouvre la page d'ajout d'un équipement.
     */
    const ouvrirPageAjoutEquipement = () => {
      router.push({ name: 'AjouterEquipement' });
    };

    /**
     * Ouvre la page de visualisation d'un équipement.
     * 
     * @param {number} id - L'ID de l'équipement à visualiser.
     */
    const ouvrirPageVoirEquipement = (id) => {
      if (!id) {
        console.error('ID is missing');
        return;
      }
      router.push({ name: 'VisualiserEquipement', params: { id } });
    };

    /**
     * Filtre les équipements en fonction du lieu selectionné.
     */
    const equipementsFiltres = computed(() => {
      if (!lieuSelectione.value) {
        return equipements.value;
      }
      return equipements.value.filter(e => e.lieu === lieuSelectione.value);
    });

    /**
     * Met à jour la valeur de lieuSelectione en fonction du lieu 
     * qui a été selectionné dans l'arbre.
     * 
     * @param {Object} lieu - Le lieu qui a été selectionné.
     */
    const gererLieuSelectione = (lieu) => {
      lieuSelectione.value = lieu.nomLieu;
    };
    
    return {
      typesEquipements,
      headers,
      equipements,
      lieux,
      lieuSelectione,
      gererLieuSelectione,
      equipementsFiltres,
      page,
      nbPage,
      itemsParPage,
      ouvrirPageAjoutEquipement,
      ouvrirPageVoirEquipement,
    };
  }
};
</script>

<style scoped>
.v-data-table tr:hover {
  background-color: #e6f2ff; 
  transition: background-color 0.3s ease;
}

.v-data-table tr:hover td {
  color: #0056b3;
}
</style>