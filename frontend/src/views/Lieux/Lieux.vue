<template>
    <v-container>
      <v-row>
        <!-- Structure des lieux -->
        <v-card elevation="1" class="rounded-lg pa-4 mb-4" style="min-width: 800px; width: 100%; min-height: 400px;">
          <v-card-title class="font-weight-bold text-uppercase text-primary d-flex justify-space-between align-center">
            <span>Liste des lieux</span>
            <v-btn 
              color="primary" 
              @click="goToAddLieuPage"
              small
              class="ml-4"
            >
              Ajouter un lieu
            </v-btn>
          </v-card-title>
          <v-divider></v-divider>
          <div>
            <p v-if="!lieuxAvecTous || lieuxAvecTous.length === 0">Aucune donnée disponible.</p>
            <v-treeview
              v-else
              :items="lieuxAvecTous"
              item-key="id"
              :open-on-click="false"
              item-text="nomLieu"
              rounded
              hoverable
              activatable
              dense
            >
              <template v-slot:prepend="{ item, open }">
                <v-icon
                  v-if="item.children && item.children.length > 0 && item.nomLieu !== 'Tous'"
                  @click.stop="toggleNode(item)"
                  :class="{ 'rotate-icon': open }"
                >
                  {{ open ? 'mdi-triangle-down' : 'mdi-triangle-right' }}
                </v-icon>
                <span v-else class="tree-icon-placeholder"></span>
                {{ item.nomLieu }}
              </template>
              <template v-slot:label="{ item }">
                <span class="text-caption ml-2">{{ item.typeLieu }}</span>
              </template>
            </v-treeview>
          </div>
        </v-card>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import { ref, computed, onMounted, reactive, toRefs } from 'vue';
  import { useRouter } from 'vue-router';
  import { VTreeview } from 'vuetify/labs/VTreeview';
  import api from '@/services/api';
  
  export default {
    name: 'Lieux',
    components: {
      VTreeview,
    },
    setup() {
      const router = useRouter();
  
      const state = reactive({
        lieux: [],
        selectedLieu: null,
        header: [
          { title: 'Lieu', value: 'lieu.nomLieu', sortable: true, align: 'center' },
        ],
        openNodes: new Set(),
      });
  
      const fetchData = async () => {
        try {
          const [ lieuxRes] = await Promise.all([
            api.getLieuxHierarchy(),
          ]);
          state.lieux = lieuxRes.data;
        } catch (error) {
          console.error('Erreur lors de la récupération des données:', error);
        }
      };
  
      const lieuxAvecTous = computed(() => {
        return state.lieux;
      });
  
      const onSelectLieu = (items) => {
        if (items.length > 0) {
          const selectedItem = findItem(lieuxAvecTous.value, items[0]);
          if (selectedItem) {
            state.selectedLieu = selectedItem.nomLieu;
          }
        }
      };
  
      const findItem = (items, id) => {
        for (const item of items) {
          if (item.id === id) {
            return item;
          }
          if (item.children) {
            const found = findItem(item.children, id);
            if (found) {
              return found;
            }
          }
        }
        return null;
      };
  
      const toggleNode = (item) => {
        if (state.openNodes.has(item.id)) {
          state.openNodes.delete(item.id);
        } else {
          state.openNodes.add(item.id);
        }
      };
  
      const goToAddLieuPage = () => {
        router.push('/creerLieu'); 
      };
  
      onMounted(fetchData);
  
      return {
        ...toRefs(state),
        lieuxAvecTous,
        onSelectLieu,
        toggleNode,
        goToAddLieuPage,
      };
    }
  };
  </script>
  
  <style scoped>
  .pa-4 {
    padding: 32px;
  }
  .rotate-icon {
    transform: rotate(90deg);
  }
  .tree-icon-placeholder {
    width: 20px;
    height: 20px;
  }
  </style>
  