<template>
  <div class="h-full flex flex-col">
    <div class="px-4 py-3 border-b border-atlassian-neutral-20 flex items-center justify-between">
      <h1 class="text-lg font-semibold text-atlassian-neutral-100">Board</h1>
      <div class="flex items-center gap-2">
        <button class="px-2 py-1 text-sm text-atlassian-neutral-70 hover:bg-atlassian-neutral-10 rounded flex items-center gap-1">
          <Filter class="w-4 h-4" />
          Filter
        </button>
        <button class="px-2 py-1 text-sm text-atlassian-neutral-70 hover:bg-atlassian-neutral-10 rounded">
          <MoreHorizontal class="w-4 h-4" />
        </button>
      </div>
    </div>
    
    <div class="flex-1 overflow-x-auto p-4">
      <div class="flex gap-4 h-full">
        <KanbanColumn 
          v-for="column in columns" 
          :key="column.key"
          :status="column.key"
          :label="column.label"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Filter, MoreHorizontal } from 'lucide-vue-next'
import KanbanColumn from './KanbanColumn.vue'

const columns = [
  { key: 'todo', label: 'To Do' },
  { key: 'inprogress', label: 'In Progress' },
  { key: 'done', label: 'Done' }
]
</script>