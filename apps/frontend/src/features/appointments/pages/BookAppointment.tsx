import Layout from '@/shared/components/layout/Layout';
import AdvancedSearch from '../components/AdvancedSearch';
// import { useNavigate } from 'react-router-dom';
// import AdvancedSearch from '../components/AdvancedSearch';
// import Header from '@/shared/components/headers/Header';

// const navigate = useNavigate();

const BookAppointment = () => {
    const handleBack = () => {
        console.log('Volver atrás');
        // navigate(-1);
    };

    return (
        // <main className="min-h-screen flex flex-col items-center">
        //     <div className="w-full max-w-sm">
        //         <Header title={'Reservar Cita'} onBack={() => window.history.back()} />
        //     </div>
        // </main>
        <Layout title="Reservar Cita" onBack={handleBack}>
            <AdvancedSearch />
        </Layout>
    );
};

export default BookAppointment;
