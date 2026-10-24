import { useMemo } from 'react'

export default function useBookStats(books) {
  return useMemo(() => {
    const counts = books.reduce((result, book) => {
      result[book.status] += 1
      return result
    }, { milik: 0, baca: 0, beli: 0 })

    return { ...counts, total: books.length }
  }, [books])
}
