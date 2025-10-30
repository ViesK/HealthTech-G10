import React from 'react';

interface SelectOption {
    label: string;
    value: string;
}

interface SelectInputProps {
    label?: string;
    id?: string;
    name?: string;
    value?: string;
    onChange?: (value: string) => void;
    options: SelectOption[];
    required?: boolean;
    disabled?: boolean;
    helperText?: string;
}

export const SelectInput: React.FC<SelectInputProps> = ({ label = 'Selecciona una opción', id, name, value, onChange, options, required = false, disabled = false, helperText }) => {
    return (
        <div className="relative w-full">
            {/* Label */}
            {label && (
                <label htmlFor={id} className="text-sm font-medium text-gray-700">
                    {label}
                </label>
            )}
            {/* Select */}
            <select
                id={id}
                name={name}
                value={value || ''}
                onChange={(e) => onChange?.(e.target.value)}
                required={required}
                disabled={disabled}
                className={`w-full border appearance-none border-gray-300 rounded-sm pl-3 p-1 text-sm text-gray-900 hover:cursor-pointer focus:outline-none focus:border-black focus:border[1px] ${
                    disabled ? 'bg-gray-100 cursor-not-allowed' : 'bg-white'
                } transition-colors duration-200 ease-in-out`}>
                <option value="" className="text-gray-400" disabled>
                    Seleccionar...
                </option>
                {options.map((opt) => (
                    <option key={opt.value} value={opt.value}>
                        {opt.label}
                    </option>
                ))}
            </select>

            <p className="absolute right-3 top-7.5 text-sm w-4 h-4 text-gray-500 pointer-events-none"> ▽ </p>

            {helperText && <p className="text-xs text-gray-500 mt-1">{helperText}</p>}
        </div>
    );
};
