import { useState } from 'react';

const days = ['Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa', 'Do'];
const times = [
    { label: 'Mañana', icon: '☀️' },
    { label: 'Tarde', icon: '🌤️' },
    { label: 'Noche', icon: '🌙' },
];

const AdvancedSearch = () => {
    const [selectedConsultType, setSelectedConsultType] = useState<'Presencial' | 'Videoconsulta'>('Presencial');

    return (
        <section className="mt-6 flex flex-col gap-4 w-full">
            {/* Tipo de consulta */}
            <div className="flex flex-col gap-2">
                <span className="text-sm font-medium">Tipo de consulta</span>
                <div className="flex gap-2">
                    <button
                        className={`flex-1 px-4 py-2 rounded-lg border ${selectedConsultType === 'Presencial' ? 'bg-blue-100 border-blue-500' : 'border-gray-300'}`}
                        onClick={() => setSelectedConsultType('Presencial')}>
                        Presencial
                    </button>
                    <button
                        className={`flex-1 px-4 py-2 rounded-lg border ${selectedConsultType === 'Videoconsulta' ? 'bg-blue-100 border-blue-500' : 'border-gray-300'}`}
                        onClick={() => setSelectedConsultType('Videoconsulta')}>
                        Videoconsulta
                    </button>
                </div>
            </div>

            {/* Lugar o selección */}
            <div className="flex flex-col gap-2">
                <label className="text-sm font-medium">A partir de</label>
                <select className="w-full border border-gray-300 rounded-lg px-4 py-2">
                    <option>Seleccionar...</option>
                </select>
            </div>

            {/* Días de preferencia */}
            <div className="flex flex-col gap-2">
                <span className="text-sm font-medium">Días de preferencia</span>
                <div className="flex gap-2">
                    {days.map((day) => (
                        <button key={day} className="px-3 py-1 rounded-lg border border-gray-300 text-sm">
                            {day}
                        </button>
                    ))}
                </div>
            </div>

            {/* Banda horaria */}
            <div className="flex flex-col gap-2">
                <span className="text-sm font-medium">Banda horaria</span>
                <div className="flex gap-2">
                    {times.map((time) => (
                        <button key={time.label} className="flex-1 flex items-center justify-center gap-2 px-4 py-2 border border-gray-300 rounded-lg text-sm">
                            <span>{time.icon}</span>
                            {time.label}
                        </button>
                    ))}
                </div>
            </div>

            {/* Botón Buscar */}
            <button className="mt-4 w-full bg-blue-600 text-white py-3 rounded-lg text-sm font-medium">Buscar</button>
        </section>
    );
};

export default AdvancedSearch;
