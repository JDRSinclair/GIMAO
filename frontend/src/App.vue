<template>
  <v-app>
    <NavigationDrawer :items="menuItems" />
    <TopNavBar :pageTitle="currentPageTitle" />
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import NavigationDrawer from '@/components/BarreNavigation.vue';
import TopNavBar from "@/components/BarreNavigationHaut.vue";

export default {
  name: 'App',
  components: {
    NavigationDrawer,
    TopNavBar,
  },
  
  data() {
    return {
      currentPageTitle: '',
      menuItems: [
        { name: 'Tableau de bord', icon: require('@/assets/images/Graphe.svg'), routeName: 'Dashboard' },
        { name: 'Equipements', icon: require('@/assets/images/Outils.svg'), routeName: 'Equipements' },
        { name: 'Maintenances', icon: require('@/assets/images/Maintenance.svg'), routeName: 'Maintenances' },
        { name: 'Techniciens', icon: require('@/assets/images/Techniciens.svg'), routeName: 'Techniciens' },
      ],
    };
  },
  
  watch: {
    $route: {
      immediate: true,
      handler(to) {
        this.currentPageTitle = to.meta.title || 'GIMAO';
      }
    }
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

h1 {
  color: #05004E;
}
</style>