<template>
  <div>
    <h2>Ajouter un nouvel équipement</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="reference">Référence:</label>
        <input type="text" id="reference" v-model="formData.reference" required />
      </div>

      <div>
        <label for="dateCreation">Date de création:</label>
        <input type="datetime-local" id="dateCreation" v-model="formData.dateCreation" required />
      </div>

      <div>
        <label for="designation">Désignation:</label>
        <input type="text" id="designation" v-model="formData.designation" />
      </div>

      <div>
        <label for="dateMiseEnService">Date de mise en service:</label>
        <input type="date" id="dateMiseEnService" v-model="formData.dateMiseEnService" required />
      </div>

      <div>
        <label for="prixAchat">Prix d'achat:</label>
        <input type="number" id="prixAchat" v-model="formData.prixAchat" step="0.01" />
      </div>

      <div>
        <label for="lienImageEquipement">Image de l'équipement:</label>
        <input type="file" id="lienImageEquipement" @change="handleImageUpload" />
      </div>

      <div>
        <label for="preventifGlissant">Préventif glissant:</label>
        <input type="checkbox" id="preventifGlissant" v-model="formData.preventifGlissant" />
      </div>

      <div>
        <label for="joursIntervalleMaintenance">Jours d'intervalle de maintenance:</label>
        <input type="number" id="joursIntervalleMaintenance" v-model="formData.joursIntervalleMaintenance" />
      </div>

      <div>
        <label for="fournisseur">Fournisseur:</label>
        <select id="fournisseur" v-model="formData.fournisseur" required>
          <option v-for="fourn in fournisseurs" :key="fourn.id" :value="fourn.id">{{ fourn.nomFournisseur }}</option>
        </select>
      </div>

      <div>
        <label for="modeleEquipement">Modèle:</label>
        <select id="modeleEquipement" v-model="formData.modeleEquipement" required>
          <option v-for="mod in modeles" :key="mod.id" :value="mod.id">{{ mod.nomModeleEquipement }}</option>
        </select>
      </div>

      <div>
        <label for="lieu">Lieu:</label>
        <select id="lieu" v-model="formData.lieu" required>
          <option v-for="l in lieux" :key="l.id" :value="l.id">{{ l.nomLieu }}</option>
        </select>
      </div>

      <div>
        <label for="createurEquipement">Créateur:</label>
        <select id="createurEquipement" v-model="formData.createurEquipement" required>
          <option v-for="uti in utilisateurs" :key="uti.id" :value="uti.id">{{ uti.username }}</option>
        </select>
      </div>

      <div>
        <label for="nomDocumentTechnique">Nom du document:</label>
        <input type="text" id="nomDocumentTechnique" v-model="formData.nomDocumentTechnique"/>
      </div>

      <div>
        <label for="lienDocumentTechnique">Document:</label>
        <input type="file" id="lienDocumentTechnique" @change="handleFileUpload" />
      </div>

      <button type="submit">Ajouter l'équipement</button>
    </form>
  </div>
</template>

<script>
import { ref, reactive, onMounted, toRefs } from 'vue';
import api from '@/services/api'; // Assurez-vous que l'API est bien configurée
import { useRouter } from 'vue-router';

