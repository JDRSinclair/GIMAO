
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

const apiClient = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Récupérer tous les lieux
export const getAllLieux = () => apiClient.get('lieux/');

// Récupérer tous les types d'équipements si aucun lieu n'est pris
export const getAllTypesEquipements = () => apiClient.get('modeleequipements/');

// Récupérer les types d'équipements pour un lieu donné
export const getTypesEquipementsByLieu = (lieuId) => apiClient.get(`lieux/${lieuId}/types-equipements/`);

// Récupérer tous les équipements si aucun choix n'est fait
export const getAllEquipements = () => apiClient.get('equipements/');

// Récupérer tous les équipements pour un lieu et un type d'équipement donnés
export const getEquipementsByLieu = (lieuId, typeEquipementId) => apiClient.get(`lieux/${lieuId}/equipements/`, { params: { typeEquipementId } });

// Récupérer tous les équipements pour plusieurs lieux et types d'équipements donnés
export const getEquipementsByLieuxAndTypes = (lieuIds, typeIds) => {
  return Promise.all(lieuIds.map(lieuId => typeIds.map(typeId => getEquipementsByLieu(lieuId, typeId))).flat());
};

export default apiClient;
