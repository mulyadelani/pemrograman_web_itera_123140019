import { fireEvent, render, screen, waitFor, within } from '@testing-library/react'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { MemoryRouter } from 'react-router-dom'
import App from '../App.jsx'

function renderApp(route = '/') {
  return render(
    <MemoryRouter initialEntries={[route]}>
      <App />
    </MemoryRouter>,
  )
}

function openForm() {
  fireEvent.click(screen.getByRole('button', { name: /tambah buku/i }))
}

function submitForm(buttonName) {
  fireEvent.click(within(screen.getByRole('dialog')).getByRole('button', { name: buttonName, exact: true }))
}

function fillBook({ title = 'Laut Bercerita', author = 'Leila S. Chudori', status } = {}) {
  fireEvent.change(screen.getByLabelText('Judul buku'), { target: { value: title } })
  fireEvent.change(screen.getByLabelText('Nama penulis'), { target: { value: author } })
  if (status) fireEvent.change(screen.getByLabelText('Status buku'), { target: { value: status } })
}

describe('RakBuku', () => {
  beforeEach(() => window.localStorage.clear())
  afterEach(() => vi.restoreAllMocks())

  it('menampilkan halaman perpustakaan dan keadaan kosong', () => {
    renderApp()
    expect(screen.getByRole('heading', { name: /setiap buku punya tempatnya sendiri/i })).toBeInTheDocument()
    expect(screen.getByText('Rakmu masih kosong')).toBeInTheDocument()
  })

  it('menampilkan pesan validasi jika judul dan penulis kosong', () => {
    renderApp()
    openForm()
    submitForm('Tambah buku')
    expect(screen.getByText('Judul buku wajib diisi.')).toBeInTheDocument()
    expect(screen.getByText('Nama penulis wajib diisi.')).toBeInTheDocument()
    expect(screen.getByLabelText('Judul buku')).toHaveAttribute('aria-invalid', 'true')
  })

  it('menambahkan buku baru dan menyimpannya ke localStorage', async () => {
    renderApp()
    openForm()
    fillBook()
    submitForm('Tambah buku')
    expect(await screen.findByRole('heading', { name: 'Laut Bercerita' })).toBeInTheDocument()
    await waitFor(() => {
      expect(JSON.parse(window.localStorage.getItem('rakbuku-books'))[0]).toMatchObject({
        title: 'Laut Bercerita',
        author: 'Leila S. Chudori',
        status: 'milik',
      })
    })
  })

  it('mencari judul dan penulis tanpa membedakan huruf besar-kecil', async () => {
    window.localStorage.setItem('rakbuku-books', JSON.stringify([
      { id: 'one', title: 'Laut Bercerita', author: 'Leila S. Chudori', status: 'milik' },
      { id: 'two', title: 'Bumi Manusia', author: 'Pramoedya Ananta Toer', status: 'baca' },
    ]))
    renderApp()
    fireEvent.change(screen.getByRole('searchbox'), { target: { value: 'PRAMOEDYA' } })
    expect(screen.getByRole('heading', { name: 'Bumi Manusia' })).toBeInTheDocument()
    expect(screen.queryByRole('heading', { name: 'Laut Bercerita' })).not.toBeInTheDocument()
  })

  it('memfilter buku berdasarkan status', () => {
    window.localStorage.setItem('rakbuku-books', JSON.stringify([
      { id: 'one', title: 'Laut Bercerita', author: 'Leila S. Chudori', status: 'milik' },
      { id: 'two', title: 'Bumi Manusia', author: 'Pramoedya Ananta Toer', status: 'baca' },
    ]))
    renderApp()
    fireEvent.click(screen.getByRole('button', { name: 'Sedang dibaca' }))
    expect(screen.getByRole('heading', { name: 'Bumi Manusia' })).toBeInTheDocument()
    expect(screen.queryByRole('heading', { name: 'Laut Bercerita' })).not.toBeInTheDocument()
  })

  it('mengedit judul dan status buku', async () => {
    window.localStorage.setItem('rakbuku-books', JSON.stringify([
      { id: 'one', title: 'Laut Bercerita', author: 'Leila S. Chudori', status: 'milik' },
    ]))
    renderApp()
    fireEvent.click(screen.getByRole('button', { name: 'Opsi Laut Bercerita' }))
    fireEvent.click(screen.getByRole('button', { name: 'Edit buku' }))
    fillBook({ title: 'Laut Bercerita (Edisi Baru)', status: 'baca' })
    submitForm('Simpan perubahan')
    expect(await screen.findByRole('heading', { name: 'Laut Bercerita (Edisi Baru)' })).toBeInTheDocument()
    await waitFor(() => {
      expect(JSON.parse(window.localStorage.getItem('rakbuku-books'))[0].status).toBe('baca')
    })
  })

  it('menghapus buku setelah konfirmasi', async () => {
    window.localStorage.setItem('rakbuku-books', JSON.stringify([
      { id: 'one', title: 'Laut Bercerita', author: 'Leila S. Chudori', status: 'milik' },
    ]))
    vi.spyOn(window, 'confirm').mockReturnValue(true)
    renderApp()
    fireEvent.click(screen.getByRole('button', { name: 'Opsi Laut Bercerita' }))
    fireEvent.click(screen.getByRole('button', { name: 'Hapus buku' }))
    expect(screen.queryByRole('heading', { name: 'Laut Bercerita' })).not.toBeInTheDocument()
    await waitFor(() => expect(JSON.parse(window.localStorage.getItem('rakbuku-books'))).toEqual([]))
  })

  it('menampilkan ringkasan statistik di halaman terpisah', () => {
    window.localStorage.setItem('rakbuku-books', JSON.stringify([
      { id: 'one', title: 'Laut Bercerita', author: 'Leila S. Chudori', status: 'milik' },
      { id: 'two', title: 'Bumi Manusia', author: 'Pramoedya Ananta Toer', status: 'baca' },
    ]))
    renderApp('/statistik')
    expect(screen.getByRole('heading', { name: /ruang baca, dalam angka/i })).toBeInTheDocument()
    expect(screen.getByText('2', { selector: '.total-stat strong' })).toBeInTheDocument()
    expect(within(screen.getByLabelText('Ringkasan jumlah buku')).getByText('Sedang dibaca')).toBeInTheDocument()
  })
})
