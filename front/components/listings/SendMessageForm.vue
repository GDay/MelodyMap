<template>
  <div>
    <v-form>
      <v-text-field
        v-model="email.name"
        label="Name"
        class="mt-4"
        placeholder="John Smith"
        :error-messages="errors.name"
        @keyup="errors.name=''"
      />
      <v-text-field
        v-model="email.email"
        label="Email"
        type="email"
        placeholder="john@example.com"
        :error-messages="errors.email"
        @keyup="errors.email=''"
      />
      <v-textarea
        v-model="email.message"
        label="Message"
        placeholder="Hi, I am..."
        :error-messages="errors.message"
        @keyup="errors.message=''"
      />
      <h-captcha ref="captcha" v-model="email.hcaptcha" :error="errors.hcaptcha" />
    </v-form>
    <v-btn block :loading="loading" color="primary" @click="sendMessage">
      Send message
    </v-btn>
  </div>
</template>

<script>
import HCaptcha from '@/components/general/HCaptcha'
export default {
  name: 'SendMessageForm',
  components: { HCaptcha },
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data () {
    return {
      loading: false,
      email: {},
      errors: []
    }
  },
  methods: {
    sendMessage () {
      this.loading = true
      this.$adverts.sendMesasge(this.id, this.email).then((data) => {
        this.$store.dispatch('showSnackbar', 'Email has been sent!')
        this.$emit('closeModal')
      }).catch((errors) => {
        this.errors = errors
        this.$refs.captcha.resetCaptcha()
      }).finally(() => {
        this.loading = false
      })
    }
  }
}
</script>
