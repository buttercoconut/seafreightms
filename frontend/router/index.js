import { createRouter, createWebHistory } from 'vue-router'
import CargoList from '../components/CargoList.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: CargoList
  }
]

export default routes
