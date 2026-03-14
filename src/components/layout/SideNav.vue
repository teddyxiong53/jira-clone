<template>
  <aside 
    class="bg-atlassian-neutral-0 border-r border-atlassian-neutral-20 flex flex-col transition-all duration-200"
    :class="[uiStore.isSideNavCollapsed ? 'w-12' : 'w-60']"
  >
    <nav class="flex-1 py-2">
      <div class="px-3 mb-4">
        <button 
          @click="uiStore.toggleSideNav"
          class="w-full flex items-center gap-2 px-2 py-1.5 text-sm text-atlassian-neutral-70 hover:bg-atlassian-neutral-10 rounded transition-colors"
        >
          <Menu class="w-5 h-5" />
          <span v-if="!uiStore.isSideNavCollapsed" class="font-medium">Collapse</span>
        </button>
      </div>

      <div class="space-y-0.5">
        <router-link 
          v-for="item in navItems" 
          :key="item.path"
          :to="item.path"
          class="flex items-center gap-3 px-3 py-1.5 text-sm text-atlassian-neutral-80 hover:bg-atlassian-neutral-10 transition-colors"
          :class="{ 'bg-atlassian-neutral-10': $route.path === item.path }"
        >
          <component :is="item.icon" class="w-5 h-5 shrink-0" />
          <span v-if="!uiStore.isSideNavCollapsed">{{ item.label }}</span>
        </router-link>
      </div>

      <div v-if="!uiStore.isSideNavCollapsed" class="mt-6 px-3">
        <div class="text-xs font-medium text-atlassian-neutral-70 uppercase tracking-wider mb-2 px-2">Recent</div>
        <div class="space-y-0.5">
          <div 
            v-for="project in recentProjects" 
            :key="project.id"
            class="flex items-center gap-2 px-2 py-1.5 text-sm text-atlassian-neutral-80 hover:bg-atlassian-neutral-10 rounded cursor-pointer"
          >
            <div class="w-5 h-5 rounded bg-atlassian-blue-400 flex items-center justify-center text-white text-xs font-medium">{{ project.initials }}</div>
            <span>{{ project.name }}</span>
          </div>
        </div>
      </div>

      <div v-if="!uiStore.isSideNavCollapsed" class="mt-4 px-3">
        <div class="text-xs font-medium text-atlassian-neutral-70 uppercase tracking-wider mb-2 px-2">Starred</div>
        <div class="space-y-0.5">
          <div 
            v-for="project in starredProjects" 
            :key="project.id"
            class="flex items-center gap-2 px-2 py-1.5 text-sm text-atlassian-neutral-80 hover:bg-atlassian-neutral-10 rounded cursor-pointer"
          >
            <div class="w-5 h-5 rounded bg-atlassian-green-400 flex items-center justify-center text-white text-xs font-medium">{{ project.initials }}</div>
            <span>{{ project.name }}</span>
          </div>
        </div>
      </div>
    </nav>

    <div class="border-t border-atlassian-neutral-20 py-2">
      <div class="space-y-0.5">
        <div class="flex items-center gap-3 px-3 py-1.5 text-sm text-atlassian-neutral-80 hover:bg-atlassian-neutral-10 cursor-pointer">
          <Grid3x3 class="w-5 h-5" />
          <span v-if="!uiStore.isSideNavCollapsed">Apps</span>
        </div>
        <div class="flex items-center gap-3 px-3 py-1.5 text-sm text-atlassian-neutral-80 hover:bg-atlassian-neutral-10 cursor-pointer">
          <Settings class="w-5 h-5" />
          <span v-if="!uiStore.isSideNavCollapsed">Settings</span>
        </div>
      </div>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useUiStore } from '../../stores/ui'
import { LayoutDashboard, Kanban, ListTodo, List, Menu, Grid3x3, Settings } from 'lucide-vue-next'

const uiStore = useUiStore()

const navItems = [
  { path: '/dashboard', label: 'Your work', icon: LayoutDashboard },
  { path: '/board', label: 'Board', icon: Kanban },
  { path: '/backlog', label: 'Backlog', icon: ListTodo },
  { path: '/issues', label: 'Issues', icon: List },
]

const recentProjects = ref([
  { id: '1', name: 'Frontend App', initials: 'FA' },
  { id: '2', name: 'Backend API', initials: 'BA' },
])

const starredProjects = ref([
  { id: '3', name: 'Mobile App', initials: 'MA' },
])
</script>