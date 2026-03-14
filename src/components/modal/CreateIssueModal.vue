<template>
  <Teleport to="body">
    <div class="fixed inset-0 bg-atlassian-neutral-400/50 flex items-start justify-center pt-[60px] z-50" @click.self="close">
      <div class="w-[600px] bg-atlassian-neutral-0 rounded-lg shadow-jira-modal max-h-[calc(100vh-80px)] overflow-hidden flex flex-col">
        <div class="px-6 py-3 border-b border-atlassian-neutral-20 flex items-center justify-between">
          <h2 class="text-lg font-semibold text-atlassian-neutral-100">Create Issue</h2>
          <button class="p-1.5 hover:bg-atlassian-neutral-10 rounded" @click="close">
            <X class="w-4 h-4 text-atlassian-neutral-70" />
          </button>
        </div>

        <form @submit.prevent="handleSubmit" class="p-6 space-y-4">
          <div>
            <label class="block text-sm font-medium text-atlassian-neutral-100 mb-1">Summary *</label>
            <input 
              v-model="form.summary"
              type="text" 
              required
              class="w-full h-9 px-3 border border-atlassian-neutral-30 rounded text-sm text-atlassian-neutral-100 focus:outline-none focus:border-atlassian-blue-400"
              placeholder="Short description"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-atlassian-neutral-100 mb-1">Description</label>
            <textarea 
              v-model="form.description"
              class="w-full h-24 px-3 py-2 border border-atlassian-neutral-30 rounded text-sm text-atlassian-neutral-100 focus:outline-none focus:border-atlassian-blue-400 resize-none"
              placeholder="Add more details..."
            ></textarea>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-atlassian-neutral-100 mb-1">Status</label>
              <select 
                v-model="form.status"
                class="w-full h-9 px-3 border border-atlassian-neutral-30 rounded text-sm text-atlassian-neutral-100 bg-atlassian-neutral-0"
              >
                <option value="todo">To Do</option>
                <option value="inprogress">In Progress</option>
                <option value="done">Done</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-atlassian-neutral-100 mb-1">Priority</label>
              <select 
                v-model="form.priority"
                class="w-full h-9 px-3 border border-atlassian-neutral-30 rounded text-sm text-atlassian-neutral-100 bg-atlassian-neutral-0"
              >
                <option value="highest">Highest</option>
                <option value="high">High</option>
                <option value="medium">Medium</option>
                <option value="low">Low</option>
                <option value="lowest">Lowest</option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-atlassian-neutral-100 mb-1">Assignee</label>
              <select 
                v-model="form.assigneeId"
                class="w-full h-9 px-3 border border-atlassian-neutral-30 rounded text-sm text-atlassian-neutral-100 bg-atlassian-neutral-0"
              >
                <option :value="null">Unassigned</option>
                <option v-for="user in issueStore.users" :key="user.id" :value="user.id">{{ user.name }}</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-atlassian-neutral-100 mb-1">Story Points</label>
              <input 
                v-model.number="form.storyPoints"
                type="number"
                class="w-full h-9 px-3 border border-atlassian-neutral-30 rounded text-sm text-atlassian-neutral-100"
                placeholder="0"
              />
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-atlassian-neutral-100 mb-1">Labels (comma separated)</label>
            <input 
              v-model="form.labelsInput"
              type="text"
              class="w-full h-9 px-3 border border-atlassian-neutral-30 rounded text-sm text-atlassian-neutral-100 focus:outline-none focus:border-atlassian-blue-400"
              placeholder="bug, feature, urgent"
            />
          </div>

          <div class="flex justify-end gap-2 pt-4">
            <button 
              type="button"
              class="h-8 px-4 text-sm text-atlassian-neutral-70 hover:bg-atlassian-neutral-10 rounded transition-colors"
              @click="close"
            >
              Cancel
            </button>
            <button 
              type="submit"
              :disabled="loading"
              class="h-8 px-4 bg-atlassian-blue-400 text-white text-sm font-medium rounded hover:bg-atlassian-blue-500 transition-colors disabled:opacity-50"
            >
              {{ loading ? 'Creating...' : 'Create' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { X } from 'lucide-vue-next'
import { useIssueStore } from '../../stores/issues'
import { useAuthStore } from '../../stores/auth'

const emit = defineEmits(['close', 'created'])

const issueStore = useIssueStore()
const authStore = useAuthStore()

const loading = ref(false)

const form = reactive({
  summary: '',
  description: '',
  status: 'todo' as string,
  priority: 'medium' as string,
  assigneeId: null as string | null,
  storyPoints: null as number | null,
  labelsInput: ''
})

const close = () => {
  emit('close')
}

const handleSubmit = async () => {
  if (!form.summary.trim()) return
  
  loading.value = true
  try {
    const labels = form.labelsInput.split(',').map(l => l.trim()).filter(l => l)
    
    await issueStore.addIssue({
      summary: form.summary,
      description: form.description,
      status: form.status as 'todo' | 'inprogress' | 'done',
      priority: form.priority as 'highest' | 'high' | 'medium' | 'low' | 'lowest',
      assignee: issueStore.users.find(u => u.id === form.assigneeId) || null,
      reporter: authStore.user!,
      labels,
      storyPoints: form.storyPoints
    })
    
    emit('created')
    close()
  } finally {
    loading.value = false
  }
}
</script>