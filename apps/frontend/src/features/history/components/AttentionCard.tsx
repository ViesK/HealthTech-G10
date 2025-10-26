import { useState } from 'react';
import { Download } from 'lucide-react';

interface AttentionCardProps {
  doctor: string;
  specialty: string;
  date: string;
  color?: string;
  type?: 'doctor' | 'study'; 
}

const AttentionCard = ({
  doctor,
  specialty,
  date,
  color = 'blue',
  type = 'doctor', // por defecto
}: AttentionCardProps) => {
  const [expanded, setExpanded] = useState(false);

  const colorMap: Record<string, string> = {
    blue: 'bg-blue-400',
    red: 'bg-red-400',
    yellow: 'bg-yellow-400',
    orange: 'bg-orange-400',
    purple: 'bg-purple-400',
  };

  return (
    <div
      className="bg-white rounded-2xl p-3 shadow-sm border border-gray-100 transition-all duration-300 hover:shadow-md"
    >
      
      <button
        onClick={() => setExpanded(!expanded)}
        className="flex items-center justify-between w-full text-left"
      >
        <div className="flex items-center gap-3">
          <div className={`w-1.5 h-10 rounded-full ${colorMap[color]} flex-shrink-0`} />
          <div>
            <p className="text-sm font-semibold text-gray-800">{doctor}</p>
            <p className="text-xs text-gray-500">{specialty}</p>
          </div>
        </div>
        <span className="text-xs text-gray-400">{date}</span>
      </button>

     
      <div
        className={`overflow-hidden transition-all duration-300 ${
          expanded ? 'max-h-20 mt-3 opacity-100' : 'max-h-0 opacity-0'
        }`}
      >
        {type === 'doctor' ? (
          <div className="flex gap-2 justify-end">
            <button className="border border-blue-400 text-blue-600 text-xs font-medium rounded-full px-3 py-1 hover:bg-blue-50 transition">
              Ver resumen
            </button>
            <button className="bg-blue-600 text-white text-xs font-medium rounded-full px-3 py-1 hover:bg-blue-700 transition">
              Reservar nueva cita
            </button>
          </div>
        ) : (
          <div className="flex gap-2 justify-end">
            <button className="border border-blue-400 text-blue-600 text-xs font-medium rounded-full px-3 py-1 flex items-center gap-1 hover:bg-blue-50 transition">
              <Download size={14} /> Descargar
            </button>
            <button className="bg-blue-600 text-white text-xs font-medium rounded-full px-3 py-1 hover:bg-blue-700 transition">
              Ver informe
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default AttentionCard;