export default {
  name: 'testInsertionEquipement',
  setup() {
    const router = useRouter();

    const state = reactive({
      formData: {
        reference: '',
        dateCreation: '',
        designation: '',
        dateMiseEnService: '',
        prixAchat: null,
        lienImageEquipement: null,
        preventifGlissant: false,
        joursIntervalleMaintenance: null,
        fournisseur: null,
        modeleEquipement: null,
        lieu: null,
        createurEquipement: null,
        nomDocumentTechnique: '',
        lienDocumentTechnique: null,
        documentationTechnique: null,
      },
      fournisseurs: [],
      modeles: [],
      lieux: [],
      utilisateurs: [],
    });

    const handleImageUpload = (event) => {
      state.formData.lienImageEquipement = event.target.files[0];
    };

    const handleFileUpload = (event) => {
      state.formData.lienDocumentTechnique = event.target.files[0];
    };

    const submitForm = async () => {
      const formDataEquipement = new FormData();
      let counter = 0;
      // Ajouter les 12 premiers champs dans formDataEquipement
      Object.keys(state.formData).forEach((key) => {
        counter = counter + 1
        if (state.formData[key] !== null && state.formData[key] !== undefined) {
          if(counter < 13) {
            formDataEquipement.append(key, state.formData[key]);
          }
        }
      });
        // Envoi de la requête pour l'équipement
        const responseEquipement = await api.createEquipement(formDataEquipement);

        if (responseEquipement.status === 201) {
          alert('Équipement ajouté avec succès !');

          // Si le nom du document technique est renseigné, ajouter à la table des documents
          if (state.formData.nomDocumentTechnique) {
            const formDataDocument = new FormData();
            formDataDocument.append('nomDocumentTechnique', state.formData.nomDocumentTechnique);
            formDataDocument.append('lienDocumentTechnique', state.formData.lienDocumentTechnique);

            const responseDocument = await api.createDocumentation(formDataDocument);

            if (responseDocument.status === 201) {
              alert('Document technique ajouté avec succès !');

              await fetchDocument();

              const formDataJointure = new FormData();
              formDataJointure.append('modeleEquipement', state.formData.modeleEquipement);  // ID du modèle
              formDataJointure.append('documentationTech', state.documentsTech[0].id);

              await api.joinEquipementDocumentation(formDataJointure);
              if (responseDocument.status === 201) {
                alert('Jointure réussite !');
                router.push('/equipements');
              } else {
                alert('Erreur lors de la jointure.');
              }
            } else {
              alert('Erreur lors de l’ajout du document technique.');
            }
          }
        } else {
          alert('Erreur lors de l’ajout de l’équipement.');
        }
    };

    const fetchDocument = async () => {
      try {
        const documentationRES = await api.getDernierDocumentationTech();

        if (documentationRES.data) {
          state.documentsTech = state.documentsTech || [];
          state.documentsTech.push(documentationRES.data);
        }
      } catch (error) {
        console.error('Erreur lors du chargement des données :', error);
      }
    };

    const fetchData = async () => {
      try {
        const [fournisseurRES, modeleRES, lieuRES, utilisateurRES] = await Promise.all([
          api.getFournisseurs(),
          api.getModeleEquipements(),
          api.getLieux(),
          api.getUsers(),
        ]);

        state.fournisseurs = fournisseurRES.data;
        state.modeles = modeleRES.data;
        state.lieux = lieuRES.data;
        state.utilisateurs = utilisateurRES.data;
      } catch (error) {
        console.error('Erreur lors du chargement des données :', error);
      }
    };

    onMounted(() => {
      fetchData();
    });

    return {
      ...toRefs(state),
      handleFileUpload,
      handleImageUpload,
      submitForm,
    };
  },
};
</script>



