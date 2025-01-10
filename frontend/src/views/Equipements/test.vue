<template>
    <div>
      <h2>Test</h2>
      <form @submit.prevent="submitForm">

        <div>
          <label for="modeleEquipement">Modèle:</label>
          <select id="modeleEquipement" v-model="formData.modeleEquipement" required>
            <option v-for="mod in modeles" :key="mod.id" :value="mod.id">{{ mod.nomModeleEquipement }}</option>
          </select>
        </div>

        <div>
          <label for="documentationTech">Modèle:</label>
          <select id="documentationTech" v-model="formData.documentationTech" required>
            <option v-for="docTech in documentsTech" :key="docTech.id" :value="docTech.id">{{ docTech.nomDocumentTechnique }}</option>
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
          documentationTech: null
        },
        modeles: [],
        documentsTech: []
        
      });
      
      const submitForm = async () => {
        const formDataEquipement = new FormData();
        
        formDataEquipement.append('modeleEquipement', state.formData.modeleEquipement);
        formDataEquipement.append('documentationTech', state.formData.nomDocumentTechnique);

        const responseDocument = await api.joinEquipementDocumentation(formDataEquipement);
        if (responseDocument.status === 201) {
          alert('Jointure réussite !');
          router.push('/equipements');
        } else {
          alert('Erreur lors de la jointure.');
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
  </script>
  