import { fireEvent, render, screen, within } from '@testing-library/react'
import { beforeEach, describe, expect, it, vi } from 'vitest'
import { MemoryRouter } from 'react-router-dom'
import App from '../App.jsx'

function renderApp(path = '/') {
  return render(
    <MemoryRouter initialEntries={[path]}>
      <App />
    </MemoryRouter>,
  )
}

describe('React Task Manager module', () => {
  beforeEach(() => window.localStorage.clear())

  it('renders the reusable header, navigation, and empty task state', () => {
    renderApp()
    expect(screen.getByRole('heading', { name: 'React Task Manager' })).toBeInTheDocument()
    expect(screen.getByRole('navigation', { name: 'Navigasi utama' })).toBeInTheDocument()
    expect(screen.getByText('Belum ada tugas. Tambahkan tugas baru di atas!')).toBeInTheDocument()
  })

  it('validates the required task title', () => {
    renderApp()
    fireEvent.click(screen.getByRole('button', { name: 'Tambah', exact: true }))
    expect(screen.getByRole('alert')).toHaveTextContent('Judul tugas wajib diisi.')
    expect(screen.getByLabelText('Judul tugas baru')).toHaveAttribute('aria-invalid', 'true')
  })

  it('adds a task and persists it in localStorage', () => {
    renderApp()
    fireEvent.change(screen.getByLabelText('Judul tugas baru'), { target: { value: 'Mempelajari React' } })
    fireEvent.click(screen.getByRole('button', { name: 'Tambah', exact: true }))
    expect(screen.getByText('Mempelajari React')).toBeInTheDocument()
    expect(JSON.parse(window.localStorage.getItem('tasks_data'))[0]).toMatchObject({
      title: 'Mempelajari React',
      completed: false,
    })
  })

  it('toggles completion and updates task statistics', () => {
    window.localStorage.setItem('tasks_data', JSON.stringify([
      { id: 7, title: 'Baca modul React', completed: false },
    ]))
    renderApp()
    fireEvent.click(screen.getByRole('checkbox', { name: 'Tandai Baca modul React sebagai selesai' }))
    expect(screen.getByText('Selesai').parentElement).toHaveTextContent('1')
    expect(JSON.parse(window.localStorage.getItem('tasks_data'))[0].completed).toBe(true)
  })

  it('deletes an individual task', () => {
    window.localStorage.setItem('tasks_data', JSON.stringify([
      { id: 7, title: 'Tugas yang dihapus', completed: false },
    ]))
    renderApp()
    fireEvent.click(screen.getByRole('button', { name: 'Hapus' }))
    expect(screen.queryByText('Tugas yang dihapus')).not.toBeInTheDocument()
  })

  it('clears all tasks only after confirmation', () => {
    window.localStorage.setItem('tasks_data', JSON.stringify([
      { id: 7, title: 'Tugas pertama', completed: false },
    ]))
    const confirmation = vi.spyOn(window, 'confirm').mockReturnValue(true)
    renderApp()
    fireEvent.click(screen.getByRole('button', { name: 'Hapus semua tugas' }))
    expect(confirmation).toHaveBeenCalledOnce()
    expect(screen.queryByText('Tugas pertama')).not.toBeInTheDocument()
  })

  it('shares task statistics with the About page via context', () => {
    window.localStorage.setItem('tasks_data', JSON.stringify([
      { id: 7, title: 'Selesai', completed: true },
      { id: 8, title: 'Aktif', completed: false },
    ]))
    renderApp('/about')
    expect(screen.getByText(/Saat ini Anda memiliki total/)).toHaveTextContent('Saat ini Anda memiliki total 2 tugas')
    expect(screen.getByText(/Saat ini Anda memiliki total/)).toHaveTextContent('2 tugas yang tersimpan')
  })

  it('shows the custom 404 page for unknown routes', () => {
    renderApp('/alamat-salah')
    expect(screen.getByRole('heading', { name: 'Halaman tidak ditemukan' })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: 'Kembali ke beranda' })).toHaveAttribute('href', '/')
  })

  it('provides interactive counter and immutable array exercises', () => {
    renderApp()
    const counter = screen.getByRole('region', { name: 'Latihan counter' })
    fireEvent.click(within(counter).getByRole('button', { name: 'Tambah (+1)' }))
    expect(within(counter).getByText('1')).toBeInTheDocument()
    const arrayExercise = screen.getByRole('region', { name: 'Latihan array state' })
    fireEvent.click(within(arrayExercise).getByRole('button', { name: 'Tambah item' }))
    expect(within(arrayExercise).getByText('Tugas Baru ke-1')).toBeInTheDocument()
    fireEvent.click(within(arrayExercise).getByRole('button', { name: 'Hapus' }))
    expect(within(arrayExercise).queryByText('Tugas Baru ke-1')).not.toBeInTheDocument()
  })
})
