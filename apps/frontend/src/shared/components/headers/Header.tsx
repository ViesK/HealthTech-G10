interface HeaderProps {
    title: string;
    onBack?: () => void;
}

const Header = ({ title, onBack }: HeaderProps) => {
    return (
        <header className="flex items-center mt-8 py-4 w-full max-w-sm mx-auto">
            {/* Botón de retroceso */}
            {onBack ? (
                <button onClick={onBack} className="text-xl pr-4 hover:cursor-pointer transition-colors">
                    ←
                </button>
            ) : (
                // Placeholder para mantener el título centrado
                <div className="w-6"></div>
            )}

            {/* Título centrado */}
            <h1 className="flex-1 text-center text-sm font-medium">{title}</h1>

            {/* Otro placeholder para balancear el layout */}
            <div className="w-6"></div>
        </header>
    );
};

export default Header;
