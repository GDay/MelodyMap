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
        <modal-header text="Add listing" @onCloseModal="closeModal" />
      </v-card-title>

      <v-card-text>
        <v-form>
          <v-btn-toggle v-model="listing.is_band" active-class="active">
            <v-btn color="secondary" :value="1">
              Band looking for musician
            </v-btn>
            <v-btn color="secondary" :value="0">
              Musician looking for band
            </v-btn>
          </v-btn-toggle>
          <div v-if="'is_band' in listing">
            <v-text-field
              v-model="listing.title"
              label="Title"
              class="mt-4"
              :placeholder="(listing.is_band) ? 'We are looking for a guitarist!' : 'Guitarist looking for a band'"
              :error-messages="errors.title"
              @keyup="errors.title=''"
            />
            <v-textarea
              v-model="listing.description"
              label="Description"
              :placeholder="(listing.is_band) ? 'Hi, we are...' : 'Hi, I am...'"
              :error-messages="errors.description"
              @keyup="errors.description=''"
            />
            <search-bar :inverted="false" label="Where?" />
            <v-select
              v-model="listing.instrument"
              :items="instruments"
              chips
              :label="(listing.is_band) ? 'We are looking for a' : 'I am a'"
              :error-messages="errors.instrument"
              item-text="name"
              multiple
              return-object
              outlined
              @keyup="errors.instrument=''"
            />
            <v-subheader class="pl-0 pb-3">
              Age preference
            </v-subheader>
            <v-range-slider
              v-model="listing.range"
              :max="max"
              :min="min"
              hide-details
              thumb-label="always"
              class="align-center mt-4"
            />
          </div>
        </v-form>
      </v-card-text>

      <v-divider />

      <v-card-actions v-if="'is_band' in listing">
        <v-spacer />
        <v-btn block :loading="loading" color="primary" @click="submit">
          Place listing
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import SearchBar from '@/components/general/SearchBar'
export default {
  name: 'AddModal',
  components: { SearchBar },
  props: {
    value: {
      type: Boolean,
      default: false
    },
    instruments: {
      type: Array,
      default: () => { return [] }
    }
  },
  data () {
    return {
      loading: false,
      signupModalOpen: false,
      listing: { range: [13, 99] },
      errors: {},
      max: 99,
      min: 13,
      range: [13, 99]
    }
  },
  methods: {
    submit () {
      if (!this.$auth.loggedIn) {
        this.$store.commit('toggleSignupModal')
        return
      }
      this.loading = true
      this.listing.lat = this.$store.state.center[0]
      this.listing.lon = this.$store.state.center[1]
      this.$adverts.add(this.listing).then((item) => {
        this.closeModal()
      }).catch((error) => {
        this.errors = error
      }).finally(() => {
        this.loading = false
      })
    },
    goToPasswordReset () {
      // this.loading = true
    },
    closeModal () {
      this.$emit('input', false)
      this.listing = { range: [13, 99] }
      this.errors = {}
    }
  }
}
</script>

<style scoped>
.theme--light.v-btn-toggle .v-btn.v-btn.active {
  background-color: #327AAD !important;
}
</style>
