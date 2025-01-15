<template>
  <v-app>
    <v-main>
      <v-container>
        <v-row>
          <v-col cols="12">
            <!-- Bouton pour rediriger vers la page d'ajout d'équipement -->
            <v-btn color="primary" @click="pageCreerFabricant" class="mb-4">
              Aller à l'ajout de fabricant
            </v-btn>

            <!-- Tableau des fabricants -->
            <v-data-table
              :headers="headers"
              :items="fabricants"
              :items-per-page="itemsPerPage"
              :page.sync="page"
              class="elevation-1 rounded-lg"
              @page-count="pageCount = $event"
              :sort-by="['nomFabricant']"
              :sort-desc="[false]"
            >
              <template v-slot:item.serviceApresVente="{ item }">
                <v-chip :color="item.serviceApresVente ? 'green' : 'red'" dark>
                  {{ item.serviceApresVente ? 'Oui' : 'Non' }}
                </v-chip>
              </template>
            </v-data-table>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import api from "@/services/api";
import { ref, reactive, onMounted } from "vue";
import { useRouter } from "vue-router";

export default {
  name: "ListeFabricants",
  setup() {
    const router = useRouter();
    
    // Déclaration des références et des données
    const fabricants = ref([]); // Liste des fabricants
    const page = ref(1); // Page actuelle
    const pageCount = ref(0); // Compteur de pages
    const itemsPerPage = ref(10); // Nombre d'items par page

    // En-têtes du tableau
    const headers = [
      { text: 'Fabricant', value: 'nomFabricant', sortable: true, align: 'center' },
      { text: 'Pays', value: 'paysFabricant', sortable: true, align: 'center' },
      { text: 'Email', value: 'mailFabricant', sortable: true, align: 'center' },
      { text: 'Téléphone', value: 'numTelephoneFabricant', sortable: true, align: 'center' },
      { text: 'Service après-vente', value: 'serviceApresVente', sortable: true, align: 'center' }
    ];

    // Fonction pour récupérer les fabricants
    const getFabricant = async () => {
      try {
        const response = await api.getFabricant(); // Appel à l'API pour récupérer la liste
        if (response && response.data) {
          fabricants.value = response.data; // Assignation des fabricants récupérés
        }
      } catch (error) {
        console.error("Erreur lors de la récupération des fabricants:", error);
      }
    };

    // Récupérer les fabricants lors du montage du composant
    onMounted(() => {
      getFabricant();
    });

    // Fonction pour ouvrir la page d'ajout d'équipement (rediriger vers une autre page)
    const pageCreerFabricant = () => {
      router.push('/creer-fabricants'); // Remplace 'AjoutEquipement' par le nom de ta route
    };

    return {
      fabricants,
      headers,
      itemsPerPage,
      page,
      pageCount,
      pageCreerFabricant,
    };
  }
};
</script>

<style scoped>
.v-btn {
  margin: 0 5px;
}
</style>
