<template>
  <div>
    <h2>Cargo List</h2>
    <ul>
      <li v-for="cargo in cargos" :key="cargo.id">
        {{ cargo.id }} - {{ cargo.description }} ({{ cargo.status }})
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Cargo {
  id: number
  description: string
  weight: number
  origin_port: string
  destination_port: string
  booking_date: string
  status: string
}

const cargos = ref<Cargo[]>([])

onMounted(async () => {
  const res = await axios.get('http://localhost:8000/cargo/list')
  cargos.value = res.data
})
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}
</style>
