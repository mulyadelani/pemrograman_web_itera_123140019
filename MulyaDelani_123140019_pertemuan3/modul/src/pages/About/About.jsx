import PropTypes from 'prop-types'
import Header from '../../components/Header/Header.jsx'
import useTasks from '../../hooks/useTasks.js'

function About() {
  const { stats } = useTasks()

  return (
    <div className="page-container">
      <Header title="Tentang Task Manager" description="Aplikasi manajemen tugas praktikum Pemrograman Web." />
      <main className="container" style={{ paddingTop: 18 }}>
        <article className="about-content">
          <h2>Tentang aplikasi</h2>
          <p>
            Aplikasi Task Manager ini dibangun menggunakan React modern dengan functional components,
            React Hooks (useState, useEffect), Context API, dan React Router.
          </p>
          <p className="about-stat">
            Saat ini Anda memiliki total <strong>{stats.total}</strong> tugas yang tersimpan di sistem.
            {' '}Dari jumlah tersebut, <strong>{stats.completed}</strong> tugas sudah selesai.
          </p>
          <h3>Fitur yang dipraktikkan</h3>
          <ul>
            <li>Komponen reusable, props, dan validasi PropTypes.</li>
            <li>Tambah, tandai selesai, hapus tugas, dan konfirmasi hapus semua.</li>
            <li>Penyimpanan localStorage melalui custom hook.</li>
            <li>Global task state melalui Context API dan ringkasan statistik.</li>
            <li>Navigasi SPA, halaman About, dan penanganan halaman 404.</li>
            <li>Custom hook untuk mendeteksi lebar layar desktop atau mobile.</li>
          </ul>
        </article>
      </main>
    </div>
  )
}

About.propTypes = {}

export default About
