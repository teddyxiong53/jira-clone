import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

const API_BASE = 'http://localhost:5000/api'

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
  const issues = ref<Issue[]>([])
  const users = ref<User[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)
  const columns = ref<string[]>(['todo', 'inprogress', 'done'])

  const fetchIssues = async () => {
    loading.value = true
    error.value = null
    try {
      const res = await fetch(`${API_BASE}/issues`)
      if (!res.ok) throw new Error('Failed to fetch issues')
      issues.value = await res.json()
    } catch (e: any) {
      error.value = e.message
      console.error('Failed to fetch issues:', e)
    } finally {
      loading.value = false
    }
  }

  const fetchUsers = async () => {
    try {
      const res = await fetch(`${API_BASE}/users`)
      if (!res.ok) throw new Error('Failed to fetch users')
      users.value = await res.json()
    } catch (e) {
      console.error('Failed to fetch users:', e)
    }
  }

  const getIssuesByStatus = (status: string) => {
    return computed(() => issues.value.filter(issue => issue.status === status))
  }

  const getIssueById = (id: string) => {
    return issues.value.find(issue => issue.id === id)
  }

  const moveIssue = async (issueId: string, newStatus: string) => {
    const issue = issues.value.find(i => i.id === issueId)
    if (issue) {
      issue.status = newStatus as Issue['status']
      issue.updated = new Date().toISOString()
    }
    try {
      await fetch(`${API_BASE}/issues/${issueId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: newStatus })
      })
    } catch (e) {
      console.error('Failed to update issue status:', e)
    }
  }

  const updateIssue = async (issueId: string, updates: Partial<Issue>) => {
    const index = issues.value.findIndex(i => i.id === issueId)
    if (index !== -1) {
      issues.value[index] = { ...issues.value[index], ...updates, updated: new Date().toISOString() }
    }
    try {
      const body: any = {}
      if (updates.summary !== undefined) body.summary = updates.summary
      if (updates.description !== undefined) body.description = updates.description
      if (updates.status !== undefined) body.status = updates.status
      if (updates.priority !== undefined) body.priority = updates.priority
      if (updates.assignee !== undefined) body.assignee_id = updates.assignee?.id
      if (updates.labels !== undefined) body.labels = updates.labels
      if (updates.storyPoints !== undefined) body.storyPoints = updates.storyPoints
      
      await fetch(`${API_BASE}/issues/${issueId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      })
    } catch (e) {
      console.error('Failed to update issue:', e)
    }
  }

  const addIssue = async (issue: Omit<Issue, 'id' | 'key' | 'created' | 'updated'>) => {
    try {
      const res = await fetch(`${API_BASE}/issues`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          summary: issue.summary,
          description: issue.description,
          status: issue.status,
          priority: issue.priority,
          assignee_id: issue.assignee?.id,
          reporter_id: issue.reporter.id,
          labels: issue.labels,
          storyPoints: issue.storyPoints
        })
      })
      const newIssue = await res.json()
      issues.value.push(newIssue)
      return newIssue
    } catch (e) {
      console.error('Failed to create issue:', e)
      return null
    }
  }

  return {
    issues,
    users,
    loading,
    error,
    columns,
    fetchIssues,
    fetchUsers,
    getIssuesByStatus,
    getIssueById,
    moveIssue,
    updateIssue,
    addIssue
  }
})