import PropTypes from 'prop-types'
import { NavLink } from 'react-router-dom'

function Navbar() {
  return (
    <nav className="navbar" aria-label="Navigasi utama">
      <div className="nav-container">
        <div className="logo">
          <NavLink to="/" end>
            <span className="logo-mark" aria-hidden="true">r.</span>
            <span>React <span className="logo-accent">Task Manager</span></span>
          </NavLink>
        </div>
        <ul className="nav-links">
          <li><NavLink to="/" end>Beranda</NavLink></li>
          <li><NavLink to="/about">Tentang</NavLink></li>
        </ul>
      </div>
    </nav>
  )
}

Navbar.propTypes = {}

export default Navbar
