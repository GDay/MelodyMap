<template>
  <v-layout>
    <v-flex xs8>
      {{ text }}
    </v-flex>
    <v-flex xs4>
      <v-btn icon small fab style="float:right" @click="closeModal">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: 'ModalHeader',
  props: {
    text: {
      type: String,
      default: '<USE text PROP>'
    }
  },
  methods: {
    closeModal () {
      this.$emit('onCloseModal')
    }
  }
}
</script>
