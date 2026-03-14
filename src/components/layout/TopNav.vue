<template>
  <header class="h-12 bg-atlassian-neutral-0 border-b border-atlassian-neutral-20 flex items-center px-3 shrink-0">
    <div class="flex items-center gap-3">
      <div class="flex items-center gap-2 cursor-pointer hover:bg-atlassian-neutral-10 px-2 py-1 rounded">
        <svg class="w-6 h-6" viewBox="0 0 32 32" fill="none">
          <rect width="32" height="32" rx="4" fill="#0052CC"/>
          <path d="M8 10h6v12H8V10z" fill="white"/>
          <path d="M16 10h6v12h-6V10z" fill="white" opacity="0.7"/>
        </svg>
        <span class="font-semibold text-atlassian-neutral-100 text-sm">Project Name</span>
        <ChevronDown class="w-4 h-4 text-atlassian-neutral-70" />
      </div>
    </div>

    <div class="flex-1 flex justify-center">
      <div class="relative w-[320px]">
        <Search class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-atlassian-neutral-60" />
        <input 
          type="text" 
          placeholder="Search issues..."
          class="w-full h-7 pl-9 pr-3 bg-atlassian-neutral-10 border border-atlassian-neutral-20 rounded text-sm text-atlassian-neutral-100 placeholder-atlassian-neutral-60 focus:outline-none focus:border-atlassian-blue-300"
          v-model="searchQuery"
          @input="handleSearch"
        />
        <div class="absolute right-2 top-1/2 -translate-y-1/2 text-xs text-atlassian-neutral-60 bg-atlassian-neutral-20 px-1.5 py-0.5 rounded">/</div>
      </div>
    </div>

    <div class="flex items-center gap-1">
      <button class="flex items-center gap-1.5 h-7 px-2 bg-atlassian-blue-400 text-white text-sm font-medium rounded hover:bg-atlassian-blue-500 transition-colors">
        <Plus class="w-4 h-4" />
        <span>Create</span>
        <ChevronDown class="w-3 h-3" />
      </button>
      
      <button class="relative p-1.5 text-atlassian-neutral-70 hover:bg-atlassian-neutral-10 rounded transition-colors">
        <Bell class="w-5 h-5" />
        <span class="absolute top-0.5 right-0.5 w-2 h-2 bg-atlassian-red-400 rounded-full"></span>
      </button>
      
      <button class="p-1.5 text-atlassian-neutral-70 hover:bg-atlassian-neutral-10 rounded transition-colors">
        <HelpCircle class="w-5 h-5" />
      </button>
      
      <div class="ml-2 flex items-center gap-2 cursor-pointer hover:bg-atlassian-neutral-10 px-1.5 py-1 rounded" @click="showUserMenu = !showUserMenu">
        <img v-if="authStore.user" :src="authStore.user.avatar" alt="User" class="w-6 h-6 rounded-full" />
        <span v-if="authStore.user" class="text-sm text-atlassian-neutral-100">{{ authStore.user.name }}</span>
      </div>
      
      <div v-if="showUserMenu" class="absolute right-3 top-10 bg-atlassian-neutral-0 border border-atlassian-neutral-20 rounded shadow-jira-card py-1 z-50">
        <button 
          class="w-full px-4 py-2 text-left text-sm text-atlassian-neutral-100 hover:bg-atlassian-neutral-10"
          @click="handleLogout"
        >
          Log out
        </button>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { Search, ChevronDown, Plus, Bell, HelpCircle } from 'lucide-vue-next'
import { useUiStore } from '../../stores/ui'
import { useAuthStore } from '../../stores/auth'

const router = useRouter()
const uiStore = useUiStore()
const authStore = useAuthStore()
const searchQuery = ref('')
const showUserMenu = ref(false)

const handleSearch = (e: Event) => {
  const target = e.target as HTMLInputElement
  uiStore.setSearchQuery(target.value)
}

const handleLogout = () => {
  authStore.logout()
  showUserMenu.value = false
  router.push('/login')
}
</script>