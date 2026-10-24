import PropTypes from 'prop-types'

function Card({ title, children }) {
  return (
    <section className="card">
      {title && <h2 className="card-heading">{title}</h2>}
      {children}
    </section>
  )
}

Card.propTypes = {
  title: PropTypes.string,
  children: PropTypes.node.isRequired,
}

Card.defaultProps = {
  title: '',
}

export default Card
