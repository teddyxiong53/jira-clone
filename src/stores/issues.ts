import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { mockIssues, mockUsers } from '../mock/data'

export interface User {
  id: string
  name: string
  avatar: string
  email: string
}

export interface Issue {
  id: string
  key: string
  summary: string
  description: string
  status: 'todo' | 'inprogress' | 'done'
  priority: 'highest' | 'high' | 'medium' | 'low' | 'lowest'
  assignee: User | null
  reporter: User
  labels: string[]
  storyPoints: number | null
  created: string
  updated: string
}

export const useIssueStore = defineStore('issues', () => {
  const issues = ref<Issue[]>(mockIssues)
  const users = ref<User[]>(mockUsers)
  const columns = ref<string[]>(['todo', 'inprogress', 'done'])

  const getIssuesByStatus = (status: string) => {
    return computed(() => issues.value.filter(issue => issue.status === status))
  }

  const getIssueById = (id: string) => {
    return issues.value.find(issue => issue.id === id)
  }

  const moveIssue = (issueId: string, newStatus: string) => {
    const issue = issues.value.find(i => i.id === issueId)
    if (issue) {
      issue.status = newStatus as Issue['status']
      issue.updated = new Date().toISOString()
    }
  }

  const updateIssue = (issueId: string, updates: Partial<Issue>) => {
    const index = issues.value.findIndex(i => i.id === issueId)
    if (index !== -1) {
      issues.value[index] = { ...issues.value[index], ...updates, updated: new Date().toISOString() }
    }
  }

  const addIssue = (issue: Omit<Issue, 'id' | 'key' | 'created' | 'updated'>) => {
    const id = String(issues.value.length + 1)
    const key = `PROJ-${String(issues.value.length + 1).padStart(4, '0')}`
    issues.value.push({
      ...issue,
      id,
      key,
      created: new Date().toISOString(),
      updated: new Date().toISOString()
    })
  }

  return {
    issues,
    users,
    columns,
    getIssuesByStatus,
    getIssueById,
    moveIssue,
    updateIssue,
    addIssue
  }
})