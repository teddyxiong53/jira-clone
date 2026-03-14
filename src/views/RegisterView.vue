<template>
  <div class="min-h-screen flex items-center justify-center bg-atlassian-neutral-10">
    <div class="bg-atlassian-neutral-0 rounded-lg shadow-jira-modal p-8 w-[400px]">
      <div class="text-center mb-6">
        <div class="w-12 h-12 bg-atlassian-blue-400 rounded-lg flex items-center justify-center mx-auto mb-4">
          <svg class="w-8 h-8 text-white" viewBox="0 0 32 32" fill="none">
            <rect width="32" height="32" rx="4" fill="#0052CC"/>
            <path d="M8 10h6v12H8V10z" fill="white"/>
            <path d="M16 10h6v12h-6V10z" fill="white" opacity="0.7"/>
          </svg>
        </div>
        <h1 class="text-xl font-semibold text-atlassian-neutral-100">Create an account</h1>
      </div>

      <form @submit.prevent="handleRegister">
        <div class="mb-4">
          <label class="block text-sm font-medium text-atlassian-neutral-100 mb-1">Name</label>
          <input 
            v-model="name"
            type="text" 
            required
            class="w-full h-9 px-3 border border-atlassian-neutral-30 rounded text-sm text-atlassian-neutral-100 focus:outline-none focus:border-atlassian-blue-400"
            placeholder="Your name"
          />
        </div>

        <div class="mb-4">
          <label class="block text-sm font-medium text-atlassian-neutral-100 mb-1">Email</label>
          <input 
            v-model="email"
            type="email" 
            required
            class="w-full h-9 px-3 border border-atlassian-neutral-30 rounded text-sm text-atlassian-neutral-100 focus:outline-none focus:border-atlassian-blue-400"
            placeholder="your@email.com"
          />
        </div>

        <div class="mb-4">
          <label class="block text-sm font-medium text-atlassian-neutral-100 mb-1">Password</label>
          <input 
            v-model="password"
            type="password" 
            required
            class="w-full h-9 px-3 border border-atlassian-neutral-30 rounded text-sm text-atlassian-neutral-100 focus:outline-none focus:border-atlassian-blue-400"
            placeholder="Password (any)"
          />
        </div>

        <div v-if="error" class="mb-4 p-2 bg-red-50 border border-red-200 rounded text-sm text-red-600">
          {{ error }}
        </div>

        <button 
          type="submit" 
          :disabled="loading"
          class="w-full h-9 bg-atlassian-blue-400 text-white font-medium rounded hover:bg-atlassian-blue-500 transition-colors disabled:opacity-50"
        >
          {{ loading ? 'Creating account...' : 'Sign up' }}
        </button>
      </form>

      <div class="mt-4 text-center text-sm text-atlassian-neutral-70">
        Already have an account? 
        <router-link to="/login" class="text-atlassian-blue-400 hover:underline">Sign in</router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const name = ref('')
const email = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

const handleRegister = async () => {
  error.value = ''
  loading.value = true
  try {
    await authStore.register(name.value, email.value, password.value)
    router.push('/')
  } catch (e: any) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>