<template>
  <div>
    <p v-if="!lieux || lieux.length === 0">Aucune donnée de localisation disponible.</p>
    <v-treeview
      v-else
      :items="lieux"
      item-key="id"
      open-on-click
      item-text="nomLieu"
      rounded
      hoverable
      activatable
      dense
      @update:active="onSelect"
    >
      <template v-slot:prepend="{ item,open }">
        {{item.nomLieu}}
      </template>
      <template v-slot:label="{ item }">
      </template>
      
    </v-treeview>
  </div>
</template>

<script>
import { VTreeview } from 'vuetify/labs/VTreeview';

export default {
  name: 'LieuxExplorer',
  components: {
    VTreeview
  },
  props: {
    lieux: {
      required: true
    }
  },
  methods: {
    onSelect(items) {
      console.log('Item sélectionné:', items);
      if (items.length > 0) {
        const selectedItem = this.findItem(this.lieux, items[0]);
        if (selectedItem) {
          console.log('Item trouvé:', selectedItem);
          this.$emit('select-lieu', selectedItem);
        }
      }
    },
    findItem(items, id) {
      for (const item of items) {
        if (item.id === id) {
          return item;
        }
        if (item.children) {
          const found = this.findItem(item.children, id);
          if (found) {
            return found;
          }
        }
      }
      return null;
    }
  }
}
</script>

<style scoped>
.text-caption {
  color: #666;
  font-size: 0.75rem;
}
</style>
