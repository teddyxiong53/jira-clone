<template>
  <span 
    class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded text-xs font-medium"
    :class="statusClasses"
  >
    <span class="w-2 h-2 rounded-full" :class="dotClass"></span>
    {{ label }}
  </span>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  status: string
}>()

const label = computed(() => {
  const labels: Record<string, string> = {
    todo: 'To Do',
    inprogress: 'In Progress',
    done: 'Done'
  }
  return labels[props.status] || props.status
})

const statusClasses = computed(() => {
  const classes: Record<string, string> = {
    todo: 'bg-atlassian-neutral-20 text-atlassian-neutral-100',
    inprogress: 'bg-blue-100 text-blue-700',
    done: 'bg-green-100 text-green-700'
  }
  return classes[props.status] || ''
})

const dotClass = computed(() => {
  const classes: Record<string, string> = {
    todo: 'bg-atlassian-neutral-70',
    inprogress: 'bg-atlassian-blue-400',
    done: 'bg-atlassian-green-400'
  }
  return classes[props.status] || ''
})
</script>