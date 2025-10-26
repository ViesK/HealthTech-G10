import { Filter } from 'lucide-react';
import AppLayout from '../../../shared/components/layouts/AppLayout';
import AttentionCard from '../components/AttentionCard';


const HistoryPage = () => {
// prueba
  const records = [
    { doctor: 'Dr. Gutiérrez Hugo', specialty: 'Medicina familiar', date: '05-10-25', color: 'blue' },
    { doctor: 'Dr. Belli Patricia', specialty: 'Atención por guardia', date: '28-09-25', color: 'red' },
    { doctor: 'Dr. Quiróz Rubén', specialty: 'Gastroenterología', date: '17-09-25', color: 'yellow' },
    { doctor: 'RMN de Hombro Izquierdo s/c', specialty: 'Resonancia', date: '12-04-25', color: 'purple' },
    { doctor: 'Dr. Carter Miguel', specialty: 'Traumatología', date: '10-04-25', color: 'blue' },
    { doctor: 'Análisis de sangre', specialty: 'Laboratorio', date: '24-01-25', color: 'orange' },
  ];

  return (
    <AppLayout
      title="Historial Clínico"
      onBack={() => window.history.back()}
    >
      
      <div className="flex justify-end mb-2">
        <button onClick={() => alert('Abrir filtro')}>
          <Filter size={18} className="text-blue-500" />
        </button>
      </div>

    
      <p className="text-gray-500 text-sm mb-1">Sus atenciones</p>
      <p className="text-gray-400 text-xs mb-3">AÑO 2025</p>

      
      <div className="flex flex-col gap-3">
        {records.map((item, i) => (
          <AttentionCard
            key={i}
            doctor={item.doctor}
            specialty={item.specialty}
            date={item.date}
            color={item.color}
          />
        ))}
      </div>
    </AppLayout>
  );
};

export default HistoryPage;