import { useState } from 'react';

interface ToggleProps {
    label?: string; // Texto opcional a la izquierda
    initialValue?: boolean;
    onChange?: (checked: boolean) => void;
    disabled?: boolean;
}

const SwitchToggle = ({ label, initialValue = false, onChange, disabled = false }: ToggleProps) => {
    const [checked, setChecked] = useState(initialValue);

    const handleToggle = () => {
        if (disabled) return;

        const newValue = !checked;

        setChecked(newValue);
        onChange?.(newValue);
    };

    return (
        <div className="flex items-center justify-between w-full max-w-sm select-none">
            {label && <span className="text-sm font-medium text-gray-700">{label}</span>}

            <button
                type="button"
                aria-pressed={checked}
                onClick={handleToggle}
                disabled={disabled}
                className={`relative inline-flex items-center h-6 w-11 rounded-full transition-colors duration-300 hover:cursor-pointer focus:outline-none ${
                    checked ? 'bg-blue-600' : 'bg-gray-300'
                } ${disabled ? 'opacity-60 cursor-not-allowed' : ''}`}>
                <span className={`inline-block w-4 h-4 transform bg-white rounded-full transition-transform duration-300 ${checked ? 'translate-x-5' : 'translate-x-1'}`} />
            </button>
        </div>
    );
};

export default SwitchToggle;
