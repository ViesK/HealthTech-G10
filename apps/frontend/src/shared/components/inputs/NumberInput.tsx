import React from 'react';

interface NumberInputProps {
    label?: string;
    id?: string;
    name?: string;
    value?: string | number;
    placeholder?: string;
    required?: boolean;
    disabled?: boolean;
    helperText?: string;
    min?: number;
    max?: number;
    step?: number;
    onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

export const NumberInput: React.FC<NumberInputProps> = ({
    label = '',
    id,
    name,
    value,
    placeholder,
    required = false,
    disabled = false,
    helperText,
    min,
    max,
    step,
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
                type="number"
                name={name}
                value={value}
                placeholder={placeholder}
                required={required}
                disabled={disabled}
                min={min}
                max={max}
                step={step}
                onChange={onChange}
                className={`w-full border border-gray-300 rounded-sm px-3 py-1 text-sm focus:outline-none focus:border-black ${
                    disabled ? 'bg-gray-100 cursor-not-allowed' : 'bg-white'
                } transition-colors duration-200 ease-in-out`}
            />

            {/* Helper Text */}
            {helperText && <p className="text-xs text-gray-500 mt-1">{helperText}</p>}
        </div>
    );
};
