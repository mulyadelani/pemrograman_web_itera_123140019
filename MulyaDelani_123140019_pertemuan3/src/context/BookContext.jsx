import { createContext, useMemo } from 'react'
import PropTypes from 'prop-types'
import useLocalStorage from '../hooks/useLocalStorage.js'

const BookContext = createContext(null)
export default BookContext

function createBookId() {
  return globalThis.crypto?.randomUUID?.() ?? `${Date.now()}-${Math.random().toString(36).slice(2)}`
}

export function BookProvider({ children }) {
  const [books, setBooks, storageError] = useLocalStorage('rakbuku-books', [])

  // Keep all collection mutations in one shared place for both pages.
  const value = useMemo(() => ({
    books,
    storageError,
    addBook(book) {
      setBooks((currentBooks) => [{ ...book, id: createBookId(), createdAt: new Date().toISOString() }, ...currentBooks])
    },
    updateBook(updatedBook) {
      setBooks((currentBooks) => currentBooks.map((book) => (
        book.id === updatedBook.id ? { ...book, ...updatedBook } : book
      )))
    },
    deleteBook(id) {
      setBooks((currentBooks) => currentBooks.filter((book) => book.id !== id))
    },
  }), [books, setBooks, storageError])

  return <BookContext.Provider value={value}>{children}</BookContext.Provider>
}

BookProvider.propTypes = {
  children: PropTypes.node.isRequired,
}
