<template>
  <v-container>
    <v-row class="mb-4">
      <!-- Search Bar -->
      <v-col cols="9">
        <v-text-field
          v-model="search_query"
          label="Rechercher un modele d'equipement"
          prepend-icon="mdi-magnify"
          clearable
        ></v-text-field>
      </v-col>
      <v-col cols="3" class="align-center">
        <v-btn 
          color="primary"
          @click="$router.push('/CreateModelEquipment')"
          class="ml-2"
          height="50%"
        >
          Creer un modele d'equipement
        </v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col 
        v-for="model_equipment in filtered_model_equipment" 
        :key="model_equipment.id" 
        cols="12" 
        sm="6" 
        md="4"
      >
        <v-card @click="go_to_model_equipment_details(model_equipment.id)">
          <v-card-title>{{ model_equipment.nomModeleEquipement }}</v-card-title>
          <v-card-text>
            <p>Fabricant : {{ model_equipment.fabricant }}</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from '@/services/api';

export default {
  name: 'ModelEquipmentList',
  data() {
    return {
      model_equipments: [],
      search_query: ''
    };
  },
  computed: {
    filtered_model_equipment() {
      if (!this.search_query) {
        return this.model_equipments;
      }
      const searchLower = this.search_query.toLowerCase();
      return this.model_equipments.filter(model_equipment => 
        model_equipment.nomModeleEquipement.toLowerCase().includes(searchLower) ||
        model_equipment.ville.toLowerCase().includes(searchLower) ||
        model_equipment.paysmodeleEquipement.toLowerCase().includes(searchLower)
      );
    }
  },
  methods: {
    async fetch_model_equipments() {
      try {
        const response = await api.getModeleEquipements();
        this.model_equipments = response.data;
      } catch (error) {
        console.error('Error fetching model equipments:', error);
      }
    },
    go_to_model_equipment_details(id) {
      this.$router.push(`/ModelEquipmentDetail/${id}`);
    }
  },
  created() {
    this.fetch_model_equipments();
  }
}
</script>