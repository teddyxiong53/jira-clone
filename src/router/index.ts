import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      redirect: '/board'
    },
    {
      path: '/board',
      name: 'board',
      component: () => import('../views/BoardView.vue')
    },
    {
      path: '/backlog',
      name: 'backlog',
      component: () => import('../views/BacklogView.vue')
    },
    {
      path: '/issues',
      name: 'issues',
      component: () => import('../views/IssuesListView.vue')
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue')
    }
  ]
})

export default router