import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.js'],
    clearMocks: true,
    pool: 'threads',
    maxWorkers: 1,
    minWorkers: 1,
  },
})
