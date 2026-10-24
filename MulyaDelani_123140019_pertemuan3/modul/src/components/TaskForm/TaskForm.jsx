import { useState } from 'react'
import PropTypes from 'prop-types'

function TaskForm({ onAddTask }) {
  const [title, setTitle] = useState('')
  const [error, setError] = useState('')

  const handleSubmit = (event) => {
    event.preventDefault()
    const normalizedTitle = title.trim()
    if (!normalizedTitle) {
      setError('Judul tugas wajib diisi.')
      return
    }

    onAddTask({
      id: Date.now(),
      title: normalizedTitle,
      completed: false,
    })
    setTitle('')
    setError('')
  }

  return (
    <form className="task-form" onSubmit={handleSubmit} noValidate>
      <input
        type="text"
        placeholder="Ketik tugas baru lalu tekan Enter..."
        value={title}
        onChange={(event) => {
          setTitle(event.target.value)
          if (error) setError('')
        }}
        aria-label="Judul tugas baru"
        aria-invalid={Boolean(error)}
        aria-describedby={error ? 'task-form-error' : undefined}
        maxLength={120}
      />
      <button type="submit">Tambah</button>
      {error && <span className="task-form-error" id="task-form-error" role="alert">{error}</span>}
    </form>
  )
}

TaskForm.propTypes = {
  onAddTask: PropTypes.func.isRequired,
}

export default TaskForm
