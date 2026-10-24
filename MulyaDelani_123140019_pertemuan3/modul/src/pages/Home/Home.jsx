import { useState } from 'react'
import Header from '../../components/Header/Header.jsx'
import TaskForm from '../../components/TaskForm/TaskForm.jsx'
import TaskItem from '../../components/TaskItem/TaskItem.jsx'
import Card from '../../components/Card/Card.jsx'
import useTasks from '../../hooks/useTasks.js'
import useWindowSize from '../../hooks/useWindowSize.js'

function Home() {
  const { tasks, addTask, deleteTask, toggleComplete, clearTasks, stats } = useTasks()
  const { width } = useWindowSize()
  const [count, setCount] = useState(0)
  const [items, setItems] = useState([])

  const handleClearTasks = () => {
    if (tasks.length && window.confirm('Hapus semua tugas? Tindakan ini tidak dapat dibatalkan.')) {
      clearTasks()
    }
  }

  const addLabItem = () => {
    setItems((current) => [
      ...current,
      { id: `${Date.now()}-${current.length}`, name: `Tugas Baru ke-${current.length + 1}` },
    ])
  }

  return (
    <div className="home page-container">
      <Header title="React Task Manager" description="Kelola tugas harian Anda secara terstruktur." />
      <main className="container">
        <div className="mode-row">
          <span className="mode-badge">{width < 768 ? 'Mode Layar Mobile' : 'Mode Layar Desktop'}</span>
        </div>

        <section className="stats" aria-label="Statistik tugas">
          <article className="stat-card"><span>Total tugas</span><strong>{stats.total}</strong></article>
          <article className="stat-card"><span>Selesai</span><strong className="stat-completed">{stats.completed}</strong></article>
          <article className="stat-card"><span>Belum selesai</span><strong>{stats.remaining}</strong></article>
        </section>
        <div className="stats-actions">
          <p>Progress penyelesaian: <strong>{stats.completionRate.toFixed(0)}%</strong></p>
          <button type="button" className="clear-button" onClick={handleClearTasks} disabled={!tasks.length}>
            Hapus semua tugas
          </button>
        </div>

        <Card title="Tambah tugas">
          <TaskForm onAddTask={addTask} />
        </Card>

        <section aria-labelledby="task-list-title">
          <div className="task-list-heading">
            <h2 id="task-list-title">Tugas saya</h2>
            <span>{stats.total} tugas</span>
          </div>
          {tasks.length === 0 ? (
            <p className="empty-message">Belum ada tugas. Tambahkan tugas baru di atas!</p>
          ) : (
            <div className="task-list">
              {tasks.map((task) => (
                <TaskItem
                  key={task.id}
                  task={task}
                  onDelete={deleteTask}
                  onToggleComplete={toggleComplete}
                />
              ))}
            </div>
          )}
        </section>

        <details className="lab-section">
          <summary>Latihan interaktif: useState dan immutable array</summary>
          <div className="lab-grid">
            <section className="lab-card" aria-label="Latihan counter">
              <h3>Counter sederhana</h3>
              <p className="counter-value" aria-live="polite">{count}</p>
              <div className="lab-buttons">
                <button type="button" onClick={() => setCount((value) => value + 1)}>Tambah (+1)</button>
                <button type="button" onClick={() => setCount((value) => value - 1)}>Kurang (-1)</button>
                <button type="button" className="reset-button" onClick={() => setCount(0)}>Reset</button>
              </div>
            </section>
            <section className="lab-card" aria-label="Latihan array state">
              <h3>Array state (immutable)</h3>
              <div className="lab-buttons">
                <button type="button" onClick={addLabItem}>Tambah item</button>
                <button type="button" className="reset-button" onClick={() => setItems([])} disabled={!items.length}>Kosongkan</button>
              </div>
              <ul className="lab-items">
                {items.map((item) => (
                  <li key={item.id}>
                    <span>{item.name}</span>
                    <button type="button" onClick={() => setItems((current) => current.filter((entry) => entry.id !== item.id))}>
                      Hapus
                    </button>
                  </li>
                ))}
              </ul>
              {!items.length && <p className="task-form-error">Array kosong — coba tambah item.</p>}
            </section>
          </div>
        </details>
      </main>
    </div>
  )
}

Home.propTypes = {}

export default Home
