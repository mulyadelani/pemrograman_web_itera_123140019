import PropTypes from 'prop-types'

function Header({ title, description }) {
  return (
    <header className="header">
      <p className="header-kicker">PRAKTIKUM PEMROGRAMAN WEB · REACT</p>
      <h1>{title}</h1>
      {description && <p>{description}</p>}
    </header>
  )
}

Header.propTypes = {
  title: PropTypes.string.isRequired,
  description: PropTypes.string,
}

Header.defaultProps = {
  description: '',
}

export default Header
