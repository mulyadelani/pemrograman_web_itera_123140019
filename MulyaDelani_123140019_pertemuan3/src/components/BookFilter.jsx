import PropTypes from 'prop-types'

const filters = [
  { value: 'semua', label: 'Semua buku' },
  { value: 'milik', label: 'Sudah dimiliki' },
  { value: 'baca', label: 'Sedang dibaca' },
  { value: 'beli', label: 'Wishlist' },
]

function BookFilter({ activeStatus, onChange }) {
  return (
    <div className="filter-row" role="group" aria-label="Filter buku berdasarkan status">
      {filters.map((filter) => (
        <button
          type="button"
          key={filter.value}
          className={`filter-chip${activeStatus === filter.value ? ' is-active' : ''}`}
          aria-pressed={activeStatus === filter.value}
          onClick={() => onChange(filter.value)}
        >
          {filter.label}
        </button>
      ))}
    </div>
  )
}

BookFilter.propTypes = {
  activeStatus: PropTypes.oneOf(['semua', 'milik', 'baca', 'beli']).isRequired,
  onChange: PropTypes.func.isRequired,
}

export default BookFilter
