import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';  

export const BASE_URL = 'http://localhost:8000';

export default {

  getEquipements() {
    return axios.get(`${API_URL}equipements/`);
  },

  getLieuxHierarchy() {
    return axios.get(`${API_URL}lieux-hierarchy/`);
  },

  getModeleEquipements() {
    return axios.get(`${API_URL}modele-equipements/`);
  },

  getEquipementsVue(){
    return axios.get(`${API_URL}equipements-detail/`);
  },

  getEquipementAffichage(reference) {
    return axios.get(`${API_URL}equipement/${reference}/affichage/`);
  },

  getInterventionAffichage(id) {
    return axios.get(`${API_URL}intervention/${id}/affichage/`);
  },

  getUtilisateurs() {
    return axios.get(`${API_URL}utilisateurs/`);
  },

  createIntervention(interventionData) {
    return axios.post(`${API_URL}interventions/`, interventionData);
  },

  // -----------------------
  getLieux() {
    return axios.get(`${API_URL}lieux/`);
  },

  createLieu(data) {
    return axios.post(`${API_URL}creer-lieu/`, data);
  },

};