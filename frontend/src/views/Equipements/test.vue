<template>
  <div>
    <h2>Ajouter un nouvel équipement</h2>
    <form @submit.prevent="submitForm">

      <div>
        <label for="nomDocumentTechnique">Nom du document:</label>
        <input type="text" id="nomDocumentTechnique" v-model="formData.nomDocumentTechnique"/>
      </div>

      <div>
        <label for="lienDocumentTechnique">Document:</label>
        <input type="file" id="lienDocumentTechnique" @change="handleFileUpload" />
      </div>

      <div>
        <label for="modeleEquipement">Modèle:</label>
        <select id="modeleEquipement" v-model="formData.modeleEquipement" required>
          <option v-for="mod in modeles" :key="mod.id" :value="mod.id">{{ mod.nomModeleEquipement }}</option>
        </select>
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
        nomDocumentTechnique: '',
        lienDocumentTechnique: null,
        modeleEquipement: null,
        
      },
      documentsTech: [],
      modeles: []
    });

    const handleFileUpload = (event) => {
      state.formData.lienDocumentTechnique = event.target.files[0];
    };

    const submitForm = async () => {
      const formDataEquipement = new FormData();
      let counter = 0;

      Object.keys(state.formData).forEach((key) => {
        counter = counter + 1;
        if (state.formData[key] !== null && state.formData[key] !== undefined) {
          if (counter < 3) {
            formDataEquipement.append(key, state.formData[key]);
          }
        }
      });

      try {
        const responseEquipement = await api.createDocumentation(formDataEquipement);

        if (responseEquipement.status === 201) {
          alert('Équipement ajouté avec succès !');

          await fetchData();

          const formDataJointure = new FormData();
          formDataJointure.append('modeleEquipement', state.formData.modeleEquipement);  // ID du modèle
          formDataJointure.append('documentationTech', state.documentsTech[0].id);

          await api.joinEquipementDocumentation(formDataJointure);
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
        const documentationRES = await api.getDernierDocumentationTech();

        if (documentationRES.data) {
          state.documentsTech = state.documentsTech || [];
          state.documentsTech.push(documentationRES.data);
        }
      } catch (error) {
        console.error('Erreur lors du chargement des données :', error);
      }
    };

    const fetchFeur = async () => {
      try {
        const [modeleRES] = await Promise.all([
          api.getModeleEquipements(),
        ]);
        state.modeles = modeleRES.data;
      } catch (error) {
        console.error('Erreur lors du chargement des données :', error);
      }
    };

    onMounted(() => {
      fetchFeur();
    });

    return {
      ...toRefs(state),
      handleFileUpload,
      submitForm,
    };
  },
};
</script>



<!-- <template>
  <div>
    <h2>Test</h2>
    <form @submit.prevent="submitForm">

      <div>
        <label for="modeleEquipement">Modèle:</label>
        <select id="modeleEquipement" v-model="formData.modeleEquipement" required>
          <option v-for="mod in modeles" :key="mod.id" :value="mod.id">
            {{ mod.nomModeleEquipement }}
          </option>
        </select>
      </div>

      <div>
        <label for="documentTechnique">Document Technique:</label>
        <select id="documentTechnique" v-model="formData.documentTechnique" required>
          <option v-for="docTech in documentsTech" :key="docTech.id" :value="docTech.id">
            {{ docTech.nomDocumentTechnique }}
          </option>
        </select>
      </div>

      <button type="submit">Ajouter la documentation</button>
    </form>
  </div>
</template>

  
<script>
import { ref, reactive, onMounted, toRefs } from 'vue';
import api from '@/services/api'; 
import { useRouter } from 'vue-router';

export default {
  name: 'test',
  setup() {
    const router = useRouter();
    const state = reactive({
      formData: {
        modeleEquipement: null,
        documentTechnique: null
      },
      modeles: [],
      documentsTech: []
    });

    const submitForm = async () => {
      try {
        
        const response = await api.joinEquipementDocumentation({
          modeleEquipement: state.formData.modeleEquipement,
          documentTechnique: state.formData.documentTechnique
        });

        if (response.status === 201) {
          alert('Jointure réussie !');
          router.push('/equipements'); 
        } else {
          alert('Erreur lors de la jointure.');
        }
      } catch (error) {
        console.error('Erreur lors de la soumission du formulaire :', error);
        alert('Une erreur est survenue.');
      }
    };

    const fetchData = async () => {
      try {
        const [modeleRES, documentationRES] = await Promise.all([
          api.getModeleEquipements(),
          api.getDocumentationTech()
        ]);

        state.modeles = modeleRES.data;
        state.documentsTech = documentationRES.data;
      } catch (error) {
        console.error('Erreur lors du chargement des données :', error);
      }
    };

    onMounted(() => {
      fetchData();
    });

    return {
      ...toRefs(state),
      submitForm,
    };
  },
};
</script> -->