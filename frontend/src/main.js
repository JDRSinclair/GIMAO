import { createApp } from 'vue';
import App from './App.vue';
import { createVuetify } from 'vuetify';
import 'vuetify/styles'; // Ensure you are using css-loader

const vuetify = createVuetify();

createApp(App).use(vuetify).mount('#app');
