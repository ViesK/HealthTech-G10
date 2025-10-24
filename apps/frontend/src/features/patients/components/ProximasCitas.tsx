import { Calendar, Clock, MapPin, Video } from 'lucide-react';

type Cita = {
  id: number;
  fecha: string;
  hora: string;
  medico: string;
  especialidad: string;
  tipo: string;
  foto: string;
};

export const ProximasCitas = () => {
  //  ejemplo (provisorios)
  const citas: Cita[] = [
    {
      id: 1,
      fecha: 'Miércoles 22 de OCT, 2025',
      hora: '07:15',
      medico: 'Dra. Laura Pérez',
      especialidad: 'Dermatología',
      tipo: 'Videoconsulta',
      foto: 'https://images.unsplash.com/photo-1607746882042-944635dfe10e?auto=format&fit=crop&w=150&q=80',
    },
 
  ];

  return (
    <section className="p-4">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-lg font-semibold">Próximas citas</h2>
        <button className="text-blue-600 text-sm hover:underline">
          Ver más
        </button>
      </div>

      <div className="space-y-4">
        {citas.map((cita) => (
          <div
            key={cita.id}
            className="bg-white p-4 rounded-2xl shadow flex items-start gap-4"
          >
           
            <img
              src={cita.foto}
              alt={cita.medico}
              className="w-16 h-16 rounded-xl object-cover"
            />

           
            <div className="flex-1">
              <div className="flex items-center gap-2 text-gray-600 text-sm">
                <Calendar className="w-4 h-4 text-red-500" />
                <p>{cita.fecha}</p>
              </div>

              <div className="flex items-center gap-2 text-gray-600 text-sm mt-1">
                <Clock className="w-4 h-4 text-red-500" />
                <p>{cita.hora} hs</p>
              </div>

              <div className="flex items-center gap-2 mt-2">
                <MapPin className="w-4 h-4 text-blue-500" />
                <p className="font-semibold">{cita.medico}</p>
                <span className="text-gray-500 text-sm">
                  {cita.especialidad}
                </span>
              </div>

             
              <div className="mt-3 flex items-center gap-2">
                <span className="bg-blue-100 text-blue-700 text-xs font-medium px-2 py-1 rounded-full">
                  {cita.tipo}
                </span>

                <button
                  disabled
                  className="flex items-center justify-center gap-1 text-gray-400 bg-gray-100 rounded-full px-3 py-1 text-sm cursor-not-allowed"
                >
                  <Video className="w-4 h-4" />
                  Unirse
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};