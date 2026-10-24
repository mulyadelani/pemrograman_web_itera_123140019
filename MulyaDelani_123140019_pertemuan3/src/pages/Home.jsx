import { useState } from 'react'
import BookForm from '../components/BookForm.jsx'
import BookFilter from '../components/BookFilter.jsx'
import BookList from '../components/BookList.jsx'
import useBooks from '../hooks/useBooks.js'

function Home() {
  const [query, setQuery] = useState('')
  const [status, setStatus] = useState('semua')
  const [editingBook, setEditingBook] = useState(null)
  const [formOpen, setFormOpen] = useState(false)
  const { books } = useBooks()
  const search = query.trim().toLocaleLowerCase('id')
  const filteredBooks = books.filter((book) => (
    (status === 'semua' || book.status === status)
    && (!search || `${book.title} ${book.author}`.toLocaleLowerCase('id').includes(search))
  ))

  const openCreateForm = () => {
    setEditingBook(null)
    setFormOpen(true)
  }

  const openEditForm = (book) => {
    setEditingBook(book)
    setFormOpen(true)
  }

  const closeForm = () => {
    setFormOpen(false)
    setEditingBook(null)
  }

  return (
    <main className="page-content" id="main-content">
      <section className="welcome-panel">
        <div className="welcome-copy">
          <span className="eyebrow"><span className="eyebrow-dot" /> KOLEKSI PRIBADI</span>
          <h1 aria-label="Setiap buku punya tempatnya sendiri">Setiap buku punya<br />tempatnya sendiri.</h1>
          <p>Catat yang sudah kamu punya, sedang kamu baca, atau ingin kamu temukan berikutnya.</p>
          <button type="button" className="button button-dark welcome-button" onClick={openCreateForm}>
            <span aria-hidden="true">＋</span> Tambah buku
          </button>
        </div>
        <div className="book-illustration" aria-hidden="true">
          <div className="sun-shape" />
          <div className="plant plant-one"><i /><i /><i /><b /></div>
          <div className="book-stack">
            <div className="book-cover book-cover-green"><span>THE<br />QUIET<br />GARDEN</span><i /></div>
            <div className="book-cover book-cover-coral"><span>Stories<br />to keep</span><i /></div>
            <div className="book-cover book-cover-cream"><span>NOTES ON<br />SLOW LIVING</span><i /></div>
          </div>
          <div className="sparkle sparkle-one">✳</div>
          <div className="sparkle sparkle-two">✳</div>
          <div className="illustration-caption">satu halaman<br />dalam satu waktu</div>
        </div>
      </section>

      <section className="library-section" aria-labelledby="library-heading">
        <div className="section-heading">
          <div>
            <span className="eyebrow muted-eyebrow">KATALOGMU</span>
            <h2 id="library-heading">Rak buku <span className="book-count">{books.length}</span></h2>
          </div>
          <label className="search-box">
            <span className="search-icon" aria-hidden="true">⌕</span>
            <span className="visually-hidden">Cari judul atau penulis</span>
            <input
              type="search"
              placeholder="Cari judul atau penulis..."
              value={query}
              onChange={(event) => setQuery(event.target.value)}
            />
            <kbd>⌘ K</kbd>
          </label>
        </div>
        <BookFilter activeStatus={status} onChange={setStatus} />
        <BookList books={filteredBooks} query={query} onEdit={openEditForm} />
      </section>
      {formOpen && <BookForm book={editingBook} onClose={closeForm} />}
    </main>
  )
}

Home.propTypes = {}

export default Home
