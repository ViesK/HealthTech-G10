import type { ButtonHTMLAttributes } from 'react';

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
    label: string;
    variant?: 'primary' | 'secondary' | 'danger';
    fullWidth?: boolean;
    loading?: boolean;
}

const baseStyles = 'rounded-sm font-medium text-sm py-3 px-4 transition-all duration-200 ease-in-out focus:outline-none disabled:opacity-60 disabled:cursor-not-allowed';

export const Button: React.FC<ButtonProps> = ({ label, variant = 'primary', fullWidth = true, loading = false, disabled, ...props }) => {
    const widthClass = fullWidth ? 'w-full' : 'w-auto';

    let variantClasses = '';
    switch (variant) {
        case 'primary':
            variantClasses = 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-2 focus:ring-blue-500';
            break;
        case 'secondary':
            variantClasses = 'bg-gray-200 text-gray-800 hover:bg-gray-300 focus:ring-2 focus:ring-gray-400';
            break;
        case 'danger':
            variantClasses = 'bg-red-600 text-white hover:bg-red-700 focus:ring-2 focus:ring-red-500';
            break;
    }

    return (
        <button {...props} disabled={disabled || loading} className={`${baseStyles} ${variantClasses} ${widthClass}`}>
            {loading ? 'Cargando...' : label}
        </button>
    );
};
