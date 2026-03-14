<template>
  <div class="w-4 h-4 flex items-center justify-center">
    <svg v-if="priority === 'highest'" viewBox="0 0 16 16" class="w-4 h-4">
      <path fill="#ff5630" d="M8 1.5L2.5 14h11L8 1.5z"/>
    </svg>
    <svg v-else-if="priority === 'high'" viewBox="0 0 16 16" class="w-4 h-4">
      <path fill="#ff5630" d="M8 3L3 14h10L8 3z" opacity="0.6"/>
    </svg>
    <svg v-else-if="priority === 'medium'" viewBox="0 0 16 16" class="w-4 h-4">
      <path fill="#ffab00" d="M8 4L4 14h8L8 4z"/>
    </svg>
    <svg v-else-if="priority === 'low'" viewBox="0 0 16 16" class="w-4 h-4">
      <path fill="#36b37e" d="M8 12l4-10H4l4 10z" opacity="0.6"/>
    </svg>
    <svg v-else viewBox="0 0 16 16" class="w-4 h-4">
      <path fill="#36b37e" d="M8 13l5-10H3l5 10z"/>
    </svg>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  priority: 'highest' | 'high' | 'medium' | 'low' | 'lowest'
}>()
</script>