<template>
  <Teleport to="body">
    <div class="fixed inset-0 bg-atlassian-neutral-400/50 flex items-start justify-center pt-[60px] z-50" @click.self="close">
      <div class="w-[960px] bg-atlassian-neutral-0 rounded-lg shadow-jira-modal max-h-[calc(100vh-80px)] overflow-hidden flex flex-col">
        <div class="px-6 py-3 border-b border-atlassian-neutral-20 flex items-center justify-between">
          <div class="flex items-center gap-3">
            <StatusBadge :status="issue?.status || 'todo'" />
            <span class="text-sm text-atlassian-neutral-70">{{ issue?.key }}</span>
          </div>
          <div class="flex items-center gap-2">
            <button class="p-1.5 hover:bg-atlassian-neutral-10 rounded">
              <Maximize2 class="w-4 h-4 text-atlassian-neutral-70" />
            </button>
            <button class="p-1.5 hover:bg-atlassian-neutral-10 rounded" @click="close">
              <X class="w-4 h-4 text-atlassian-neutral-70" />
            </button>
          </div>
        </div>

        <div class="flex-1 overflow-y-auto">
          <div class="flex">
            <div class="flex-1 p-6 border-r border-atlassian-neutral-20">
              <input 
                v-model="editSummary"
                class="w-full text-lg font-semibold text-atlassian-neutral-100 border-none outline-none mb-4 bg-transparent"
                placeholder="Summary"
              />
              
              <div class="mb-6">
                <div class="flex items-center gap-2 mb-2">
                  <span class="text-sm font-medium text-atlassian-neutral-100">Description</span>
                </div>
                <textarea 
                  v-model="editDescription"
                  class="w-full min-h-[150px] p-3 border border-atlassian-neutral-20 rounded bg-atlassian-neutral-10 text-atlassian-neutral-100 text-sm resize-none focus:outline-none focus:border-atlassian-blue-300"
                  placeholder="Add a description..."
                ></textarea>
              </div>

              <div>
                <div class="flex items-center gap-2 mb-3">
                  <MessageSquare class="w-4 h-4 text-atlassian-neutral-70" />
                  <span class="text-sm font-medium text-atlassian-neutral-100">Activity</span>
                </div>
                <div class="flex items-start gap-3">
                  <img src="https://i.pravatar.cc/150?img=1" class="w-8 h-8 rounded-full" />
                  <div class="flex-1">
                    <div class="text-sm text-atlassian-neutral-100 mb-1">John Smith</div>
                    <div class="text-xs text-atlassian-neutral-70 mb-2">Just now</div>
                    <div class="text-sm text-atlassian-neutral-100">No comments yet</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="w-[240px] p-6 space-y-4">
              <div>
                <label class="block text-xs font-medium text-atlassian-neutral-70 mb-1">Status</label>
                <select 
                  v-model="editStatus"
                  class="w-full h-8 px-2 border border-atlassian-neutral-20 rounded text-sm text-atlassian-neutral-100 bg-atlassian-neutral-0"
                >
                  <option value="todo">To Do</option>
                  <option value="inprogress">In Progress</option>
                  <option value="done">Done</option>
                </select>
              </div>

              <div>
                <label class="block text-xs font-medium text-atlassian-neutral-70 mb-1">Assignee</label>
                <select 
                  v-model="editAssignee"
                  class="w-full h-8 px-2 border border-atlassian-neutral-20 rounded text-sm text-atlassian-neutral-100 bg-atlassian-neutral-0"
                >
                  <option :value="null">Unassigned</option>
                  <option v-for="user in issueStore.users" :key="user.id" :value="user">{{ user.name }}</option>
                </select>
              </div>

              <div>
                <label class="block text-xs font-medium text-atlassian-neutral-70 mb-1">Priority</label>
                <select 
                  v-model="editPriority"
                  class="w-full h-8 px-2 border border-atlassian-neutral-20 rounded text-sm text-atlassian-neutral-100 bg-atlassian-neutral-0"
                >
                  <option value="highest">Highest</option>
                  <option value="high">High</option>
                  <option value="medium">Medium</option>
                  <option value="low">Low</option>
                  <option value="lowest">Lowest</option>
                </select>
              </div>

              <div>
                <label class="block text-xs font-medium text-atlassian-neutral-70 mb-1">Story Points</label>
                <input 
                  v-model.number="editStoryPoints"
                  type="number"
                  class="w-full h-8 px-2 border border-atlassian-neutral-20 rounded text-sm text-atlassian-neutral-100"
                  placeholder="0"
                />
              </div>

              <div>
                <label class="block text-xs font-medium text-atlassian-neutral-70 mb-1">Reporter</label>
                <div class="flex items-center gap-2">
                  <img v-if="issue?.reporter" :src="issue.reporter.avatar" class="w-6 h-6 rounded-full" />
                  <span class="text-sm text-atlassian-neutral-100">{{ issue?.reporter?.name }}</span>
                </div>
              </div>

              <div>
                <label class="block text-xs font-medium text-atlassian-neutral-70 mb-1">Created</label>
                <span class="text-sm text-atlassian-neutral-80">{{ formatDate(issue?.created) }}</span>
              </div>

              <div>
                <label class="block text-xs font-medium text-atlassian-neutral-70 mb-1">Updated</label>
                <span class="text-sm text-atlassian-neutral-80">{{ formatDate(issue?.updated) }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { X, Maximize2, MessageSquare } from 'lucide-vue-next'
import dayjs from 'dayjs'
import { useUiStore } from '../../stores/ui'
import { useIssueStore } from '../../stores/issues'
import StatusBadge from '../common/StatusBadge.vue'

const uiStore = useUiStore()
const issueStore = useIssueStore()

const issue = computed(() => {
  if (!uiStore.selectedIssueId) return null
  return issueStore.getIssueById(uiStore.selectedIssueId)
})

const editSummary = ref('')
const editDescription = ref('')
const editStatus = ref<'todo' | 'inprogress' | 'done'>('todo')
const editAssignee = ref<any>(null)
const editPriority = ref<'highest' | 'high' | 'medium' | 'low' | 'lowest'>('medium')
const editStoryPoints = ref<number | null>(null)

watch(issue, (newIssue) => {
  if (newIssue) {
    editSummary.value = newIssue.summary
    editDescription.value = newIssue.description
    editStatus.value = newIssue.status
    editAssignee.value = newIssue.assignee
    editPriority.value = newIssue.priority
    editStoryPoints.value = newIssue.storyPoints
  }
}, { immediate: true })

watch([editSummary, editDescription, editStatus, editAssignee, editPriority, editStoryPoints], () => {
  if (issue.value) {
    issueStore.updateIssue(issue.value.id, {
      summary: editSummary.value,
      description: editDescription.value,
      status: editStatus.value,
      assignee: editAssignee.value,
      priority: editPriority.value,
      storyPoints: editStoryPoints.value
    })
  }
})

const formatDate = (date?: string) => {
  if (!date) return ''
  return dayjs(date).format('MMM d, YYYY')
}

const close = () => {
  uiStore.closeModal()
}
</script>