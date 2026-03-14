<template>
  <div class="h-screen flex flex-col bg-atlassian-neutral-10">
    <TopNav v-if="authStore.isAuthenticated()" />
    <div v-if="authStore.isAuthenticated()" class="flex flex-1 overflow-hidden">
      <SideNav />
      <main class="flex-1 overflow-auto">
        <router-view />
      </main>
    </div>
    <router-view v-else />
    <IssueModal v-if="uiStore.isModalOpen" />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import TopNav from './components/layout/TopNav.vue'
import SideNav from './components/layout/SideNav.vue'
import IssueModal from './components/modal/IssueModal.vue'
import { useUiStore } from './stores/ui'
import { useIssueStore } from './stores/issues'
import { useAuthStore } from './stores/auth'

const uiStore = useUiStore()
const issueStore = useIssueStore()
const authStore = useAuthStore()

onMounted(async () => {
  await authStore.initAuth()
  if (authStore.isAuthenticated()) {
    await Promise.all([issueStore.fetchIssues(), issueStore.fetchUsers()])
  }
})
</script>