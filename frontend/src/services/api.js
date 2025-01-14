import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';  

export const BASE_URL = 'http://localhost:8000';

export default {

  getEquipements() {
    return axios.get(`${API_URL}equipements/`);
  },

  getInterventions() {
    return axios.get(`${API_URL}interventions/`);
  },

  getLieux() {
    return axios.get(`${API_URL}lieux-hierarchy/`);
  },

  getModeleEquipements() {
    return axios.get(`${API_URL}modele-equipements/`);
  },

  getEquipementsVue(){
    return axios.get(`${API_URL}equipements-detail/`);
  },

  getEquipement(reference) {
    return axios.get(`${API_URL}equipements/${reference}/affichage/`);
  },
};