<template>
  <v-dialog
    v-model="value"
    width="600"
    persistent
  >
    <v-card>
      <v-card-title
        class="headline"
        primary-title
      >
        <modal-header text="Details" @onCloseModal="closeModal" />
      </v-card-title>

      <v-card-text>
        <h4>{{ item.title }}</h4>
        <p>{{ item.description }}</p>
        <v-subheader class="pl-0">
          Between {{ item.min_age }} and {{ item.max_age }} years old.
        </v-subheader>
        <v-divider />
        <send-message-form v-if="formOpened" :id="item.id" @closeModal="closeModal" />
        <v-btn v-if="!formOpened" block color="primary" @click="formOpened = true">
          Get in touch
        </v-btn>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import SendMessageForm from '@/components/listings/SendMessageForm'

export default {
  name: 'DetailModal',
  components: { SendMessageForm },
  props: {
    item: {
      type: Object,
      default: () => { return {} }
    },
    value: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      formOpened: false
    }
  },
  methods: {
    closeModal () {
      this.formOpened = false
      this.$emit('input', false)
    }
  }
}
</script>

<style scoped>
.theme--light.v-btn-toggle .v-btn.v-btn.active {
  background-color: #327AAD !important;
}
</style>
