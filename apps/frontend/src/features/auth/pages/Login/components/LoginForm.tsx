import { useState } from 'react';
import { InputField, PasswordInput, Button } from '@/shared/components';

const LoginForm = () => {
  const [documento, setDocumento] = useState('');
  const [password, setPassword] = useState('');
  const [recordarme, setRecordarme] = useState(false);

  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      
      <div className="bg-white w-full max-w-sm p-6 rounded-md shadow-md border">
        
        
        <div className="flex mb-4 border-b border-gray-300">
          <button className="flex-1 py-2 text-sm font-medium border-b-2 border-blue-600 text-blue-600">
            Portal Paciente
          </button>
          <button className="flex-1 py-2 text-sm font-medium text-gray-500 hover:text-gray-700">
            Portal Profesional
          </button>
        </div>

        <form className="flex flex-col gap-4">
          
          
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
                className="w-4 h-4"
              />
              Recordarme
            </label>
            <a href="#" className="text-blue-600 hover:underline">
              Recuperar contraseña
            </a>
          </div>

          
          <Button label="Ingresar" variant="primary" />

        
          <p className="text-sm text-center text-gray-600">
            ¿Aún no tienes cuenta?{' '}
            <a href="#" className="text-blue-600 hover:underline">
              Crear nuevo usuario
            </a>
          </p>
        </form>
      </div>
    </main>
  );
};

export default LoginForm;