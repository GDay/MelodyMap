<template>
  <v-app>
    <v-app-bar
      app
      dark
      color="accent"
    >
      <v-toolbar-title class="hidden-sm-and-down">Connecting musicians to each other!</v-toolbar-title>
      <v-spacer />
      <SearchBar />
      <v-spacer />
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn text @click="aboutModalOpened = true">
          About
        </v-btn>
        <v-btn v-if="!$auth.loggedIn" text @click="$store.commit('toggleLoginModal')">
          Log in
        </v-btn>
        <v-btn v-if="!$auth.loggedIn" text @click="$store.commit('toggleSignupModal')">
          Sign up
        </v-btn>
        <v-btn v-if="$auth.loggedIn" text @click="logout">
          Log out
        </v-btn>
      </v-toolbar-items>
    </v-app-bar>
    <v-content style="padding: 0px; margin-top: 60px;">
      <v-container fill-height ma-0 pa-0 style="max-width: 100%">
        <nuxt />
      </v-container>
    </v-content>
    <LoginModal />
    <SignupModal />
    <AboutModal v-model="aboutModalOpened" />
    <SnackbarNotification />
  </v-app>
</template>

<script>
import LoginModal from '@/components/auth/LoginModal'
import SignupModal from '@/components/auth/SignupModal'
import AboutModal from '@/components/AboutModal'
import SnackbarNotification from '@/components/general/SnackbarNotification'
import SearchBar from '@/components/general/SearchBar'

export default {
  components: { LoginModal, SignupModal, SnackbarNotification, SearchBar, AboutModal },
  data () {
    return {
      aboutModalOpened: false,
      detailModalOpened: false,
      item: {}
    }
  },
  methods: {
    logout () {
      this.$auth.logout()
    }
  }
}
</script>
