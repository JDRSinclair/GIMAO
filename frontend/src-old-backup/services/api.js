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

  getInformationStatus() {
    return axios.get(`${API_URL}informationStatus/`);
  },

  getEquipementById(id) {
    return axios.get(`${API_URL}equipements/${id}/`);
  },
};

