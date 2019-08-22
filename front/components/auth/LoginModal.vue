<template>
  <v-dialog
    v-model="$store.state.loginModalOpen"
    width="500"
    persistent
  >
    <v-card>
      <v-card-title
        class="headline"
        primary-title
      >
        <modal-header text="Login" @onCloseModal="closeModal" />
      </v-card-title>

      <v-card-text>
        <v-form>
          <v-text-field
            v-model="username"
            label="Email"
            placeholder="john@example.com"
          />
          <v-text-field
            v-model="password"
            label="Password"
            type="password"
            placeholder="*****"
            @keyup.enter="login"
          />
        </v-form>
        <v-layout>
          <a @click="goToPasswordReset">Forgot password?</a>
        </v-layout>
      </v-card-text>

      <v-divider />

      <v-card-actions>
        <v-spacer />
        <v-btn block :loading="loading" color="primary" @click="login">
          Log in
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'LoginModal',
  data () {
    return {
      username: '',
      password: '',
      loading: false
    }
  },
  methods: {
    login () {
      this.loading = true
      this.$auth
        .loginWith('local', {
          data: {
            username: this.username,
            password: this.password
          }
        })
        .then(() => {
          this.$store.dispatch('showSnackbar', 'You are now logged in')
          this.$store.commit('toggleLoginModal')
        })
        .catch((error) => {
          this.$store.dispatch('showSnackbar', error.response.data.error)
        })
        .finally(() => {
          this.loading = false
        })
    },
    goToPasswordReset () {
      // this.loading = true
    },
    closeModal () {
      this.$store.commit('toggleLoginModal')
      this.username = ''
      this.password = ''
    }
  }
}
</script>
