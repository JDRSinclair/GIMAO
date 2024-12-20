<template>
  <v-app-bar app color="white" elevation="2" density="comfortable" class="px-6">
    <!-- Logo and Title -->
    <v-col class="d-flex align-center justify-start">
      <v-avatar size="48" class="mr-2">
        <v-img
          src="https://i.imghippo.com/files/wCa5810fAA.png"
          alt="Logo"
          cover
          class="border"
        ></v-img>
      </v-avatar>
      <span class="text-h6 font-weight-bold" style="color: #151d48; font-family: 'Montserrat', sans-serif;">
        GIMAO
      </span>
    </v-col>

    <!-- Left-aligned Page Title -->
    <div class="text-h5 font-weight-bold" style="color: #151d48; margin-left: 16px;">
      Tableau de Bord
    </div>

    <v-spacer></v-spacer>

    <!-- Action Buttons -->
    <v-btn
      color="#151D48"
      class="mr-4 text-none"
      density="comfortable"
    >
      <v-icon start>mdi-database-export</v-icon>
      Exporter la base de données
    </v-btn>

    <v-btn
      color="#151D48"
      class="mr-4 text-none"
      density="comfortable"
    >
      <v-icon start>mdi-logout</v-icon>
      Déconnexion
    </v-btn>

    <!-- Profile Section -->
    <v-avatar size="40" class="ml-4">
      <v-img
        src="https://i.imghippo.com/files/SRJI2293jtI.png"
        alt="Admin"
        cover
        class="border"
      ></v-img>
    </v-avatar>
    <div class="ml-2 text-left">
      <div class="font-weight-bold" style="color: #151d48;">
        Admin
      </div>
      <div class="text-caption text-grey-darken-1">
        Administrateur
      </div>
    </div>
  </v-app-bar>
</template>

<script>
export default {
  name: "TopNavBar",
};
</script>