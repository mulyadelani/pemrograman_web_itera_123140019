import { useEffect, useState } from 'react'

export default function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key)
      return item === null ? initialValue : JSON.parse(item)
    } catch (error) {
      console.error(`Gagal membaca localStorage dengan key "${key}".`, error)
      return initialValue
    }
  })
  const [storageError, setStorageError] = useState('')

  useEffect(() => {
    try {
      window.localStorage.setItem(key, JSON.stringify(storedValue))
      // eslint-disable-next-line react/set-state-in-effect -- Report storage sync failures to the user.
      setStorageError('')
    } catch (error) {
      console.error(`Gagal menyimpan localStorage dengan key "${key}".`, error)
      // eslint-disable-next-line react/set-state-in-effect -- Report storage sync failures to the user.
      setStorageError('Penyimpanan browser gagal. Perubahan belum tersimpan di perangkat ini.')
    }
  }, [key, storedValue])

  return [storedValue, setStoredValue, storageError]
}
