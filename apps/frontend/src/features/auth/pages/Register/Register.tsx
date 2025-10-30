import Header from '@/shared/components/headers/Header';
import RegisterForm from './components/RegisterForm';

const Register = () => {
    return (
        <div className="min-h-screen flex flex-col items-center">
            <div className="w-full max-w-sm">
                <Header title={'Registrarse'} onBack={() => window.history.back()} />

                <RegisterForm />
            </div>
        </div>
    );
};

export default Register;
