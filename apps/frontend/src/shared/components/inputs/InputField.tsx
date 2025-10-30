import React from 'react';

type InputFieldProps = {
  label?: string;
  id?: string;
  type: string;
  name?: string;
  value?: string;
  placeholder?: string;
  required?: boolean;
  disabled?: boolean;
  helperText?: string;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
};

export const InputField: React.FC<InputFieldProps> = ({
  label = '',
  id,
  type,
  name,
  value,
  placeholder,
  required = false,
  disabled = false,
  helperText,
  onChange,
}) => {
  return (
    <div className="w-full mb-4">
      {/* Label */}
      {label && (
        <label
          htmlFor={id}
          className="block text-sm font-medium text-gray-700 mb-1"
        >
          {label}
        </label>
      )}

      {/* Input */}
      <input
        id={id}
        type={type}
        name={name}
        value={value}
        placeholder={placeholder}
        required={required}
        disabled={disabled}
        onChange={onChange}
        className={`w-full rounded-md border border-gray-300 bg-[#ffffff] px-3 py-2.5 text-sm text-gray-900 placeholder-gray-400 
        focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 
        ${disabled ? 'opacity-70 cursor-not-allowed' : ''} 
        transition-all duration-200 ease-in-out`}
        style={{ backgroundColor: '#ffffff' }} // 🔒 Fuerza blanco absoluto
      />

      {/* Helper Text */}
      {helperText && <p className="text-xs text-gray-500 mt-1">{helperText}</p>}
    </div>
  );
};