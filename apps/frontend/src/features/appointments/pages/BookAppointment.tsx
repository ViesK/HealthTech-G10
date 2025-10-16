import { useNavigate } from 'react-router-dom';
import { useState } from 'react';
import AppLayout from '@/shared/components/layout/AppLayout';
import AdvancedSearch from '../components/AdvancedSearch';

const BookAppointment = () => {
    const [showAdvanced, setShowAdvanced] = useState(false);
    const navigate = useNavigate();

    const handleBack = () => {
        console.log('Volver atrás');
        navigate(-1);
    };

    return (
        <AppLayout title="Reservar Cita" onBack={handleBack}>
            <div className="flex items-center justify-between">
                <span className="text-sm font-medium">Búsqueda avanzada (opcional)</span>
                <input type="checkbox" checked={showAdvanced} onChange={() => setShowAdvanced(!showAdvanced)} className="toggle toggle-primary" />
            </div>

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
