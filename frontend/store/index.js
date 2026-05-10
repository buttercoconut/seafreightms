import { defineStore } from 'pinia'
import api from '../services/api.js'

export const useCargoStore = defineStore('cargo', {
  state: () => ({
    cargos: []
  }),
  actions: {
    async fetchCargos() {
      const data = await api.getCargos()
      this.cargos = data
      return data
    }
  }
})
