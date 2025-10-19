import { useState } from 'react';

const TypesOfQuery = () => {
    const [selectedConsultType, setSelectedConsultType] = useState<'Presencial' | 'Videoconsulta'>('Presencial');

    return (
        <div className="flex flex-col gap-2">
            <span className="text-sm font-medium text-gray-800">Tipo de consulta</span>

            <div className="flex gap-3">
                {['Presencial', 'Videoconsulta'].map((type) => (
                    <button
                        key={type}
                        onClick={() => setSelectedConsultType(type as 'Presencial' | 'Videoconsulta')}
                        className={`flex-1 px-4 py-1 rounded-full border text-sm font-medium transition-all hover:cursor-pointer duration-200 shadow-sm ${
                            selectedConsultType === type
                                ? 'bg-blue-50 border-blue-200 text-blue-800 shadow-[0_0_6px_rgba(37,99,235,0.2)]'
                                : 'border-blue-100 text-blue-500 hover:bg-blue-50 hover:border-blue-300'
                        }`}>
                        {type}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default TypesOfQuery;
