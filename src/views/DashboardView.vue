<template>
  <div class="p-6">
    <h1 class="text-xl font-semibold text-atlassian-neutral-100 mb-6">Your work</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div class="bg-atlassian-neutral-0 rounded-lg p-4 shadow-jira-card">
        <div class="flex items-center gap-2 mb-4">
          <Clock class="w-5 h-5 text-atlassian-blue-400" />
          <span class="font-medium text-atlassian-neutral-100">Assigned to me</span>
        </div>
        <div class="space-y-2">
          <div 
            v-for="issue in assignedIssues" 
            :key="issue.id"
            class="flex items-center gap-3 p-2 hover:bg-atlassian-neutral-10 rounded cursor-pointer"
            @click="openIssue(issue.id)"
          >
            <StatusBadge :status="issue.status" />
            <span class="text-sm text-atlassian-neutral-100 flex-1 truncate">{{ issue.summary }}</span>
            <span class="text-xs text-atlassian-neutral-70">{{ issue.key }}</span>
          </div>
          <div v-if="assignedIssues.length === 0" class="text-sm text-atlassian-neutral-70">No issues assigned</div>
        </div>
      </div>

      <div class="bg-atlassian-neutral-0 rounded-lg p-4 shadow-jira-card">
        <div class="flex items-center gap-2 mb-4">
          <TrendingUp class="w-5 h-5 text-atlassian-green-400" />
          <span class="font-medium text-atlassian-neutral-100">Recent updates</span>
        </div>
        <div class="space-y-2">
          <div 
            v-for="issue in recentIssues" 
            :key="issue.id"
            class="flex items-center gap-3 p-2 hover:bg-atlassian-neutral-10 rounded cursor-pointer"
            @click="openIssue(issue.id)"
          >
            <StatusBadge :status="issue.status" />
            <span class="text-sm text-atlassian-neutral-100 flex-1 truncate">{{ issue.summary }}</span>
            <span class="text-xs text-atlassian-neutral-70">{{ formatDate(issue.updated) }}</span>
          </div>
        </div>
      </div>

      <div class="bg-atlassian-neutral-0 rounded-lg p-4 shadow-jira-card">
        <div class="flex items-center gap-2 mb-4">
          <BarChart2 class="w-5 h-5 text-atlassian-yellow-400" />
          <span class="font-medium text-atlassian-neutral-100">Quick stats</span>
        </div>
        <div class="space-y-3">
          <div class="flex justify-between items-center">
            <span class="text-sm text-atlassian-neutral-70">Total issues</span>
            <span class="text-lg font-semibold text-atlassian-neutral-100">{{ issueStore.issues.length }}</span>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-sm text-atlassian-neutral-70">To Do</span>
            <span class="text-lg font-semibold text-atlassian-neutral-100">{{ todoCount }}</span>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-sm text-atlassian-neutral-70">In Progress</span>
            <span class="text-lg font-semibold text-atlassian-neutral-100">{{ inProgressCount }}</span>
          </div>
          <div class="flex justify-between items-center">
            <span class="text-sm text-atlassian-neutral-70">Done</span>
            <span class="text-lg font-semibold text-atlassian-neutral-100">{{ doneCount }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { Clock, TrendingUp, BarChart2 } from 'lucide-vue-next'
import dayjs from 'dayjs'
import { useIssueStore } from '../stores/issues'
import { useUiStore } from '../stores/ui'
import StatusBadge from '../components/common/StatusBadge.vue'

const issueStore = useIssueStore()
const uiStore = useUiStore()

const assignedIssues = computed(() => {
  return issueStore.issues.filter(issue => issue.assignee?.id === '1').slice(0, 5)
})

const recentIssues = computed(() => {
  return [...issueStore.issues]
    .sort((a, b) => new Date(b.updated).getTime() - new Date(a.updated).getTime())
    .slice(0, 5)
})

const todoCount = computed(() => issueStore.issues.filter(i => i.status === 'todo').length)
const inProgressCount = computed(() => issueStore.issues.filter(i => i.status === 'inprogress').length)
const doneCount = computed(() => issueStore.issues.filter(i => i.status === 'done').length)

const formatDate = (date: string) => {
  return dayjs(date).format('MMM d')
}

const openIssue = (id: string) => {
  uiStore.openModal(id)
}
</script>