<!-- <template>
  <div>
    <h2>Ajouter un nouvel équipement</h2>
    <form @submit.prevent="submitForm">
      
      <div>
        <label for="reference">Référence:</label>
        <input type="text" id="reference" v-model="formData.reference" required />
      </div>

      <div>
        <label for="dateCreation">Date de création:</label>
        <input type="datetime-local" id="dateCreation" v-model="formData.dateCreation" required />
      </div>

      <div>
        <label for="designation">Désignation:</label>
        <input type="text" id="designation" v-model="formData.designation" />
      </div>

      <div>
        <label for="dateMiseEnService">Date de mise en service:</label>
        <input type="date" id="dateMiseEnService" v-model="formData.dateMiseEnService" required />
      </div>

      <div>
        <label for="prixAchat">Prix d'achat:</label>
        <input type="number" id="prixAchat" v-model="formData.prixAchat" step="0.01" />
      </div>

      <div>
        <label for="lienImageEquipement">Image de l'équipement:</label>
        <input type="file" id="lienImageEquipement" @change="handleFileUpload" />
      </div>

      <div>
        <label for="preventifGlissant">Préventif glissant:</label>
        <input type="checkbox" id="preventifGlissant" v-model="formData.preventifGlissant" />
      </div>

      <div>
        <label for="joursIntervalleMaintenance">Jours d'intervalle de maintenance:</label>
        <input type="number" id="joursIntervalleMaintenance" v-model="formData.joursIntervalleMaintenance" />
      </div>

      <div>
        <label for="fournisseur">Fournisseur:</label>
        <select id="fournisseur" v-model="formData.fournisseur" required>
          <option v-for="fourn in fournisseurs" :key="fourn.id" :value="fourn.id">{{ fourn.nomFournisseur }}</option>
        </select>
      </div>

      <div>
        <label for="modeleEquipement">Modèle:</label>
        <select id="modeleEquipement" v-model="formData.modeleEquipement" required>
          <option v-for="mod in modeles" :key="mod.id" :value="mod.id">{{ mod.nomModeleEquipement }}</option>
        </select>
      </div>

      <div>
        <label for="lieu">Lieu:</label>
        <select id="lieu" v-model="formData.lieu" required>
          <option v-for="l in lieux" :key="l.id" :value="l.id">{{ l.nomLieu }}</option>
        </select>
      </div>

      <div>
        <label for="createurEquipement">Créateur:</label>
        <select id="createurEquipement" v-model="formData.createurEquipement" required>
          <option v-for="uti in utilisateurs" :key="uti.id" :value="uti.id">{{ uti.username }}</option>
        </select>
      </div>
      

      
      <div>
        <label for="nomDocumentTechnique">Nom du document:</label>
        <input type="text" id="nomDocumentTechnique" v-model="formData.nomDocumentTechnique"/>
      </div>

      <div>
        <label for="lienDocumentTechnique">Document:</label>
        <input type="file" id="lienDocumentTechnique" @change="handleFileUpload" />
      </div>

      <button type="submit">Ajouter l'équipement</button>
    </form>
  </div>
</template>

<script>
import { ref, reactive, onMounted, toRefs } from 'vue';
import api from '@/services/api'; 
import { useRouter } from 'vue-router';

export default {
  name: 'AjouterEquipement',
  setup() {
    const router = useRouter();

    const state = reactive({
      formData: {
        reference: '',
        dateCreation: '',
        designation: '',
        dateMiseEnService: '',
        prixAchat: null,
        lienImageEquipement: null,
        preventifGlissant: false,
        joursIntervalleMaintenance: null,
        fournisseur: null,
        modeleEquipement: null,
        lieu: null,
        createurEquipement: null,
        nomDocumentTechnique: '',
        lienDocumentTechnique: null,
      },
      fournisseurs: [],
      modeles: [],
      lieux: [],
      utilisateurs: [],
    });

    const handleFileUpload = (event) => {
      state.formData.lienImageEquipement = event.target.files[0];
    };

    const submitForm = async () => {
      const formData = new FormData();

      Object.keys(state.formData).forEach((key) => {
        if (key !== 'nomDocumentTechnique' && key !== 'lienDocumentTechnique') {
          if (state.formData[key] !== null && state.formData[key] !== undefined) {
            formData.append(key, state.formData[key]);
          }
        }
      });

      try {
        const response = await api.createEquipement(formData);

        if (response.status === 201) {
          alert('Équipement ajouté avec succès !');
        } else {
          alert('Erreur lors de l’ajout de l’équipement.');
        }
      } catch (error) {
        console.error('Erreur lors de la soumission du formulaire :', error);
        alert('Une erreur est survenue.');
      }
    };


    const fetchData = async () => {
      try {
        const [fournisseurRES, modeleRES, lieuRES, utilisateurRES] = await Promise.all([
          api.getFournisseurs(),
          api.getModeleEquipements(),
          api.getLieux(),
          api.getUsers(),
        ]);

        state.fournisseurs = fournisseurRES.data;
        state.modeles = modeleRES.data;
        state.lieux = lieuRES.data;
        state.utilisateurs = utilisateurRES.data;
      } catch (error) {
        console.error('Erreur lors du chargement des données :', error);
      }
    };

    onMounted(() => {
      fetchData();
    });

    return {
      ...toRefs(state),
      handleFileUpload,
      submitForm,
    };
  },
};
</script> -->
