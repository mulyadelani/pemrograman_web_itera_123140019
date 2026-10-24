import { createContext, useMemo } from 'react'
import PropTypes from 'prop-types'
import useLocalStorage from '../hooks/useLocalStorage.js'

const TaskContext = createContext(null)
export default TaskContext

export function TaskProvider({ children }) {
  const [tasks, setTasks, storageError] = useLocalStorage('tasks_data', [])

  // Functional updates avoid stale state if several task actions happen quickly.
  const value = useMemo(() => {
    const completed = tasks.filter((task) => task.completed).length
    return {
      tasks,
      storageError,
      addTask: (newTask) => setTasks((current) => [...current, newTask]),
      deleteTask: (taskId) => setTasks((current) => current.filter((task) => task.id !== taskId)),
      toggleComplete: (taskId) => setTasks((current) => current.map((task) => (
        task.id === taskId ? { ...task, completed: !task.completed } : task
      ))),
      clearTasks: () => setTasks([]),
      stats: {
        total: tasks.length,
        completed,
        remaining: tasks.length - completed,
        completionRate: tasks.length ? (completed / tasks.length) * 100 : 0,
      },
    }
  }, [tasks, setTasks, storageError])

  return (
    <TaskContext.Provider value={value}>
      {storageError && <div className="storage-alert" role="alert">{storageError}</div>}
      {children}
    </TaskContext.Provider>
  )
}

TaskProvider.propTypes = {
  children: PropTypes.node.isRequired,
}
