import type { ButtonHTMLAttributes } from 'react';

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
    label: string;
    variant?: 'primary' | 'secondary' | 'danger';
    fullWidth?: boolean;
    loading?: boolean;
}

const baseStyles =
    'rounded-full font-medium text-sm py-2 px-4 transition-all duration-200 ease-in-out hover:cursor-pointer focus:outline-none disabled:opacity-60 disabled:cursor-not-allowed';

export const Button: React.FC<ButtonProps> = ({ label, variant = 'primary', fullWidth = true, loading = false, disabled, ...props }) => {
    const widthClass = fullWidth ? 'w-full' : 'w-auto';

    let variantClasses = '';
    switch (variant) {
        case 'primary':
            variantClasses = 'bg-[#3478C6] text-white hover:bg-[#2f6bb0] active:bg-[#2a5f9b]';
            break;
        case 'secondary':
            variantClasses = 'bg-gray-200 text-gray-800 hover:bg-gray-300 active:bg-gray-400';
            break;
        case 'danger':
            variantClasses = 'bg-red-600 text-white hover:bg-red-700 active:bg-red-800';
            break;
    }

    return (
        <button {...props} disabled={disabled || loading} className={`${baseStyles} ${variantClasses} ${widthClass}`}>
            {loading ? 'Cargando...' : label}
        </button>
    );
};
