import { useState } from 'react'
import PropTypes from 'prop-types'
import useBooks from '../hooks/useBooks.js'

function BookForm({ book, onClose }) {
  const { addBook, updateBook } = useBooks()
  const [title, setTitle] = useState(book?.title ?? '')
  const [author, setAuthor] = useState(book?.author ?? '')
  const [status, setStatus] = useState(book?.status ?? 'milik')
  const [errors, setErrors] = useState({})

  const handleSubmit = (event) => {
    event.preventDefault()
    const nextErrors = {}
    if (!title.trim()) nextErrors.title = 'Judul buku wajib diisi.'
    if (!author.trim()) nextErrors.author = 'Nama penulis wajib diisi.'
    setErrors(nextErrors)
    if (Object.keys(nextErrors).length > 0) return

    const nextBook = { ...(book ?? {}), title: title.trim(), author: author.trim(), status }
    if (book) updateBook(nextBook)
    else addBook(nextBook)
    onClose()
  }

  return (
    <div className="modal-backdrop" onMouseDown={(event) => event.target === event.currentTarget && onClose()}>
      <section className="book-modal" role="dialog" aria-modal="true" aria-labelledby="form-heading">
        <div className="modal-heading">
          <div>
            <span className="eyebrow muted-eyebrow">{book ? 'PERBARUI KOLEKSI' : 'TAMBAH KE RAK'}</span>
            <h2 id="form-heading">{book ? 'Edit buku' : 'Buku baru'}</h2>
          </div>
          <button type="button" className="modal-close" aria-label="Tutup formulir" onClick={onClose}>×</button>
        </div>
        <form className="book-form" onSubmit={handleSubmit} noValidate>
          <label htmlFor="book-title">Judul buku</label>
          <input
            id="book-title"
            value={title}
            onChange={(event) => setTitle(event.target.value)}
            placeholder="Contoh: Filosofi Teras"
            maxLength={100}
            aria-invalid={Boolean(errors.title)}
            aria-describedby={errors.title ? 'title-error' : undefined}
            autoFocus
          />
          {errors.title && <span className="field-error" id="title-error">{errors.title}</span>}

          <label htmlFor="book-author">Nama penulis</label>
          <input
            id="book-author"
            value={author}
            onChange={(event) => setAuthor(event.target.value)}
            placeholder="Contoh: Henry Manampiring"
            maxLength={80}
            aria-invalid={Boolean(errors.author)}
            aria-describedby={errors.author ? 'author-error' : undefined}
          />
          {errors.author && <span className="field-error" id="author-error">{errors.author}</span>}

          <label htmlFor="book-status">Status buku</label>
          <select id="book-status" value={status} onChange={(event) => setStatus(event.target.value)}>
            <option value="milik">Sudah dimiliki</option>
            <option value="baca">Sedang dibaca</option>
            <option value="beli">Ingin dibeli</option>
          </select>
          <div className="form-actions">
            <button type="button" className="button button-light" onClick={onClose}>Batal</button>
            <button type="submit" className="button button-dark">{book ? 'Simpan perubahan' : 'Tambah buku'}</button>
          </div>
        </form>
      </section>
    </div>
  )
}

BookForm.propTypes = {
  book: PropTypes.shape({
    id: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,
    author: PropTypes.string.isRequired,
    status: PropTypes.oneOf(['milik', 'baca', 'beli']).isRequired,
  }),
  onClose: PropTypes.func.isRequired,
}

BookForm.defaultProps = {
  book: null,
}

export default BookForm
