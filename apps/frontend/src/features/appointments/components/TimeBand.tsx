import { TIMES_BANDS } from '@/shared/constants';
import { useState } from 'react';

const TimeBand = () => {
    const [selectedTime, setSelectedTime] = useState<string | null>(null);

    const toggleTime = (label: string) => {
        setSelectedTime((prev) => (prev === label ? null : label));
    };

    return (
        <div className="flex flex-col gap-2">
            <span className="text-sm font-medium">Banda horaria</span>
            <div className="flex gap-2 flex-wrap">
                {TIMES_BANDS.map((time) => (
                    <button
                        key={time.label}
                        onClick={() => toggleTime(time.label)}
                        className={`flex-1 flex items-center justify-center gap-2 px-4 py-2 border rounded-lg text-sm transition-all duration-200 ${
                            selectedTime === time.label ? 'bg-blue-100 border-blue-500 text-blue-600' : 'border-gray-300 text-gray-700 hover:bg-gray-100'
                        }`}>
                        <span>{time.icon}</span>
                        {time.label}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default TimeBand;
