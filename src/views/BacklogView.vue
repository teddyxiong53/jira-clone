<template>
  <div class="h-full flex flex-col">
    <div class="px-4 py-3 border-b border-atlassian-neutral-20">
      <h1 class="text-lg font-semibold text-atlassian-neutral-100">Backlog</h1>
    </div>
    
    <div class="flex-1 overflow-y-auto p-4">
      <div class="mb-6">
        <h2 class="text-sm font-medium text-atlassian-neutral-100 mb-3">To Do</h2>
        <div class="space-y-2">
          <div 
            v-for="issue in todoIssues" 
            :key="issue.id"
            class="bg-atlassian-neutral-0 rounded shadow-jira-card p-3 cursor-pointer hover:border hover:border-atlassian-blue-400"
            @click="openIssue(issue.id)"
          >
            <div class="flex items-center justify-between mb-2">
              <span class="text-[#0052cc] text-xs font-medium">{{ issue.key }}</span>
              <PriorityIcon :priority="issue.priority" />
            </div>
            <div class="text-sm text-atlassian-neutral-100 mb-2">{{ issue.summary }}</div>
            <div class="flex items-center gap-2">
              <span 
                v-for="label in issue.labels" 
                :key="label"
                class="px-1.5 py-0.5 text-[10px] rounded bg-atlassian-blue-50 text-atlassian-blue-500"
              >
                {{ label }}
              </span>
              <img v-if="issue.assignee" :src="issue.assignee.avatar" class="w-5 h-5 rounded-full" />
            </div>
          </div>
          <div v-if="todoIssues.length === 0" class="text-sm text-atlassian-neutral-70">No issues in backlog</div>
        </div>
      </div>

      <div>
        <h2 class="text-sm font-medium text-atlassian-neutral-100 mb-3">In Progress</h2>
        <div class="space-y-2">
          <div 
            v-for="issue in inProgressIssues" 
            :key="issue.id"
            class="bg-atlassian-neutral-0 rounded shadow-jira-card p-3 cursor-pointer hover:border hover:border-atlassian-blue-400"
            @click="openIssue(issue.id)"
          >
            <div class="flex items-center justify-between mb-2">
              <span class="text-[#0052cc] text-xs font-medium">{{ issue.key }}</span>
              <PriorityIcon :priority="issue.priority" />
            </div>
            <div class="text-sm text-atlassian-neutral-100 mb-2">{{ issue.summary }}</div>
            <div class="flex items-center gap-2">
              <img v-if="issue.assignee" :src="issue.assignee.avatar" class="w-5 h-5 rounded-full" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useIssueStore } from '../stores/issues'
import { useUiStore } from '../stores/ui'
import PriorityIcon from '../components/common/PriorityIcon.vue'

const issueStore = useIssueStore()
const uiStore = useUiStore()

const todoIssues = computed(() => issueStore.issues.filter(i => i.status === 'todo'))
const inProgressIssues = computed(() => issueStore.issues.filter(i => i.status === 'inprogress'))

const openIssue = (id: string) => {
  uiStore.openModal(id)
}
</script>