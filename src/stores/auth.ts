import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { User } from './issues'

const API_BASE = 'http://localhost:5000/api'

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null)
  const token = ref<string | null>(localStorage.getItem('token'))
  const loading = ref(false)

  const register = async (name: string, email: string, password: string) => {
    loading.value = true
    try {
      const res = await fetch(`${API_BASE}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password })
      })
      if (!res.ok) {
        const data = await res.json()
        throw new Error(data.error || 'Registration failed')
      }
      const newUser = await res.json()
      user.value = newUser
      token.value = newUser.id
      localStorage.setItem('token', newUser.id)
      return true
    } catch (e: any) {
      console.error('Registration failed:', e)
      throw e
    } finally {
      loading.value = false
    }
  }

  const login = async (email: string) => {
    loading.value = true
    try {
      const res = await fetch(`${API_BASE}/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email })
      })
      if (!res.ok) {
        const data = await res.json()
        throw new Error(data.error || 'Login failed')
      }
      const newUser = await res.json()
      user.value = newUser
      token.value = newUser.id
      localStorage.setItem('token', newUser.id)
      return true
    } catch (e: any) {
      console.error('Login failed:', e)
      throw e
    } finally {
      loading.value = false
    }
  }

  const logout = () => {
    user.value = null
    token.value = null
    localStorage.removeItem('token')
  }

  const initAuth = async () => {
    const savedToken = localStorage.getItem('token')
    if (savedToken) {
      try {
        const res = await fetch(`${API_BASE}/auth/me`, {
          headers: { 'X-User-Id': savedToken }
        })
        if (res.ok) {
          user.value = await res.json()
          token.value = savedToken
        } else {
          logout()
        }
      } catch {
        logout()
      }
    }
  }

  const isAuthenticated = () => !!user.value

  return {
    user,
    token,
    loading,
    register,
    login,
    logout,
    initAuth,
    isAuthenticated
  }
})