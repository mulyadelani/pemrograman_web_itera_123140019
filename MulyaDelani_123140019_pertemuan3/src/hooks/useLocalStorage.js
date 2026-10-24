import { useEffect, useState } from 'react'

export default function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    try {
      const storedValue = window.localStorage.getItem(key)
      return storedValue === null ? initialValue : JSON.parse(storedValue)
    } catch (error) {
      console.error(`Gagal membaca penyimpanan lokal untuk "${key}".`, error)
      return initialValue
    }
  })
  const [storageError, setStorageError] = useState('')

  // Persist updates after rendering so React remains the source of truth.
  useEffect(() => {
    try {
      window.localStorage.setItem(key, JSON.stringify(value))
      // eslint-disable-next-line react/set-state-in-effect -- Reflect successful storage sync in the UI.
      setStorageError('')
    } catch (error) {
      console.error(`Gagal menyimpan data ke penyimpanan lokal untuk "${key}".`, error)
      // eslint-disable-next-line react/set-state-in-effect -- Surface persistence failures to the user.
      setStorageError('Perubahan belum tersimpan di perangkat ini. Periksa ruang penyimpanan browser.')
    }
  }, [key, value])

  return [value, setValue, storageError]
}
