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
                  <span @click="onClickLieu(item)">{{ item.nomLieu }}</span> <!-- OnClick ici -->
                </template>
                <template v-slot:label="{ item }">
                  <span class="text-caption ml-2">{{ item.typeLieu }}</span>
                </template>
              </v-treeview>
            </div>
            

            <v-row justify="end">
              <v-btn color="secoundary" class="mt-4 rounded" @click="goBack" style="border-radius: 0; margin-right: 35px;" large>
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
    name: 'AjouterLieu',
    components: {
      VTreeview,
    },
    setup() {
      const router = useRouter();
      const state = reactive({
        formData: {
          nomLieu: "",
          typeLieu: "",
          lieu: null, // Nous allons lier cette variable à l'objet sélectionné
          header: [
            { title: 'Lieu', value: 'lieu.nomLieu', sortable: true, align: 'center' },
          ],
          openNodes: new Set(),
        },
        lieux: [],
      });

      const lieuxAvecTous = computed(() => {
        return [...state.lieux];
      });

      // Fonction de gestion du clic sur un élément de l'arborescence
      const onClickLieu = (item) => {
        if (state.formData.lieu && state.formData.lieu.id === item.id) {
          // Si le même élément est cliqué deux fois d'affilée, on réinitialise `lieu` à null
          state.formData.lieu = null;
        } else {
          // Sinon, on sélectionne le nouveau lieu
          state.formData.lieu = item; // Mise à jour de formData.lieu
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

        // Vérifie si un lieu parent est sélectionné et l'ajoute
        if (state.formData.lieu) {
          formData.append('lieuParent', state.formData.lieu.id);
        }

        try {
          const responseLieu = await api.createLieu(formData);
          if (responseLieu.status === 201) {
            console.log('Lieu ajouté avec succès !');
            goBack();
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

      const goBack = () => {
        router.go(-1);
      };

      onMounted(() => {
        fetchData();
      });

      return {
        ...toRefs(state),
        submitForm,
        lieuxAvecTous,
        onClickLieu,
        toggleNode,
        goBack,
      };
    },
  };
</script>
