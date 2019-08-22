<template class="d-none d-sm-flex">
  <v-card
    max-width="344"
    class="mx-auto floating hidden-sm-and-down"
  >
    <v-card-title>Results</v-card-title>

    <v-card-text class="pa-0">
      <div v-if="items.length" class="results">
        <v-list-item
          v-for="(i, index) in items"
          :key="index"
          two-line
          @click="openItem(i)"
        >
          <v-list-item-content
            :class="{ 'border-left' : i.hover }"
          >
            <v-list-item-title>{{ i.title }}</v-list-item-title>
            <v-list-item-subtitle>{{ i.description }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </div>
      <div v-else>
        <p class="ma-4">
          There are no listings here.
        </p>
      </div>
      <v-btn
        class="ma-4 mt-1"
        color="primary"
        @click="$emit('onCreateClick')"
      >
        Add your listing
      </v-btn>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'ResultsCard',
  props: {
    loading: {
      type: Boolean,
      required: true
    },
    items: {
      type: Array,
      required: true
    }
  },
  methods: {
    openItem (item) {
      this.$emit('onItemClick', item)
    }
  }
}
</script>

<style scoped>
.floating {
  position: absolute;
  margin-left: 60px !important;
  margin-top: 30px;
  max-height: 400px;
}
.results {
  max-height: 100%;
}
.border-left {
  margin-left: 10px;
}
.results {
  overflow-y: auto;
  max-height: 300px;
}
</style>
