<template>
  <v-app>
    <v-main>
      <v-container v-if="!isLoading">
        <v-row>
          <!-- Section gauche : Détails de l'équipement -->
          <v-col cols="6">
            <v-card elevation="1" class="rounded-lg pa-2">
              <v-card-title class="font-weight-bold text-uppercase text-primary">Description de l'équipement</v-card-title>

              <v-row class="pa-2">
                <v-col cols="12" v-for="(value, key) in equipementDetails" :key="key">
                  <p><strong>{{ formatLabel(key) }} :</strong> {{ formatValue(value) }}</p>
                </v-col>
              </v-row>

              <!-- Section documentation -->
                <v-card elevation="1" class="rounded-lg pa-2 mt-4">
                  <v-card-title class="font-weight-bold text-uppercase text-primary">Documentation</v-card-title>

                  <!-- Documents techniques -->
                  <v-card-subtitle class="pt-4">Documents techniques</v-card-subtitle>
                  <v-data-table
                    :headers="documentTechniquesHeaders"
                    :items="equipement.liste_documents_techniques"
                    item-value="nomDocumentTechnique"
                    class="elevation-1 rounded-lg mb-4"
                    hide-default-footer
                  >
                    <template v-slot:item="{ item }">
                      <tr>
                        <td>{{ item.nomDocumentTechnique }}</td>
                        <td>
                          <v-btn
                            icon
                            small
                            color="primary"
                            center="center"
                            @click="telechargerDocument(item.lienDocumentTechnique, item.nomDocumentTechnique)"
                          >
                            <v-icon>mdi-download</v-icon>
                          </v-btn>
                        </td>
                      </tr>
                    </template>
                  </v-data-table>

                  <!-- Autres documents -->
                  <v-card-subtitle class="pt-4">Autres documents</v-card-subtitle>
                  <v-data-table
                    :headers="autresDocumentsHeaders"
                    :items="autresDocuments"
                    class="elevation-1 rounded-lg"
                    hide-default-footer
                  >
                    <template v-slot:item="{ item }">
                      <tr>
                        <td>{{ item.type }}</td>
                        <td>{{ item.nomDocument }}</td>
                        <td>
                          <v-btn
                            icon
                            small
                            color="primary"
                            @click="telechargerDocument(item.lienDocument, item.nomDocument)"
                          >
                            <v-icon>mdi-download</v-icon>
                          </v-btn>
                        </td>
                      </tr>
                    </template>
                  </v-data-table>
                </v-card>
            </v-card>
          </v-col>

          <!-- Section droite : Image, consommables, maintenance et actions -->
          <v-col cols="6">
            <!-- Section image -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-img
                :src="equipement.lienImageEquipement"
                aspect-ratio="4/3"
                class="rounded-lg"
                style="max-height: 30vh;"
                alt="Image de l'équipement"
              ></v-img>
            </v-card>
            
            <!-- Section consommables -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">
                Consommables
              </v-card-title>
              <v-data-table
                :items="equipement.liste_consommables"
                :headers="consommablesHeaders"
                class="elevation-1 rounded-lg"
                hide-default-footer
              ></v-data-table>
            </v-card>

            <!-- Historique de maintenance -->
            <v-card elevation="1" class="rounded-lg pa-2 mb-4">
              <v-card-title class="font-weight-bold text-uppercase text-primary">
                Interventions
              </v-card-title>
              <v-data-table
                :items="equipement.liste_interventions"
                :headers="interventionsHeaders"
                class="elevation-1 rounded-lg"
                hide-default-footer
              >
              <template v-slot:item.dateAssignation="{ item }">
                {{ formatDate(item.dateAssignation) }}
              </template>
              <template v-slot:item.action="{ item }">
                <v-btn icon @click="voirIntervention(item)">
                  <v-icon>mdi-eye</v-icon>
                </v-btn>
              </template>
            </v-data-table>
            </v-card>

            <!-- Bouton d'action -->
            <v-row justify="end">
              <v-btn color="primary" class="mt-4" large @click="modifierEquipement">
                Modifier
              </v-btn>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
      <v-progress-circular
        v-else
        indeterminate
        color="primary"
        size="64"
      ></v-progress-circular>
    </v-main>
  </v-app>
</template>

<script>
import api , { BASE_URL } from '@/services/api';
import { useRouter } from 'vue-router';


