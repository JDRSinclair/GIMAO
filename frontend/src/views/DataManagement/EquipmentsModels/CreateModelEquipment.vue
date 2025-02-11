<template>
    <v-app>
      <v-main>
        <v-container>
          <v-form @submit.prevent="submit_form">
    
            <v-text-field
              v-model="form_data.location_name"
              label="Nom du modéle d'équipement"
              required
              outlined
              dense
              class="mb-4"
            ></v-text-field>
    
            <v-text-field
              v-model="form_data.location_type"
              label="Fabricant"
              required
              outlined
              dense
              class="mb-4"
            ></v-text-field>
    
            
            
            <v-row justify="end">
              <v-btn color="secondary" class="mt-4 rounded" @click="go_back" style="border-radius: 0; margin-right: 35px;" large>
                Annuler
              </v-btn>
              <v-btn type="submit" color="primary" class="mt-4 rounded" style="border-radius: 0 ;margin-right: 35px;" large>
                Ajouter un modele d'équipement
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
        form_data: {
          location_name: "",
          location_type: "",
          location: null,
          header: [
            { title: 'Location', value: 'location.nomLieu', sortable: true, align: 'center' },
          ],
          open_nodes: new Set(),
        },
        locations: [],
      });
  
      const places_with_all = computed(() => {
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
        const form_data = new FormData();
        form_data.append('nomModeleEquipement', state.form_data.location_name);
        form_data.append('fabricant', state.form_data.location_type);
  
        if (state.form_data.location) {
          form_data.append('lieuParent', state.form_data.location.id);
        }
  
        try {
          const responseLieu = await api.postLieu(form_data);
          if (responseLieu.status === 201) {
            console.log('Location added successfully!');
            go_back();
          } else {
            console.log('Error adding location.');
          }
        } catch (error) {
          console.error('Error submitting the form:', error);
        }
      };
  
      const fetch_data = async () => {
        try {
          const [locationRES] = await Promise.all([api.getLieuxHierarchy()]);
          state.locations = locationRES.data;
        } catch (error) {
          console.error('Error loading data:', error);
        }
      };
  
      const go_back = () => {
        router.go(-1);
      };
  
      onMounted(() => {
        fetch_data();
      });
  
      return {
        ...toRefs(state),
        submit_form,
        places_with_all,
        on_click_location,
        toggle_node,
        go_back,
      };
    },
  };
  </script>