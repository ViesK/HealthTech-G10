import Header from '@/shared/components/headers/Header';

const BookAppointment = () => {
    return (
        <div className="min-h-screen flex flex-col items-center">
            <div className="w-full max-w-sm">
                <Header title={'Registrarse'} onBack={() => window.history.back()} />
            </div>
        </div>
    );
};

export default BookAppointment;
