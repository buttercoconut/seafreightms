<template>
  <div>
    <h2>Cargo List</h2>
    <ul>
      <li v-for="cargo in cargos" :key="cargo.id">
        {{ cargo.id }} - {{ cargo.description }} ({{ cargo.weight }} kg)
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCargoStore } from '../store/cargo'

const cargoStore = useCargoStore()
const cargos = ref([])

onMounted(async () => {
  const data = await cargoStore.fetchCargos()
  cargos.value = data
})
</script>
