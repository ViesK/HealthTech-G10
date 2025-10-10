const RegisterHeader = () => {
    return (
        <header className="flex items-center mt-8 p-4 relative">
            {/* Flecha */}
            <button className="absolute left-0 text-xl pl-10">←</button>

            {/* Título centrado */}
            <h1 className="mx-auto text-sm">Registrarse</h1>
        </header>
    );
};

export default RegisterHeader;
