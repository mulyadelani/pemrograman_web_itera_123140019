import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    environment: 'jsdom',
    include: ['src/test/**/*.test.{js,jsx}'],
    setupFiles: ['./src/test/setup.js'],
    clearMocks: true,
    pool: 'threads',
    maxWorkers: 1,
    minWorkers: 1,
  },
})
