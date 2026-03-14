/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        atlassian: {
          blue: {
            50: '#deebff',
            100: '#bfe3ff',
            200: '#7ac3ff',
            300: '#2684ff',
            400: '#0052cc',
            500: '#0747a6',
          },
          neutral: {
            0: '#ffffff',
            10: '#f4f5f7',
            20: '#ebecf0',
            30: '#dfe1e6',
            40: '#c1c7d0',
            50: '#b3bac5',
            60: '#97a0af',
            70: '#7a869a',
            80: '#6b778c',
            90: '#5e6c84',
            100: '#42526e',
            200: '#344563',
            300: '#253858',
            400: '#172b4d',
          },
          red: { 400: '#ff5630' },
          yellow: { 400: '#ffab00' },
          green: { 400: '#36b37e' },
        }
      },
      fontFamily: {
        sans: ['-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
      },
      boxShadow: {
        'jira-card': '0 1px 3px rgba(9,30,66,0.15), 0 0 1px rgba(9,30,66,0.1)',
        'jira-modal': '0 10px 40px -10px rgba(9,30,66,0.3)',
      }
    }
  },
  plugins: [],
}