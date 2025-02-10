<template>
  <v-app>
    <v-main>
      <v-container>
        <h1 class="mb-4">Creer un Equipement</h1>
        <v-form @submit.prevent="submit_form">
          <v-text-field
            v-model="form_data.reference"
            label="Référence"
            required
            outlined
            dense
            class="mb-4"
          ></v-text-field>

          <v-text-field
            v-model="form_data.designation"
            label="Désignation"
            required
            outlined
            dense
            class="mb-4"
          ></v-text-field>

          <v-menu
            ref="menu"
            v-model="date_service_start_menu"
            :close-on-content-click="false"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="form_data.dateMiseEnService"
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
              v-model="form_data.dateMiseEnService"
              @input="date_service_start_menu = false"
              no-title
              scrollable
            >
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="date_service_start_menu = false">
                Cancel
              </v-btn>
              <v-btn text color="primary" @click="$refs.menu.save(form_data.dateMiseEnService)">
                OK
              </v-btn>
            </v-date-picker>
          </v-menu>

          <v-text-field
            v-model="form_data.purchase_price"
            label="Prix Achat"
            type="number"
            outlined
            dense
            class="mb-4"
          ></v-text-field>

          <v-file-input
            v-model="form_data.equipment_image_link"
            label="Image de l'Equipement"
            outlined
            dense
            class="mb-4"
          ></v-file-input>

          <v-text-field
            v-model="form_data.maintenance_interval_days"
            label="Intervalle de la maintenance (jours)"
            type="number"
            outlined
            dense
            class="mb-4"
          ></v-text-field>

          <v-switch
            v-model="form_data.sliding_preventive"
            label="Intervention Préventive Glissante"
            class="mb-4"
          ></v-switch>

          <v-select
            v-model="form_data.equipment_model"
            :items="equipment_models"
            item-text="nomModeleEquipement"
            item-title="nomModeleEquipement"
            item-value="id"
            label="Modele de l'Equipement"
            outlined
            dense
            class="mb-4"
          ></v-select>

          <v-select
            v-model="form_data.supplier"
            :items="suppliers"
            item-text="nomFournisseur"
            item-title="nomFournisseur"
            item-value="id"
            label="Fournisseur"
            outlined
            dense
            class="mb-4"
          ></v-select>

          <div>
            <h3 class="mb-2">Selectionner un lieu</h3>
            <p v-if="!locations_with_all || locations_with_all.length === 0">Pas de données disponibles.</p>
            <v-treeview
              v-else
              :items="locations_with_all"
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
                  @click.stop="toggle_node(item)"
                  :class="{ 'rotate-icon': open }"
                >
                  {{ open ? 'mdi-triangle-down' : 'mdi-triangle-right' }}
                </v-icon>
                <span v-else class="tree-icon-placeholder"></span>
                <span @click="on_click_location(item)">{{ item.nomLieu }}</span>
              </template>
              <template v-slot:label="{ item }">
                <span class="text-caption ml-2">{{ item.typeLieu }}</span>
              </template>
            </v-treeview>
          </div>

          <div class="mt-4">
            <h3 class="mb-2">Consommables Associés</h3>
            <v-select
              v-model="selected_consumables"
              :items="consumables"
              item-text="designation"
              item-title="designation"
              item-value="id"
              label="Selectionner le consommable"
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
            <v-btn type="submit" color="primary" class="mt-4 rounded" style="border-radius: 0; margin-right: 35px;" large>
              Creer un Equipement
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
  name: 'CreateEquipment',
  components: {
    VTreeview,
  },
  setup() {
    const router = useRouter();
    const state = reactive({
      form_data: {
        reference: "",
        designation: "",
        dateMiseEnService: new Date().toISOString().substr(0, 10),
        purchase_price: null,
        equipment_image_link: null,
        sliding_preventive: false,
        maintenance_interval_days: null,
        equipment_creator: 1, 
        location: null,
        equipment_model: null,
        supplier: null,
      },
      locations: [],
      equipment_models: [],
      suppliers: [],
      consumables: [],
      selected_consumables: [],
      open_nodes: new Set(),
      date_service_start_menu: false,
    });

    const locations_with_all = computed(() => {
      return [...state.locations];
    });

    const on_click_location = (item) => {
      if (state.form_data.location && state.form_data.location.id === item.id) {
        state.form_data.location = null;
      } else {
        state.form_data.location = item;
      }
    };

    const toggle_node = (item) => {
      if (state.open_nodes.has(item.id)) {
        state.open_nodes.delete(item.id);
      } else {
        state.open_nodes.add(item.id);
      }
    };

    const submit_form = async () => {
      try {
        // Check if the equipment already exists
        const checkResponse = await api.getEquipement(state.form_data.reference);
        if (checkResponse.status === 200) {
          console.error('An equipment with this reference already exists.');
          // Display an error message to the user
          return;
        }

        // If the equipment does not exist, proceed with creation
        const equipmentResponse = await api.postEquipement(state.form_data);
        if (equipmentResponse.status === 201) {
          console.log('Equipment added successfully!');
          
          // Associate consumables with the equipment
          for (const consumableId of state.selected_consumables) {
            await api.postConstituer({
              equipement: state.form_data.reference,
              consommable: consumableId
            });
          }
          
          go_back();
        } else {
          console.log('Error adding equipment.');
        }
      } catch (error) {
        console.error('Error submitting the form:', error);
      }
    };

    const fetchData = async () => {
      try {
        const [locationsRes, modelsRes, suppliersRes, consumablesRes] = await Promise.all([
          api.getLieuxHierarchy(),
          api.getModeleEquipements(),
          api.getFournisseurs(),
          api.getConsommables()
        ]);
        state.locations = locationsRes.data;
        state.equipment_models = modelsRes.data;
        state.suppliers = suppliersRes.data;
        state.consumables = consumablesRes.data;
      } catch (error) {
        console.error('Error loading data:', error);
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
      submit_form,
      locations_with_all,
      on_click_location,
      toggle_node,
      go_back,
    };
  },
};
</script>