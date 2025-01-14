import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createVuetify } from 'vuetify';
import 'vuetify/styles';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import './assets/css/global.css';  
import '@mdi/font/css/materialdesignicons.css' // Ajout de cette ligne pour MDI

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi', // Définir MDI comme jeu d'icônes par défaut
  },
});

const app = createApp(App);

// Utilisez le routeur avant Vuetify
app.use(router);

// Utilisez Vuetify
app.use(vuetify);

// Fournir Vuetify à l'application
app.provide('vuetify', vuetify);

// Montez l'application
app.mount('#app');