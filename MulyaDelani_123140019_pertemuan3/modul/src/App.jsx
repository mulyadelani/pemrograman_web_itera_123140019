import { Navigate, Route, Routes } from 'react-router-dom'
import { TaskProvider } from './context/TaskContext.jsx'
import Navbar from './components/Navbar/Navbar.jsx'
import Home from './pages/Home/Home.jsx'
import About from './pages/About/About.jsx'
import NotFound from './pages/NotFound/NotFound.jsx'

function App() {
  return (
    <TaskProvider>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/modul" element={<Navigate to="/" replace />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
        <footer className="site-footer">
          Latihan React · Components · Props · Hooks · Context API · Router
        </footer>
      </div>
    </TaskProvider>
  )
}

App.propTypes = {}

export default App
