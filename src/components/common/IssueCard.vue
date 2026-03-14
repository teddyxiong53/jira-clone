<template>
  <div 
    class="bg-atlassian-neutral-0 rounded shadow-jira-card p-2 cursor-pointer hover:border hover:border-atlassian-blue-400 hover:bg-atlassian-neutral-10 transition-all"
    @click="openModal"
  >
    <div class="text-[#0052cc] text-xs font-medium mb-1">{{ issue.key }}</div>
    <div class="text-[14px] leading-tight text-atlassian-neutral-100 mb-2 line-clamp-2">{{ issue.summary }}</div>
    
    <div class="flex items-center justify-between mt-2">
      <div class="flex items-center gap-1.5 flex-wrap">
        <span 
          v-for="label in issue.labels" 
          :key="label"
          class="px-1.5 py-0.5 text-[10px] rounded bg-atlassian-blue-50 text-atlassian-blue-500"
        >
          {{ label }}
        </span>
      </div>
      
      <div class="flex items-center gap-2">
        <div v-if="issue.storyPoints" class="text-xs text-atlassian-neutral-70 bg-atlassian-neutral-20 px-1.5 py-0.5 rounded">
          {{ issue.storyPoints }}
        </div>
        <PriorityIcon :priority="issue.priority" />
        <img 
          v-if="issue.assignee" 
          :src="issue.assignee.avatar" 
          :alt="issue.assignee.name"
          class="w-6 h-6 rounded-full ring-2 ring-white"
        />
        <div v-else class="w-6 h-6 rounded-full bg-atlassian-neutral-30"></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Issue } from '../../stores/issues'
import { useUiStore } from '../../stores/ui'
import PriorityIcon from './PriorityIcon.vue'

const props = defineProps<{
  issue: Issue
}>()

const uiStore = useUiStore()

const openModal = () => {
  uiStore.openModal(props.issue.id)
}
</script>