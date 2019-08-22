<template>
  <v-dialog
    v-model="$store.state.signupModalOpen"
    width="500"
    persistent
  >
    <v-card>
      <v-card-title
        class="headline"
        primary-title
      >
        <modal-header text="Sign up" @onCloseModal="closeModal" />
      </v-card-title>

      <v-card-text>
        <v-form>
          <v-text-field
            v-model="user.name"
            label="Name (feel free to use a nickname)"
            placeholder="John"
            :error-messages="errors.name"
            @keyup="errors.name=''"
          />
          <v-text-field
            v-model="user.email"
            label="Email (will not be shown anywhere, but needed to send responses to)"
            placeholder="john@example.com"
            :error-messages="errors.email"
            @keyup="errors.email=''"
          />
          <v-text-field
            v-model="user.password"
            label="Password"
            type="password"
            placeholder="*****"
            :error-messages="errors.password"
            @keyup.enter="signup"
            @keyup="errors.password=''"
          />
          <h-captcha ref="captcha" v-model="user.hcaptcha" :error="errors.hcaptcha" />
        </v-form>
        <a @click="$store.commit('toggleLoginModal'); $store.commit('toggleSignupModal')">Already have an account?</a>
      </v-card-text>

      <v-divider />

      <v-card-actions>
        <v-spacer />
        <v-btn block :loading="loading" color="primary" @click="signup">
          Sign up
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import HCaptcha from '@/components/general/HCaptcha'

export default {
  name: 'SignUpModal',
  components: { HCaptcha },
  data () {
    return {
      loading: false,
      user: {},
      errors: {}
    }
  },
  methods: {
    signup () {
      this.loading = true
      this.$user.signup(this.user).then(() => {
        this.$store.commit('toggleSignupModal')
      }).catch((error) => {
        this.errors = error
        this.$refs.captcha.resetCaptcha()
      }).finally(() => {
        this.loading = false
      })
    },
    goToPasswordReset () {
      // this.loading = true
    },
    closeModal () {
      this.$store.commit('toggleSignupModal')
      this.user = {}
      this.errors = {}
    }
  }
}
</script>