export default {
  name: 'AfficherEquipement',
  setup() {
    const router = useRouter();
    return { router };
  },
  data() {
    
    return {
      isLoading: true,
      equipement: {},
      documentTechniquesHeaders: [
        { title: "Document technique", value: "nomDocumentTechnique", align: "start" },
        { title: "Télécharger", value: "action", align: "center", sortable: false }
      ],
      autresDocumentsHeaders: [
        { title: "Type", value: "type", align: "start" },
        { title: "Document", value: "nomDocument", align: "start" },
        { title: "Télécharger", value: "action", align: "center", sortable: false }
      ],
      consommablesHeaders: [
        { title: "Désignation", value: "designation" },
        { title: "Fabricant", value: "fabricant.nomFabricant" }
      ],
      interventionsHeaders: [
        { title: "Nom", value: "nomIntervention" },
        { title: "Date d'assignation", value: "dateAssignation" },
        { title: "Visualiser", value: "action" }
      ]
    };
  },
  
  computed: {
    equipementDetails() {
      if (!this.equipement) return {};
      const { 
        reference, designation, dateMiseEnService, prixAchat, 
        preventifGlissant, joursIntervalleMaintenance
      } = this.equipement;
      const lieu = this.equipement.lieu ? this.equipement.lieu.nomLieu : '';
      const modele = this.equipement.modeleEquipement ? this.equipement.modeleEquipement.nomModeleEquipement : '';
      const fournisseur = this.equipement.fournisseur ? this.equipement.fournisseur.nomFournisseur : '';
      const fabricant = this.equipement.fabricant ? this.equipement.fabricant.nomFabricant : '';
      const statut = this.equipement.dernier_statut ? this.equipement.dernier_statut.statutEquipement : '';
      
      return { 
        reference, designation, dateMiseEnService, prixAchat, 
        preventifGlissant, joursIntervalleMaintenance,
        lieu, modele, fournisseur, fabricant, statut
      };
    },
    autresDocuments() {
      const documentsDefaillance = (this.equipement.liste_documents_defaillance || []).map(doc => ({
        type: 'Défaillance',
        nomDocument: doc.nomDocumentDefaillance,
        lienDocument: doc.lienDocumentDefaillance
      }));
      const documentsIntervention = (this.equipement.liste_documents_intervention || []).map(doc => ({
        type: 'Intervention',
        nomDocument: doc.nomDocumentIntervention,
        lienDocument: doc.lienDocumentIntervention
      }));
      return [...documentsDefaillance, ...documentsIntervention];
    }
  },

  methods: {
    async fetchEquipementData() {
      try {
        const response = await api.getEquipementAffichage(this.$route.params.reference);
        this.equipement = response.data;
        this.isLoading = false;
      } catch (error) {
        console.error("Erreur lors de la récupération des données de l'équipement:", error);
        this.isLoading = false;
      }
    },
    formatDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      return date.toLocaleString('fr-FR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        hour12: false
      }).replace(',', '');
    },
    
    formatLabel(key) {
      const labels = {
        reference: 'Référence',
        designation: 'Désignation',
        dateMiseEnService: 'Date de mise en service',
        prixAchat: 'Prix d\'achat',
        preventifGlissant: 'Préventif glissant',
        joursIntervalleMaintenance: 'Intervalle de maintenance (jours)',
        lieu: 'Lieu',
        modele: 'Modèle',
        fournisseur: 'Fournisseur',
        fabricant: 'Fabricant',
        statut: 'Statut'
      };
      return labels[key] || key;
    },

    formatValue(value) {
      if (typeof value === 'boolean') {
        return value ? 'Oui' : 'Non';
      }
      if (typeof value === 'number') {
        return value.toLocaleString();
      }
      return value;
    },

    telechargerDocument(lien) {
      window.open(lien, '_blank');
    },

    voirIntervention(intervention) {
      this.router.push({
        name: 'AfficherIntervention',
        params: { id: intervention.id }
      });
    },

    modifierEquipement() {
      // Implémenter la logique pour modifier l'équipement
      console.log("Modifier l'équipement");
    },

    telechargerDocument(lien, nomFichier) {
        const cleanedLink = lien.startsWith('/media/') ? lien : `/media/${lien.split('/media/').pop()}`;
        const fullUrl = `${BASE_URL}${cleanedLink}`;

        fetch(fullUrl)
          .then(response => {
            if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.blob();
          })
          .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = nomFichier;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
          })
          .catch(error => {
            alert('Erreur lors du téléchargement du fichier. Veuillez réessayer.');
          });
      },
    
  },

  created() {
    this.fetchEquipementData();
  }
};



</script>

<style scoped>
.text-primary {
  color: #05004E;
}

.text-dark {
  color: #3C3C3C;
}

.v-card {
  background-color: #FFFFFF;
}

.v-btn {
  background-color: #F1F5FF;
  border-radius: 50%;
}

.eye-icon {
  width: 24px;
  height: 24px;
}

h1 {
  color: #05004E;
}
</style>
