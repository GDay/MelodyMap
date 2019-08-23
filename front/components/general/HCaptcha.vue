<template>
  <div>
    <div id="captcha" />
    <p v-if="error" class="red-error">
      {{ error[0] }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'HCaptcha',
  props: {
    error: {
      type: Array,
      default: () => { return [] }
    },
    value: {
      type: String,
      default: ''
    }
  },
  data () {
    return {
      script: undefined
    }
  },
  beforeMount () {
    this.script = document.createElement('script')
    this.script.src = 'https://hcaptcha.com/1/api.js?render=explicit'
    this.script.onload = this.renderCaptcha
    document.querySelector('head').append(this.script)
  },
  beforeDestroy () {
    const hcaptcha = document.querySelector('iframe')
    if (hcaptcha) {
      hcaptcha.remove()
    }
    this.script.parentNode.removeChild(this.script)
  },
  methods: {
    updateToken (response) {
      this.$emit('input', response)
    },
    resetCaptcha () {
      window.hcaptcha.reset()
    },
    renderCaptcha () {
      window.hcaptcha.render('captcha', { sitekey: process.env.hCaptcha, callback: this.updateToken })
    }
  }
}
</script>

<style scoped>
.red-error {
  color: red
}
</style>
