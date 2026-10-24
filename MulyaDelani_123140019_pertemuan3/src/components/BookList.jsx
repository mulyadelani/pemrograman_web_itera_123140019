import PropTypes from 'prop-types'
import useBooks from '../hooks/useBooks.js'

const statusLabels = {
  milik: 'Sudah dimiliki',
  baca: 'Sedang dibaca',
  beli: 'Ingin dibeli',
}

const coverStyles = ['cover-rose', 'cover-sage', 'cover-blue', 'cover-yellow']

function BookCard({ book, index, onEdit }) {
  const { deleteBook } = useBooks()
  const coverStyle = coverStyles[index % coverStyles.length]

  return (
    <article className="book-card">
      <div className={`book-card-cover ${coverStyle}`} aria-hidden="true">
        <span className="cover-label">{book.title.split(/\s+/).slice(0, 3).join(' ')}</span>
        <span className="cover-author">{book.author}</span>
        <span className="cover-mark">✳</span>
      </div>
      <div className="book-card-body">
        <div className="book-card-title-row">
          <h3 title={book.title}>{book.title}</h3>
          <div className="card-menu">
            <button type="button" className="icon-button" aria-label={`Opsi ${book.title}`} aria-haspopup="true">
              ···
            </button>
            <div className="card-menu-items">
              <button type="button" onClick={() => onEdit(book)}>Edit buku</button>
              <button
                type="button"
                className="delete-action"
                onClick={() => {
                  if (window.confirm(`Hapus "${book.title}" dari koleksi?`)) deleteBook(book.id)
                }}
              >
                Hapus buku
              </button>
            </div>
          </div>
        </div>
        <p className="book-author">{book.author}</p>
        <span className={`status-badge status-${book.status}`}><i />{statusLabels[book.status]}</span>
      </div>
    </article>
  )
}

function BookList({ books, query, onEdit }) {
  if (books.length === 0) {
    return (
      <div className="empty-state">
        <span className="empty-icon" aria-hidden="true">▤</span>
        <h3>{query ? 'Buku tidak ditemukan' : 'Rakmu masih kosong'}</h3>
        <p>{query ? 'Coba gunakan kata kunci lain.' : 'Tambahkan buku pertamamu untuk mulai merapikan koleksi.'}</p>
      </div>
    )
  }

  return (
    <div className="book-grid">
      {books.map((book, index) => (
        <BookCard key={book.id} book={book} index={index} onEdit={onEdit} />
      ))}
    </div>
  )
}

const bookPropType = PropTypes.shape({
  id: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  author: PropTypes.string.isRequired,
  status: PropTypes.oneOf(['milik', 'baca', 'beli']).isRequired,
}).isRequired

BookCard.propTypes = {
  book: bookPropType,
  index: PropTypes.number.isRequired,
  onEdit: PropTypes.func.isRequired,
}

BookList.propTypes = {
  books: PropTypes.arrayOf(bookPropType).isRequired,
  query: PropTypes.string.isRequired,
  onEdit: PropTypes.func.isRequired,
}

export default BookList
