import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';  

export default {

  getEquipements() {
    return axios.get(`${API_URL}equipements/`);
  },

  getLieux() {
    return axios.get(`${API_URL}lieux-hierarchy/`);
  },

  getModeleEquipements() {
    return axios.get(`${API_URL}modeleequipements/`);
  },

  getFournisseurs() {
    return axios.get(`${API_URL}fournisseurs/`);
  },

  getUsers() {
    return axios.get(`${API_URL}users/`);
  },
  
  getDocumentationTech() {
    return axios.get(`${API_URL}documentstechniques/`);
  },

  getDernierDocumentationTech() {
    return axios.get(`${API_URL}dernier-document-technique/`);
  },

  createEquipement(data) {
    return axios.post(`${API_URL}creer-equipement/`, data);
  },

  createDocumentation(data) {
    return axios.post(`${API_URL}creer-document-technique/`, data);
  },

  joinEquipementDocumentation(data) {
    return axios.post(`${API_URL}jointure-equipement-document/`, data);
  },

};