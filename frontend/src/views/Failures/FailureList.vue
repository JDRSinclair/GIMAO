<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="defaillances"
      :items-per-page="10"
      class="elevation-1"
      @click:row="(event, {item}) => ouvrirAfficherDefaillance(item.id)"
    >
      <template v-slot:item.traite="{ item }">
        <v-chip :color="item.dateTraitementDefaillance ? 'green' : 'red'" dark>
          {{ item.dateTraitementDefaillance ? 'Oui' : 'Non' }}
        </v-chip>
      </template>
      <template v-slot:item.niveau="{ item }">
        <v-chip :color="getNiveauColor(item.niveau)" dark>
          {{ item.niveau }}
        </v-chip>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/services/api';

export default {
  name: 'ListeDefaillances',
  setup() {
    const router = useRouter();
    const defaillances = ref([]);
    const headers = [
      { 
        title: 'Commentaire', 
        align: 'start',  
        sortable: true, 
        value: 'commentaireDefaillance' 
      },
      { 
        title: 'Traitée', 
        align: 'center', 
        sortable: true, 
        value: 'traite' 
      },
      { 
        title: 'Niveau', 
        align: 'center', 
        sortable: true, 
        value: 'niveau' 
      },
      { 
        title: 'Équipement', 
        align: 'center', 
        sortable: false, 
        value: 'equipement' 
      },
    ];

    const fetchDefaillances = async () => {
      try {
        const response = await api.getDefaillances();
        defaillances.value = response.data;
      } catch (error) {
        console.error("Erreur lors de la récupération des défaillances:", error);
      }
    };

    const ouvrirAfficherDefaillance = (id) => {
      router.push({ name: 'FailureDetail', params: { id: id } });
    };


    const getNiveauColor = (niveau) => {
      switch (niveau) {
        case 'Critique':
          return 'red';
        case 'Majeur':
          return 'orange';
        default:
          return 'green';
      }
    };

    onMounted(fetchDefaillances);

    return {
      defaillances,
      headers,
      getNiveauColor,
      ouvrirAfficherDefaillance,
    };
  },
}
</script>