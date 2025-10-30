import { useState } from 'react';
import { InputField, PasswordInput, Button } from '@/shared/components';
import axios from "axios";

const LoginForm = () => {
  const [documento, setDocumento] = useState('');
  const [password, setPassword] = useState('');
  const [recordarme, setRecordarme] = useState(false);
  const [message, setMessage] = useState("");
  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/users/login", {
        id: Number(documento),
        password: password,
      });

      const { access_token, user_type, message } = response.data;

      // ✅ Guardar token
      localStorage.setItem("token", access_token);


      // ✅ Ejemplo: redirigir según el tipo de usuario
      if (user_type === "paciente") {
        window.location.href = "/portal/paciente";
      } else if (user_type === "medico") {
        window.location.href = "/portal/profesional";
      }

    } catch (error: any) {
      console.error("Error al hacer login:", error);
      if (error.response) {
        console.log("Respuesta del servidor:", error.response.data);
        setMessage("Error: " + (error.response.data?.detail || "Error en el servidor"));
      } else if (error.request) {
        console.log("No se recibió respuesta del servidor:", error.request);
        setMessage("Error: el servidor no respondió.");
      } else {
        console.log("Error al configurar la petición:", error.message);
        setMessage("Error: " + error.message);
      }
    }
  };

  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      {/* 🔹 Contenedor gris exacto (#f7f9fc) */}
      <div
        className="w-full max-w-sm p-6 rounded-2xl shadow-md border border-gray-200"
        style={{ backgroundColor: '#f7f9fc' }}
      >
        {/* Tabs */}
        <div className="flex mb-4 border-b border-gray-300">
          <button className="flex-1 py-2 text-sm font-medium border-b-2 border-blue-600 text-blue-600 bg-transparent">
            Portal Paciente
          </button>
          <button className="flex-1 py-2 text-sm font-medium text-gray-500 hover:text-gray-700 bg-transparent">
            Portal Profesional
          </button>
        </div>

        {/* Formulario */}
        <form className="flex flex-col gap-4" onSubmit={handleLogin} >
          <InputField
            label="Número de documento"
            id="documento"
            type="text"
            name="documento"
            placeholder="Ej: 123456789"
            value={documento}
            onChange={(e) => setDocumento(e.target.value)}
            required
          />

          <PasswordInput
            label="Contraseña"
            id="password"
            name="password"
            placeholder="Ingresar contraseña"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <div className="flex items-center justify-between text-sm">
            <label className="flex items-center gap-2">
              <input
                type="checkbox"
                checked={recordarme}
                onChange={(e) => setRecordarme(e.target.checked)}
                className="w-4 h-4 accent-blue-600"
              />
              Recordarme
            </label>
            <a href="#" className="text-blue-600 hover:underline">
              Recuperar contraseña
            </a>
          </div>

          <Button label="Ingresar" variant="primary"  />

          <p className="text-sm text-center text-gray-600">
            ¿Aún no tienes cuenta?{' '}
            <a href="/Register" className="text-blue-600 hover:underline">
              Crear nuevo usuario
            </a>
          </p>
        </form>
      </div>
    </main>
  );
};

export default LoginForm;