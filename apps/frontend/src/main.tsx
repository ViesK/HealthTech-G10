import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import './shared/styles/global.css';
import { store } from './app/store/store';

// Páginas
import Home from './features/home/pages/Home';
import Login from './features/auth/pages/Login/Login';
import Register from './features/auth/pages/Register/Register';
import HomePaciente from './features/patients/HomePaciente';
import BookAppointment from './features/appointments/pages/BookAppointment';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <Provider store={store}>
    <BrowserRouter>
      <Routes>
        {/* Inicio */}
        <Route path="/" element={<Home />} />

        {/* Auth */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Paciente */}
        <Route path="/paciente" element={<HomePaciente />} />

        {/* Citas */}
        <Route path="/appointments/book" element={<BookAppointment />} />

        {/* Redirección por defecto */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  </Provider>
);
