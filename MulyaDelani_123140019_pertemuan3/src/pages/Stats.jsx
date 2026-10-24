import { Link } from 'react-router-dom'
import useBooks from '../hooks/useBooks.js'
import useBookStats from '../hooks/useBookStats.js'

const statDetails = [
  { key: 'milik', label: 'Sudah dimiliki', note: 'Buku yang siap dibaca kapan saja', icon: '▤' },
  { key: 'baca', label: 'Sedang dibaca', note: 'Cerita yang sedang menemanimu', icon: '◷' },
  { key: 'beli', label: 'Ingin dibeli', note: 'Buku yang menunggu waktunya', icon: '♡' },
]

function Stats() {
  const { books } = useBooks()
  const stats = useBookStats(books)
  const mostCommon = statDetails.reduce((best, item) => (
    stats[item.key] > stats[best.key] ? item : best
  ), statDetails[0])

  return (
    <main className="page-content stats-page" id="main-content">
      <section className="stats-intro">
        <span className="eyebrow"><span className="eyebrow-dot" /> SEKILAS PERJALANAN</span>
        <h1 aria-label="Ruang baca, dalam angka">Ruang baca,<br />dalam angka.</h1>
        <p>Jejak kecil dari semua cerita yang kamu simpan di rak.</p>
      </section>
      <section className="stats-overview" aria-label="Ringkasan jumlah buku">
        <div className="total-stat">
          <span className="eyebrow muted-eyebrow">TOTAL KOLEKSI</span>
          <strong>{stats.total}</strong>
          <span>buku tersimpan di rakmu</span>
          <span className="total-stat-mark" aria-hidden="true">✳</span>
        </div>
        <div className="category-stats">
          {statDetails.map((item) => (
            <article className={`category-stat stat-${item.key}`} key={item.key}>
              <span className="category-icon" aria-hidden="true">{item.icon}</span>
              <div>
                <span className="category-label">{item.label}</span>
                <strong>{stats[item.key]}</strong>
                <p>{item.note}</p>
              </div>
            </article>
          ))}
        </div>
      </section>
      <section className="reading-note">
        <div className="note-icon" aria-hidden="true">✳</div>
        <div>
          <span className="eyebrow muted-eyebrow">CATATAN KECIL</span>
          <h2>{stats.total ? `Koleksimu paling banyak ada di “${mostCommon.label}”.` : 'Setiap koleksi dimulai dari satu buku.'}</h2>
          <p>{stats.total ? 'Terus nikmati perjalanan membaca dengan ritmemu sendiri.' : 'Tambahkan buku pertama dan mulai isi ruang bacamu.'}</p>
        </div>
        <Link className="text-link" to="/">Lihat rak buku <span aria-hidden="true">↗</span></Link>
      </section>
    </main>
  )
}

Stats.propTypes = {}

export default Stats
