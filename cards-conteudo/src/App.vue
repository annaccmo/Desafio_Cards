<template>
  <v-app>
    <v-app-bar
      prominent
      src="./img/background.svg"
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="./img/brand-insights@3x.svg"
          transition="scale-transition"
          width="70"
        />
      </div>

      <v-spacer></v-spacer>
      

      <v-btn icon>
        <v-icon
          size="80"
          color="#ED4D77"
        >
          mdi-circle
          </v-icon>
      </v-btn>
      

      <v-spacer></v-spacer>


      <v-btn icon>
        <v-icon
          large
          color="#ED4D77"
        >
          mdi-plus
          </v-icon>
      </v-btn>
    </v-app-bar>

        <v-main>
      <v-container>
        <v-row>
          <v-col
            v-for="n in 24"
            :key="n"
            cols="4"
          >
            <v-card elevation="8" shaped height="200"></v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    //
  }
</script>