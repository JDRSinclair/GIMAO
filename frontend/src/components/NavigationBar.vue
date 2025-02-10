<template>
  <v-navigation-drawer app permanent>
    <template v-slot:prepend>
      <v-list-item
        lines="two"
        :prepend-avatar="logo"
        :class="[$style.logoContainer, 'd-flex justify-center']"
        @click="goToDashboard"
        style="cursor: pointer;"
      >
        <v-list-item-title :class="[$style.logoTitle, 'font-weight-bold text-center']">
          {{ appTitle }}
        </v-list-item-title>
      </v-list-item>
    </template>

    <v-divider></v-divider>

    <v-list density="compact" nav class="d-flex flex-column align-center">
      <v-list-item
        v-for="item in navigationItems"
        :key="item.name"
        :to="!item.disabled ? { name: item.name } : null"
        :class="[getItemClasses(item.name), $style.itemSize, { 'disabled-item': item.disabled }]"
        @click="item.disabled ? $event.preventDefault() : null"
      >
        <template v-slot:prepend>
          <v-icon
            :color="isActive(item.name) ? 'white' : 'primary'"
            :class="[{ 'active-icon': isActive(item.name), 'inner-shadow': true }, $style.icon]"
          >
            {{ item.icon }}
          </v-icon>
        </template>
        <v-list-item-title class="font-weight-bold text-center" v-html="item.title"></v-list-item-title>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: {
    logo: {
      type: String,
      default: () => require('@/assets/images/LogoGIMAO.png'),
    },
    appTitle: {
      type: String,
      default: 'GIMAO',
    },
    navigationItems: {
      type: Array,
      default: () => [
        { name: 'Dashboard', icon: 'mdi-view-dashboard', title: 'Tableau de bord' },
        { name: 'EquipmentList', icon: 'mdi-tools', title: 'Équipements' },
        { name: 'Maintenances', icon: 'mdi-wrench', title: 'Bons de travail' },
        { name: 'FailureList', icon: 'mdi-alert', title: 'Demandes de <br>bons de travail' },
        { name: 'Technicians', icon: 'mdi-account-hard-hat', title: 'Techniciens', disabled: true },
        { name: 'AccountManagement', icon: 'mdi-account-cog', title: 'Gestion des <br>comptes', disabled: true },
        { name: 'Orders', icon: 'mdi-cart', title: 'Commandes', disabled: true },
        { name: 'Stocks', icon: 'mdi-package-variant-closed', title: 'Stocks',disabled: true },
        { name: 'DataManagement', icon: 'mdi-database-cog', title: 'Gestion des <br>données' }
      ],
    },
  },
  methods: {
    isActive(routeName) {
      return this.$route.name === routeName;
    },
    getItemClasses(itemName) {
      return {
        'active-item': this.isActive(itemName),
        'no-hover': this.isActive(itemName),
        'inner-shadow': true,
      };
    },
    goToDashboard() {
      this.$router.push({ name: 'Dashboard' });
    },
  },
};
</script>

<style module>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

:root {
  --primary-color: #5D5FEF;
  --hover-color: #e0e0e0;
  --text-color: #000;
  --active-text-color: #fff;
}

.logoContainer {
  height: 100px;
}

.logoContainer:active {
  transform: scale(0.95);
  transition: transform 0.2s;
}

.logoTitle {
  font-size: 24px;
}

.itemSize {
  width: 80%;
  height: auto;
  padding: 5%;
}

.icon {
  width: 50%;
  height: auto;
  margin-right: 2%;
}
</style>

<style scoped>
body {
  font-family: 'Poppins', sans-serif;
}

.v-list-item {
  color: var(--text-color);
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.v-list-item:not(.no-hover):hover {
  background-color: var(--hover-color);
}

.active-item {
  background-color: var(--primary-color);
  color: var(--active-text-color);
}

.active-icon {
  filter: brightness(0) invert(1);
}

.inner-shadow {
  box-shadow: inset 0 20px 50px rgba(55, 69, 87, 0.1);
}

.disabled-item {
  pointer-events: none;
  opacity: 0.5;
}
</style>