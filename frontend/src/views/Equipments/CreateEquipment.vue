<template>
  <v-app>
    <v-main>
      <v-container>
        <h1 class="mb-4">Créer un équipement</h1>
        <v-form @submit.prevent="submitForm">
          <v-text-field
            v-model="formData.reference"
            label="Référence"
            required
            outlined
            dense
            class="mb-4"
          ></v-text-field>

          <v-text-field
            v-model="formData.designation"
            label="Désignation"
            required
            outlined
            dense
            class="mb-4"
          ></v-text-field>

          <v-menu
            ref="menu"
            v-model="dateMiseEnServiceMenu"
            :close-on-content-click="false"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="formData.dateMiseEnService"
                label="Date de mise en service"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
                outlined
                dense
                class="mb-4"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="formData.dateMiseEnService"
              @input="dateMiseEnServiceMenu = false"
              no-title
              scrollable
            >
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="dateMiseEnServiceMenu = false">
                Annuler
              </v-btn>
              <v-btn text color="primary" @click="$refs.menu.save(formData.dateMiseEnService)">
                OK
              </v-btn>
            </v-date-picker>
          </v-menu>

          <v-text-field
            v-model="formData.prixAchat"
            label="Prix d'achat"
            type="number"
            outlined
            dense
            class="mb-4"
          ></v-text-field>

          <v-file-input
            v-model="formData.lienImageEquipement"
            label="Image de l'équipement"
            outlined
            dense
            class="mb-4"
          ></v-file-input>

          

          <v-text-field
            v-model="formData.joursIntervalleMaintenance"
            label="Jours d'intervalle de maintenance"
            type="number"
            outlined
            dense
            class="mb-4"
          ></v-text-field>

          <v-switch
            v-model="formData.preventifGlissant"
            label="Préventif glissant"
            class="mb-4"
          ></v-switch>

          <v-select
            v-model="formData.modeleEquipement"
            :items="modelesEquipement"
            item-text="nomModeleEquipement"
            item-title="nomModeleEquipement"
            item-value="id"
            label="Modèle d'équipement"
            outlined
            dense
            class="mb-4"
          ></v-select>

          <v-select
            v-model="formData.fournisseur"
            :items="fournisseurs"
            item-text="nomFournisseur"
            item-title="nomFournisseur"
            item-value="id"
            label="Fournisseur"
            outlined
            dense
            class="mb-4"
          ></v-select>

          <div>
            <h3 class="mb-2">Sélectionner un lieu</h3>
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
                <span @click="onClickLieu(item)">{{ item.nomLieu }}</span>
              </template>
              <template v-slot:label="{ item }">
                <span class="text-caption ml-2">{{ item.typeLieu }}</span>
              </template>
            </v-treeview>
          </div>

          <div class="mt-4">
            <h3 class="mb-2">Consommables associés</h3>
            <v-select
              v-model="selectedConsommables"
              :items="consommables"
              item-text="designation"
              item-title="designation"
              item-value="id"
              label="Sélectionner les consommables"
              multiple
              chips
              outlined
              dense
            ></v-select>
          </div>

          <v-row justify="end">
            <v-btn color="secondary" class="mt-4 rounded" @click="go_back" style="border-radius: 0; margin-right: 35px;" large>
              Annuler
            </v-btn>
            <v-btn type="submit" color="primary" class="mt-4 rounded" style="border-radius: 0 ;margin-right: 35px;" large>
              Créer l'équipement
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
  name: 'CreerEquipement',
  components: {
    VTreeview,
  },
  setup() {
    const router = useRouter();
    const state = reactive({
      formData: {
        reference: "",
        designation: "",
        dateMiseEnService: new Date().toISOString().substr(0, 10),
        prixAchat: null,
        lienImageEquipement: null,
        preventifGlissant: false,
        joursIntervalleMaintenance: null,
        createurEquipement: 1, // Vous devrez peut-être ajuster cela en fonction de l'utilisateur connecté
        lieu: null,
        modeleEquipement: null,
        fournisseur: null,
      },
      lieux: [],
      modelesEquipement: [],
      fournisseurs: [],
      consommables: [],
      selectedConsommables: [],
      openNodes: new Set(),
      dateMiseEnServiceMenu: false,
    });

    const lieuxAvecTous = computed(() => {
      return [...state.lieux];
    });

    const onClickLieu = (item) => {
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
      try {
        // Vérifier si l'équipement existe déjà
        const checkResponse = await api.getEquipement(state.formData.reference);
        if (checkResponse.status === 200) {
          console.error('Un équipement avec cette référence existe déjà.');
          // Afficher un message d'erreur à l'utilisateur
          return;
        }

        // Si l'équipement n'existe pas, procéder à la création
        const equipementResponse = await api.postEquipement(state.formData);
        if (equipementResponse.status === 201) {
          console.log('Équipement ajouté avec succès !');
          
          // Associer les consommables à l'équipement
          for (const consommableId of state.selectedConsommables) {
            await api.postConstituer({
              equipement: state.formData.reference,
              consommable: consommableId
            });
          }
          
          go_back();
        } else {
          console.log('Erreur lors de l\'ajout de l\'équipement.');
        }
      } catch (error) {
        console.error('Erreur lors de la soumission du formulaire:', error);
      }
    };

    const fetchData = async () => {
      try {
        const [lieuxRes, modelesRes, fournisseursRes, consommablesRes] = await Promise.all([
          api.getLieuxHierarchy(),
          api.getModeleEquipements(),
          api.getFournisseurs(),
          api.getConsommables()
        ]);
        state.lieux = lieuxRes.data;
        state.modelesEquipement = modelesRes.data;
        state.fournisseurs = fournisseursRes.data;
        state.consommables = consommablesRes.data;
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
      lieuxAvecTous,
      onClickLieu,
      toggleNode,
      go_back,
    };
  },
};
</script>