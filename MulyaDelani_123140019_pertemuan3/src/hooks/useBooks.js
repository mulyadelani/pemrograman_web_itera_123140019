import { useContext } from 'react'
import BookContext from '../context/BookContext.jsx'

export default function useBooks() {
  const context = useContext(BookContext)
  if (!context) {
    throw new Error('useBooks harus digunakan di dalam BookProvider.')
  }
  return context
}
