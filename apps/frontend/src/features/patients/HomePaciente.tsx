import { HeaderUsuario } from './components/HeaderUsuario';
import { ProximasCitas } from './components/ProximasCitas';
import { SeleccionarReserva } from './components/SeleccionarReserva';
import { TabNav } from '@/shared/components/navigation/TabNav';
import { Home as HomeIcon, Calendar, HeartPulse, ClipboardList } from 'lucide-react';

const HomePaciente = () => {
  //ejemplo
  const nombrePaciente = 'Juan González';
  const avatar = 'https://randomuser.me/api/portraits/men/32.jpg'; 

  const tabs = [
    { id: 'home', label: 'Inicio', icon: <HomeIcon size={22} strokeWidth={2} className="text-black" /> },
    { id: 'reservar', label: 'Reservar', icon: <Calendar size={22} strokeWidth={2} className="text-black" /> },
    { id: 'resultados', label: 'Resultados', icon: <HeartPulse size={22} strokeWidth={2} className="text-black" /> },
    { id: 'historial', label: 'Historial', icon: <ClipboardList size={22} strokeWidth={2} className="text-black" /> },
  ];

  return (
    <div className="min-h-screen flex justify-center items-center bg-gray-200">
      <div
        className="
          relative w-full h-screen bg-gray-50 flex flex-col overflow-hidden
          sm:max-w-[412px] sm:h-[780px] sm:rounded-2xl
          transition-all duration-500
        "
      >
        <div className="flex-1 overflow-y-auto pb-20">
          <HeaderUsuario nombre={nombrePaciente} avatar={avatar} />

          <div className="px-4 space-y-4">
            <ProximasCitas />
            <SeleccionarReserva />
          </div>
        </div>

        <TabNav tabs={tabs} activeTabId="home" />
      </div>
    </div>
  );
};

export default HomePaciente;