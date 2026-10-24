import { Link } from 'react-router-dom'

function NotFound() {
  return (
    <main className="page-container">
      <section className="not-found-card">
        <div className="not-found-code">404</div>
        <h1>Halaman tidak ditemukan</h1>
        <p>Alamat yang kamu buka tidak tersedia. Kembali ke beranda untuk melanjutkan.</p>
        <Link className="primary-button" to="/">Kembali ke beranda</Link>
      </section>
    </main>
  )
}

NotFound.propTypes = {}

export default NotFound
