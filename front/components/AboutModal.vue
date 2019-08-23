<template>
  <v-dialog
    v-model="value"
    width="700"
    persistent
  >
    <v-card>
      <v-card-title
        class="headline"
        primary-title
      >
        <modal-header text="About" @onCloseModal="$emit('input', false)" />
      </v-card-title>

      <v-card-text>
        <h4>What is this site about?</h4>
        <p>
          This is a site to connect musicians to each other. Whether you are a musician
          that wants to join a band or a band that needs a guitar player/drummer/bass player/...
          Search for people or create your own listing.
        </p>
        <h4>Why?</h4>
        <p>
          There are many sites that let you post and search for other musicians, but
          not in a way that you can visually see who is where and easily see every listing
          without having to rely on how new you listing is.
        </p>
        <h4>I have a feature request!</h4>
        <p>
          Well.. great! Actually, if you are a developer familiar with Django and
          VueJS, then you can make contributions yourself. This site is open
          source on Github. If you cannot or don't want to contribution you can
          also email me at melody@stantriepels.com with your feature request and I will see what I can
          do for you.
        </p>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'AboutModal',
  props: {
    value: {
      type: Boolean,
      default: false
    }
  }
}
</script>
