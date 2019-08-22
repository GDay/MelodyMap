<template>
  <v-snackbar
    v-model="show"
    :right="true"
    :timeout="6000"
    :top="true"
    style="margin-top: 50px;"
  >
    {{ $store.state.snackbarText }}
    <v-btn
      color="primary"
      text
      @click="$store.commit('setSnackbar', '')"
    >
      close
    </v-btn>
  </v-snackbar>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'SnackbarNotification',
  data () {
    return {
      show: false
    }
  },
  computed: mapState([
    'snackbarText',
    'snackbar'
  ]),
  watch: {
    snackbar (newVal) {
      this.show = newVal
    }
  }
}
</script>
