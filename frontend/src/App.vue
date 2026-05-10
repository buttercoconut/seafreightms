<template>
  <div id="app">
    <h1>Sea Freight Management System</h1>
    <CargoList />
  </div>
</template>

<script setup lang="ts">
import CargoList from './components/CargoList.vue'
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
