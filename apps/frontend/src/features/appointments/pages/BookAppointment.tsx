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
            <div className="flex items-center justify-between w-full max-w-sm">
                <span className="text-sm font-medium text-gray-700">Búsqueda avanzada (opcional)</span>

                <button
                    type="button"
                    aria-pressed={showAdvanced}
                    onClick={() => setShowAdvanced(!showAdvanced)}
                    className={`relative inline-flex items-center h-6 w-11 rounded-full transition-colors duration-300 hover:cursor-pointer focus:outline-none ${
                        showAdvanced ? 'bg-blue-600' : 'bg-gray-300'
                    }`}>
                    <span className={`inline-block w-4 h-4 transform bg-white rounded-full transition-transform duration-300 ${showAdvanced ? 'translate-x-5' : 'translate-x-1'}`} />
                </button>
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
