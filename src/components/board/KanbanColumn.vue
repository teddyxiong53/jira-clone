<template>
  <div class="w-[280px] flex-shrink-0 flex flex-col bg-atlassian-neutral-10 rounded-lg max-h-full">
    <div class="px-3 py-2 flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="text-sm font-medium text-atlassian-neutral-100">{{ label }}</span>
        <span class="text-xs text-atlassian-neutral-70 bg-atlassian-neutral-20 px-1.5 py-0.5 rounded">
          {{ columnIssues.length }}
        </span>
      </div>
      <button class="p-1 hover:bg-atlassian-neutral-20 rounded">
        <Plus class="w-4 h-4 text-atlassian-neutral-70" />
      </button>
    </div>
    
    <div 
      class="flex-1 overflow-y-auto p-2 space-y-2"
      @dragover.prevent
      @drop="onDrop"
    >
      <VueDraggable 
        v-model="columnIssues" 
        group="issues"
        :animation="200"
        ghost-class="opacity-50"
        class="space-y-2 min-h-[100px]"
      >
        <IssueCard 
          v-for="issue in columnIssues" 
          :key="issue.id"
          :issue="issue"
        />
      </VueDraggable>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { VueDraggable } from 'vue-draggable-plus'
import { Plus } from 'lucide-vue-next'
import { useIssueStore, type Issue } from '../../stores/issues'
import IssueCard from '../common/IssueCard.vue'

const props = defineProps<{
  status: string
  label: string
}>()

const issueStore = useIssueStore()

const columnIssues = computed({
  get: () => issueStore.issues.filter(issue => issue.status === props.status),
  set: (value: Issue[]) => {
    value.forEach(issue => {
      if (issue.status !== props.status) {
        issueStore.moveIssue(issue.id, props.status)
      }
    })
  }
})

const onDrop = (e: DragEvent) => {
  const data = e.dataTransfer?.getData('text/plain')
  if (data) {
    issueStore.moveIssue(data, props.status)
  }
}
</script>