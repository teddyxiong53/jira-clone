<template>
  <img 
    :src="src" 
    :alt="alt"
    class="rounded-full"
    :class="sizeClasses"
  />
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  src: string
  alt?: string
  size?: 'sm' | 'md' | 'lg'
}>(), {
  size: 'md'
})

const sizeClasses = computed(() => {
  const classes = {
    sm: 'w-6 h-6',
    md: 'w-8 h-8',
    lg: 'w-10 h-10'
  }
  return classes[props.size]
})
</script>