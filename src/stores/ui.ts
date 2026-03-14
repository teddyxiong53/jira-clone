import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useUiStore = defineStore('ui', () => {
  const isSideNavCollapsed = ref(false)
  const isModalOpen = ref(false)
  const selectedIssueId = ref<string | null>(null)
  const searchQuery = ref('')

  const toggleSideNav = () => {
    isSideNavCollapsed.value = !isSideNavCollapsed.value
  }

  const openModal = (issueId: string) => {
    selectedIssueId.value = issueId
    isModalOpen.value = true
  }

  const closeModal = () => {
    isModalOpen.value = false
    selectedIssueId.value = null
  }

  const setSearchQuery = (query: string) => {
    searchQuery.value = query
  }

  return {
    isSideNavCollapsed,
    isModalOpen,
    selectedIssueId,
    searchQuery,
    toggleSideNav,
    openModal,
    closeModal,
    setSearchQuery
  }
})