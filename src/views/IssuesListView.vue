<template>
  <div class="h-full flex flex-col">
    <div class="px-4 py-3 border-b border-atlassian-neutral-20 flex items-center justify-between">
      <h1 class="text-lg font-semibold text-atlassian-neutral-100">Issues</h1>
      <div class="flex items-center gap-2">
        <button class="px-2 py-1 text-sm text-atlassian-neutral-70 hover:bg-atlassian-neutral-10 rounded">
          <Filter class="w-4 h-4" />
        </button>
        <button class="px-2 py-1 text-sm text-atlassian-neutral-70 hover:bg-atlassian-neutral-10 rounded">
          <Settings class="w-4 h-4" />
        </button>
      </div>
    </div>
    
    <div class="flex-1 overflow-auto">
      <table class="w-full">
        <thead class="bg-atlassian-neutral-10 sticky top-0">
          <tr class="text-left text-xs font-medium text-atlassian-neutral-70 uppercase">
            <th class="px-4 py-2 w-12">Type</th>
            <th class="px-4 py-2 w-24">Key</th>
            <th class="px-4 py-2">Summary</th>
            <th class="px-4 py-2 w-28">Status</th>
            <th class="px-4 py-2 w-20">Priority</th>
            <th class="px-4 py-2 w-32">Assignee</th>
            <th class="px-4 py-2 w-20">Points</th>
          </tr>
        </thead>
        <tbody>
          <tr 
            v-for="issue in issueStore.issues" 
            :key="issue.id"
            class="border-b border-atlassian-neutral-20 hover:bg-atlassian-neutral-10 cursor-pointer"
            @click="openIssue(issue.id)"
          >
            <td class="px-4 py-2">
              <div class="w-5 h-5 rounded bg-atlassian-blue-400 flex items-center justify-center">
                <Square class="w-3 h-3 text-white" />
              </div>
            </td>
            <td class="px-4 py-2">
              <span class="text-[#0052cc] text-xs font-medium">{{ issue.key }}</span>
            </td>
            <td class="px-4 py-2">
              <span class="text-sm text-atlassian-neutral-100">{{ issue.summary }}</span>
            </td>
            <td class="px-4 py-2">
              <StatusBadge :status="issue.status" />
            </td>
            <td class="px-4 py-2">
              <PriorityIcon :priority="issue.priority" />
            </td>
            <td class="px-4 py-2">
              <div v-if="issue.assignee" class="flex items-center gap-2">
                <img :src="issue.assignee.avatar" class="w-5 h-5 rounded-full" />
                <span class="text-sm text-atlassian-neutral-80">{{ issue.assignee.name }}</span>
              </div>
              <span v-else class="text-sm text-atlassian-neutral-70">Unassigned</span>
            </td>
            <td class="px-4 py-2">
              <span v-if="issue.storyPoints" class="text-sm text-atlassian-neutral-70">{{ issue.storyPoints }}</span>
              <span v-else class="text-sm text-atlassian-neutral-50">-</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Filter, Settings, Square } from 'lucide-vue-next'
import { useIssueStore } from '../stores/issues'
import { useUiStore } from '../stores/ui'
import StatusBadge from '../components/common/StatusBadge.vue'
import PriorityIcon from '../components/common/PriorityIcon.vue'

const issueStore = useIssueStore()
const uiStore = useUiStore()

const openIssue = (id: string) => {
  uiStore.openModal(id)
}
</script>