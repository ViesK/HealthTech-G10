import { useState } from 'react';

const TypesOfQuery = () => {
    const [selectedConsultType, setSelectedConsultType] = useState<'Presencial' | 'Videoconsulta'>('Presencial');

    return (
        <div className="flex flex-col gap-2">
            <span className="text-sm font-medium">Tipo de consulta</span>
            <div className="flex gap-2">
                {['Presencial', 'Videoconsulta'].map((type) => (
                    <button
                        key={type}
                        onClick={() => setSelectedConsultType(type as 'Presencial' | 'Videoconsulta')}
                        className={`flex-1 px-4 py-2 rounded-lg border text-sm font-medium transition-all duration-200 ${
                            selectedConsultType === type ? 'bg-blue-100 border-blue-500 text-blue-600' : 'border-gray-300 text-gray-700 hover:bg-gray-100'
                        }`}>
                        {type}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default TypesOfQuery;
