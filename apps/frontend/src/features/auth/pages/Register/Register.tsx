import RegisterForm from './components/RegisterForm';
import RegisterHeader from './components/RegisterHeader';

const Register = () => {
    return (
        <div className="min-h-screen flex flex-col items-center">
            {/* Contenedor común para header y form */}
            <div className="w-full max-w-sm">
                <RegisterHeader />

                <RegisterForm />
            </div>
        </div>
    );
};

export default Register;
