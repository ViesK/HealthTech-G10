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
    <div className="relative w-full">
      {/* Label */}
      {label && (
        <label htmlFor={id} className="text-sm font-medium text-gray-700">
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
        className={`w-full border border-gray-300 rounded-sm px-3 py-2 text-sm focus:outline-none focus:border-black ${
          disabled ? 'bg-gray-100 cursor-not-allowed' : 'bg-white'
        } transition-colors duration-200 ease-in-out`}
      />

      {/* Helper Text */}
      {helperText && <p className="text-xs text-gray-500 mt-1">{helperText}</p>}
    </div>
  );
};

