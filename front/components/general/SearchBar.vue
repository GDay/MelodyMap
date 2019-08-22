<template>
  <v-autocomplete
    :value="$store.state.selectedPlace"
    :items="entries"
    :search-input.sync="search"
    placeholder="Search for a zipcode or place"
    return-object
    style="margin-top: 25px"
    text
    item-text="display_name"
    hide-no-data
    clearable
    :solo-inverted="inverted"
    :label="label"
    @input="updatePlace"
  />
</template>

<script>
export default {
  name: 'SearchBar',
  props: {
    inverted: {
      default: true,
      type: Boolean
    },
    label: {
      default: '',
      type: String
    }
  },
  data () {
    return {
      entries: [],
      search: '',
      searchTimeout: undefined
    }
  },
  watch: {
    search (val) {
      clearTimeout(this.searchTimeout)
      this.searchTimeout = setTimeout(() => {
        this.$axios(`https://nominatim.openstreetmap.org/search/query?q=${this.search}&format=json`).then((res) => {
          this.entries = res.data
        }).catch((err) => {
          if (err) {
            this.$store.dispatch('showSnackbar', 'Oh, something went wrong. Could not get places')
          }
        }).finally(() => {
          this.isLoading = false
        })
      }, 500)
    }
  },
  methods: {
    updatePlace (val) {
      this.$store.commit('changePlace', val)
    }
  }
}
</script>
