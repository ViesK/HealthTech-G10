import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import AppLayout from '@/shared/components/layouts/AppLayout';
import AdvancedSearch from '../components/AdvancedSearch';
import SwitchToggle from '@/shared/components/toggles/SwitchToggle';

const BookAppointment = () => {
    const [showAdvanced, setShowAdvanced] = useState(false);
    const navigate = useNavigate();

    const handleBack = () => {
        console.log('Volver atrás');
        navigate(-1);
    };

    return (
        <AppLayout title="Reservar Cita" onBack={handleBack}>
            <SwitchToggle label="Búsqueda avanzada (opcional)" initialValue={showAdvanced} onChange={setShowAdvanced} />

            {/* Solo mostrar si showAdvanced es true */}
            {/* {showAdvanced && (
                <div className="mt-4">
                    <AdvancedSearch />
                </div>
            )} */}
            <AdvancedSearch />
        </AppLayout>
    );
};

export default BookAppointment;
