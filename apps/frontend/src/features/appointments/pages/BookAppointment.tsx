import Header from '@/shared/components/headers/Header';

const BookAppointment = () => {
    return (
        <main className="min-h-screen flex flex-col items-center">
            <div className="w-full max-w-sm">
                <Header title={'Reservar Cita'} onBack={() => window.history.back()} />
            </div>
        </main>
    );
};

export default BookAppointment;
