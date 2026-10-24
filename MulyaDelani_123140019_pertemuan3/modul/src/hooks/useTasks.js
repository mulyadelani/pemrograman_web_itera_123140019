import { useContext } from 'react'
import TaskContext from '../context/TaskContext.jsx'

export default function useTasks() {
  const context = useContext(TaskContext)
  if (!context) {
    throw new Error('useTasks harus digunakan di dalam TaskProvider.')
  }
  return context
}
