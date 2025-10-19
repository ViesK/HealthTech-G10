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
            <div className="flex items-center">
                <p className="text-sm font-medium text-gray-700">Busqueda Avanzada</p>

                <SwitchToggle label="(opcional)" initialValue={showAdvanced} onChange={setShowAdvanced} />
            </div>

            {showAdvanced && (
                <div className="mt-4">
                    <AdvancedSearch />
                </div>
            )}
        </AppLayout>
    );
};

export default BookAppointment;
