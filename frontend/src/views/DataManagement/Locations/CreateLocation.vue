<template>
  <v-app>
    <v-main>
      <v-container>
        <v-form @submit.prevent="submitForm">
  
          <v-text-field
            v-model="formData.nomLieu"
            label="Nom du lieu"
            required
            outlined
            dense
            class="mb-4"
          ></v-text-field>
  
          <v-text-field
            v-model="formData.typeLieu"
            label="Type de lieu"
            required
            outlined
            dense
            class="mb-4"
          ></v-text-field>
  
          <div>
            <p v-if="!lieux_avec_tous || lieux_avec_tous.length === 0">Aucune donnée disponible.</p>
            <v-treeview
              v-else
              :items="lieux_avec_tous"
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
                <span @click="on_click_location(item)">{{ item.nomLieu }}</span> <!-- OnClick ici -->
              </template>
              <template v-slot:label="{ item }">
                <span class="text-caption ml-2">{{ item.typeLieu }}</span>
              </template>
            </v-treeview>
          </div>
          

          <v-row justify="end">
            <v-btn color="secoundary" class="mt-4 rounded" @click="go_back" style="border-radius: 0; margin-right: 35px;" large>
              Annuler
            </v-btn>
            <v-btn type="submit" color="primary" class="mt-4 rounded" style="border-radius: 0 ;margin-right: 35px;" large>
              Ajouter le lieu
            </v-btn>
          </v-row>
        </v-form>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import api from '@/services/api';
import { ref, computed, reactive, onMounted, toRefs } from 'vue';
import { useRouter } from 'vue-router';
import { VTreeview } from 'vuetify/labs/VTreeview';

export default {
  name: 'CreateLocation',
  components: {
    VTreeview,
  },
  setup() {
    const router = useRouter();
    const state = reactive({
      formData: {
        nomLieu: "",
        typeLieu: "",
        lieu: null,
        header: [
          { title: 'Lieu', value: 'lieu.nomLieu', sortable: true, align: 'center' },
        ],
        openNodes: new Set(),
      },
      lieux: [],
    });

    const lieux_avec_tous = computed(() => {
      return [...state.lieux];
    });

    
    const on_click_location = (item) => {
      if (state.formData.lieu && state.formData.lieu.id === item.id) {
     
        state.formData.lieu = null;
      } else {
        
        state.formData.lieu = item; 
      }
    };

    const toggleNode = (item) => {
      if (state.openNodes.has(item.id)) {
        state.openNodes.delete(item.id);
      } else {
        state.openNodes.add(item.id);
      }
    };

    const submitForm = async () => {
      const formData = new FormData();
      formData.append('nomLieu', state.formData.nomLieu);
      formData.append('typeLieu', state.formData.typeLieu);

      if (state.formData.lieu) {
        formData.append('lieuParent', state.formData.lieu.id);
      }

      try {
        const responseLieu = await api.postLieu(formData);
        if (responseLieu.status === 201) {
          console.log('Lieu ajouté avec succès !');
          go_back();
        } else {
          console.log('Erreur lors de l’ajout du lieu.');
        }
      } catch (error) {
        console.error('Erreur lors de la soumission du formulaire:', error);
      }
    };

    const fetchData = async () => {
      try {
        const [lieuRES] = await Promise.all([api.getLieuxHierarchy()]);
        state.lieux = lieuRES.data;
      } catch (error) {
        console.error('Erreur lors du chargement des données :', error);
      }
    };

    const go_back = () => {
      router.go(-1);
    };

    onMounted(() => {
      fetchData();
    });

    return {
      ...toRefs(state),
      submitForm,
      lieux_avec_tous,
      on_click_location,
      toggleNode,
      go_back,
    };
  },
};
</script>