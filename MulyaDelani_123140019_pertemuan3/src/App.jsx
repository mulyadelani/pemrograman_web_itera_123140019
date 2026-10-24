import { Link, NavLink, Route, Routes } from 'react-router-dom'
import { BookProvider } from './context/BookContext.jsx'
import useBooks from './hooks/useBooks.js'
import Home from './pages/Home.jsx'
import Stats from './pages/Stats.jsx'
import './App.css'

function Header() {
  return (
    <header className="topbar">
      <Link className="wordmark" to="/" aria-label="RakBuku, beranda">
        <span className="brand-icon" aria-hidden="true">r.</span>
        <span>rak<span className="wordmark-accent">buku</span></span>
      </Link>
      <nav className="main-nav" aria-label="Navigasi utama">
        <NavLink to="/" end>Perpustakaan</NavLink>
        <NavLink to="/statistik">Statistik</NavLink>
      </nav>
      <div className="profile">
        <span className="profile-avatar" aria-hidden="true">M</span>
        <span className="profile-name">Perpustakaanku</span>
      </div>
    </header>
  )
}

function AppLayout() {
  const { storageError } = useBooks()

  return (
    <div className="app-shell">
      <Header />
      {storageError && <div className="storage-alert" role="alert">{storageError}</div>}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/statistik" element={<Stats />} />
        <Route path="*" element={<Home />} />
      </Routes>
      <footer className="site-footer">
        <span>RakBuku <span aria-hidden="true">·</span> ruang kecil untuk cerita-cerita besar.</span>
        <span>Dirancang untuk perjalanan membacamu.</span>
      </footer>
    </div>
  )
}

function App() {
  return (
    <BookProvider>
      <AppLayout />
    </BookProvider>
  )
}

Header.propTypes = {}
AppLayout.propTypes = {}
App.propTypes = {}

export default App
