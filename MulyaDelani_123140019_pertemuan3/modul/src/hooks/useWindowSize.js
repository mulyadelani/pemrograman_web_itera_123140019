import { useEffect, useState } from 'react'

function readWidth() {
  return typeof window === 'undefined' ? 1200 : window.innerWidth
}

export default function useWindowSize() {
  const [width, setWidth] = useState(readWidth)

  useEffect(() => {
    const handleResize = () => setWidth(window.innerWidth)
    window.addEventListener('resize', handleResize)
    return () => window.removeEventListener('resize', handleResize)
  }, [])

  return { width }
}
