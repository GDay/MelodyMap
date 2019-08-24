<template>
  <v-layout>
    <l-map
      :zoom="$store.state.zoom"
      style="width: 100% z-index: 0 !important"
      :center="$store.state.center"
      @update:bounds="boundsUpdated"
      @update:zoom="$store.commit('setZoom', ...arguments[0])"
    >
      <l-tile-layer :url="url" />
      <l-marker
        v-for="(i, index) in items"
        :key="index"
        :lat-lng="[i.lat, i.lon]"
        @mouseover="toggleBorder(i)"
        @mouseleave="toggleBorder(i)"
        @click="openItem(i)"
      />
    </l-map>
    <results-card
      :items="items"
      :loading="loading"
      @onItemClick="openItem"
      @onCreateClick="addModalOpen = true"
    />
    <AddModal
      v-model="addModalOpen"
      :instruments="instruments"
    />
    <DetailModal
      v-model="detailModalOpen"
      :item="item"
    />
  </v-layout>
</template>

<script>
import ResultsCard from '@/components/ResultsCard'
import AddModal from '@/components/listings/AddModal'
import DetailModal from '@/components/listings/DetailModal'

export default {
  components: { ResultsCard, AddModal, DetailModal },
  data () {
    return {
      url: 'https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png',
      zoom: 3,
      loading: false,
      modalOpen: true,
      addModalOpen: false,
      detailModalOpen: false,
      items: [],
      item: {},
      instruments: []
    }
  },
  mounted () {
    this.$user.getCSRFToken()
    this.$adverts.getInstruments().then((data) => {
      this.instruments = data
    })
    this.$store.commit('setZoom', 14)
  },
  methods: {
    boundsUpdated (bounds) {
      this.loading = true
      this.$adverts.search(bounds).then((data) => {
        this.items = data
      }).finally(() => {
        this.loading = false
      })
    },
    openItem (item) {
      this.item = item
      this.detailModalOpen = true
    },
    toggleBorder (item) {
      item.hover = !item.hover
    }
  }
}
</script>
