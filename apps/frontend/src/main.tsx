import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
// import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './shared/styles/global.css';
// import Register from './features/auth/pages/Register/Register';
import { store } from './app/store/store';
import BookAppointment from './features/appointments/pages/BookAppointment';
import { BrowserRouter } from 'react-router-dom';
// import Home from './features/home/pages/Home';

// import Login from './features/auth/pages/Login/Login';
//import HomePaciente from './features/patients/HomePaciente';

// import Login from './features/auth/pages/Login/Login';
import HomePaciente from './features/patients/HomePaciente';

// const router = createBrowserRouter([{ path: '/', element: <Home /> }]);

ReactDOM.createRoot(document.getElementById('root')!).render(
    import { useState } from "react";
    import axios from "axios";
    
    export default function Login() {
      const [id, setId] = useState("");
      const [password, setPassword] = useState("");
      const [message, setMessage] = useState("");
    
      const handleLogin = async (e) => {
        e.preventDefault();
    
        try {
          const response = await axios.post("http://127.0.0.1:8000/api/users/login", {
            id: Number(id),          // asegurate de enviar número, no string
            password: password
          });
    
          console.log(response.data);   // token y user_type
          setMessage("Login exitoso: " + response.data.user_type);
    
          // Guardar token en localStorage si querés usarlo después
          localStorage.setItem("token", response.data.access_token);
    
        } catch (error) {
          console.error(error.response);
          setMessage("Error: " + error.response?.data?.detail);
        }
      };
    
      return (
        <div>
          <h2>Login</h2>
          <form onSubmit={handleLogin}>
            <input
              type="number"
              placeholder="DNI"
              value={id}
              onChange={(e) => setId(e.target.value)}
            />
            <input
              type="password"
              placeholder="Contraseña"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button type="submit">Ingresar</button>
          </form>
          <p>{message}</p>
        </div>
      );
    }
    <Provider store={store}>
        {/* <RouterProvider router={router} /> */}
        <BrowserRouter>


            <BookAppointment />

            <HomePaciente />

        </BrowserRouter>
    </Provider>
);