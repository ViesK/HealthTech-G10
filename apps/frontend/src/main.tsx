import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import './shared/styles/global.css';
import { store } from './app/store/store';
<<<<<<< HEAD
=======
import BookAppointment from './features/appointments/pages/BookAppointment';
import { BrowserRouter,Routes,Route } from 'react-router-dom';
// import Home from './features/home/pages/Home';
import Login from './features/auth/pages/Login/Login';
import HomePaciente from './features/patients/HomePaciente';
import Register from './features/auth/pages/Register/Register';
//import HomePaciente from './features/patients/HomePaciente';
>>>>>>> 5204d27d122c057daaf924357101d528916ed669

// Páginas
import Home from './features/home/pages/Home';
import Login from './features/auth/pages/Login/Login';
import Register from './features/auth/pages/Register/Register';
import HomePaciente from './features/patients/HomePaciente';
import BookAppointment from './features/appointments/pages/BookAppointment';

ReactDOM.createRoot(document.getElementById('root')!).render(
<<<<<<< HEAD
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
=======
    <Provider store={store}>
        {/* <RouterProvider router={router} /> */}
        <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login />}></Route>
          <Route path="/register" element={<Register />}></Route>
          <Route path="/portal/paciente" element={<HomePaciente />}></Route>
          <Route path="/consulta" element={<BookAppointment />} />

        </Routes>
        </BrowserRouter>
    </Provider>
);
>>>>>>> 5204d27d122c057daaf924357101d528916ed669
