<template>
  <div>
    <p v-if="!lieux || lieux.length === 0">Aucune donnée disponible.</p>
    <v-treeview
      v-else
      :items="lieux"
      item-key="id"
      :open-on-click="false"
      item-text="nomLieu"
      rounded
      hoverable
      activatable
      dense
      @update:active="onSelect"
    >
    <template v-slot:prepend="{ item, open }">
      <v-icon
        v-if="item.children && item.children.length > 0 && item.nomLieu !== 'Tous'"
        @click.stop="toggleNode(item)"
        :class="{ 'rotate-icon': open }"
      >
        {{ open ? 'mdi-triangle-down' : 'mdi-triangle-right' }}
      </v-icon>
      <span v-else class="tree-icon-placeholder"></span>
      {{ item.nomLieu }}
    </template>
      <template v-slot:label="{ item }">
        <span class="text-caption ml-2">{{ item.typeLieu }}</span>
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
      type: Array,
      required: true
    }
  },
  data() {
    return {
      openNodes: new Set(),
    };
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
    },
    toggleNode(item) {
      if (this.openNodes.has(item.id)) {
        this.openNodes.delete(item.id);
      } else {
        this.openNodes.add(item.id);
      }
      this.$forceUpdate();
    },
  }
}
</script>

<style scoped>
.text-caption {
  color: #666;
  font-size: 0.75rem;
}

.tree-icon-placeholder {
  display: inline-block;
  width: 24px;
  height: 24px;
  margin-right: 4px;
}

.rotate-icon {
  transform: rotate(180deg);
}

.v-icon {
  transition: transform 0.3s ease;
}
</style>