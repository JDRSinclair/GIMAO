<template>
  <v-app-bar app color="white" elevation="2" density="comfortable" class="px-6">
    <!-- Logo and Title -->
    <v-col class="d-flex align-center justify-start">
    </v-col>
    <!-- Left-aligned Page Title -->
    <div class="text-h5 font-weight-bold page-title">
      {{ pageTitle }}
    </div>

    <v-spacer></v-spacer>

    <!-- Action Buttons -->
    <v-btn
      color="primary"
      class="mr-4 text-none"
      density="comfortable"
      @click="exportDatabase"
    >
      <v-icon start>mdi-database-export</v-icon>
      Exporter la base de données
    </v-btn>

    <v-btn
      color="primary"
      class="mr-4 text-none"
      density="comfortable"
      @click="logout"
    >
      <v-icon start>mdi-logout</v-icon>
      Déconnexion
    </v-btn>

    <!-- Profile Section -->
    <v-avatar size="40" class="ml-4">
      <v-img :src="userAvatarUrl" :alt="userName" cover class="border"></v-img>
    </v-avatar>
    <div class="ml-2 text-left">
      <div class="font-weight-bold user-name">
        {{ userName }}
      </div>
      <div class="text-caption text-grey-darken-1">
        {{ userRole }}
      </div>
    </div>
  </v-app-bar>
</template>

<script>
export default {
  name: "TopNavBar",
  props: {
    pageTitle: {
      type: String,
      required: true
    },
    userName: {
      type: String,
      default: "Admin"
    },
    userRole: {
      type: String,
      default: "Administrateur"
    },
    userAvatarUrl: {
      type: String,
      default: "https://i.imghippo.com/files/SRJI2293jtI.png"
    },
    logoUrl: {
      type: String,
      default: "https://i.imghippo.com/files/wCa5810fAA.png"
    }
  },
  methods: {
    exportDatabase() {
      // Logique pour exporter la base de données
      console.log("Exporting database...");
    },
    logout() {
      // Logique pour la déconnexion
      console.log("Logging out...");
    }
  }
};
</script>

<style scoped>
.app-title, .page-title, .user-name {
  color: #151d48;
}

.app-title {
  font-family: 'Montserrat', sans-serif;
}
</style>