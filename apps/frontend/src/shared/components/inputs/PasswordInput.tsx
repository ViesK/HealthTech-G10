import React, { useState } from 'react';

type PasswordInputProps = {
  label?: string;
  id?: string;
  name?: string;
  value?: string;
  placeholder?: string;
  required?: boolean;
  disabled?: boolean;
  helperText?: string;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
};

export const PasswordInput: React.FC<PasswordInputProps> = ({
  label = '',
  id,
  name,
  value,
  placeholder,
  required = false,
  disabled = false,
  helperText,
  onChange,
}) => {
  // Estado para mostrar u ocultar la contraseña
  const [showPassword, setShowPassword] = useState(false);

  return (
    <div className="relative w-full">
      {/* Etiqueta */}
      {label && (
        <label htmlFor={id} className="text-sm font-medium text-gray-700">
          {label}
        </label>
      )}

      {/* Input + botón Mostrar/Ocultar */}
      <div className="relative">
        <input
          id={id}
          type={showPassword ? 'text' : 'password'}
          name={name}
          value={value}
          placeholder={placeholder}
          required={required}
          disabled={disabled}
          onChange={onChange}
          className={`w-full border border-gray-300 rounded-sm px-3 py-2 text-sm focus:outline-none focus:border-black pr-16 ${
            disabled ? 'bg-gray-100 cursor-not-allowed' : 'bg-white'
          } transition-colors duration-200 ease-in-out`}
        />

        {/* Botón Mostrar/Ocultar */}
        <button
          type="button"
          onClick={() => setShowPassword(!showPassword)}
          className="absolute right-2 top-1/2 transform -translate-y-1/2 text-xs text-gray-600 hover:text-black focus:outline-none"
          tabIndex={-1}
        >
          {showPassword ? 'Ocultar' : 'Mostrar'}
        </button>
      </div>

      {/* Texto de ayuda */}
      {helperText && <p className="text-xs text-gray-500 mt-1">{helperText}</p>}
    </div>
  );
};