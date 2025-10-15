interface HeaderProps {
    title: string;
    onBack?: () => void;
}

const Header = ({ title, onBack }: HeaderProps) => {
    return (
        <header className="flex items-center mt-8 p-4 relative">
            {onBack && (
                <button onClick={onBack} className="absolute left-0 text-xl pl-10 hover:cursor-pointer transition-colors">
                    ←
                </button>
            )}

            <h1 className="mx-auto text-sm font-medium">{title}</h1>
        </header>
    );
};

export default Header;
