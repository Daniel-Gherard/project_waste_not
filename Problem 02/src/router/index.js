import { createRouter, createWebHistory } from 'vue-router'
import DebounceInputView from '../views/DebounceInputView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: DebounceInputView
    }
  ]
})

export default router
