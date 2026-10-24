import PropTypes from 'prop-types'

function TaskItem({ task, onDelete, onToggleComplete }) {
  return (
    <div className={`task-item${task.completed ? ' completed' : ''}`}>
      <label className="task-content">
        <input
          type="checkbox"
          checked={task.completed}
          onChange={() => onToggleComplete(task.id)}
          aria-label={`Tandai ${task.title} sebagai ${task.completed ? 'belum selesai' : 'selesai'}`}
        />
        <span className="task-title">{task.title}</span>
      </label>
      <button type="button" className="delete-btn" onClick={() => onDelete(task.id)}>
        Hapus
      </button>
    </div>
  )
}

TaskItem.propTypes = {
  task: PropTypes.shape({
    id: PropTypes.oneOfType([PropTypes.number, PropTypes.string]).isRequired,
    title: PropTypes.string.isRequired,
    completed: PropTypes.bool.isRequired,
  }).isRequired,
  onDelete: PropTypes.func.isRequired,
  onToggleComplete: PropTypes.func.isRequired,
}

export default TaskItem
