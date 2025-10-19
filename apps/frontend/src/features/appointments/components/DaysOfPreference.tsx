import { DAYS_OF_PREFERENCE } from '@/shared/constants';
import { useState } from 'react';

const DaysOfPreference = () => {
    const [selectedDays, setSelectedDays] = useState<string[]>([]);

    const toggleDay = (day: string) => {
        setSelectedDays((prev) => (prev.includes(day) ? prev.filter((d) => d !== day) : [...prev, day]));
    };

    return (
        <div className="flex flex-col gap-2">
            <span className="text-sm font-medium text-gray-800">Días de preferencia</span>

            <div className="flex flex-wrap gap-2">
                {DAYS_OF_PREFERENCE.map((day) => (
                    <button
                        key={day}
                        onClick={() => toggleDay(day)}
                        className={`w-9 h-9 rounded-xl border text-sm font-medium transition-all hover:cursor-pointer duration-200 shadow-sm ${
                            selectedDays.includes(day)
                                ? 'bg-blue-50 border-blue-200 text-blue-800 shadow-[0_0_6px_rgba(37,99,235,0.2)]'
                                : 'border-blue-100 text-blue-500 hover:bg-blue-50 hover:border-blue-300'
                        }`}>
                        {day}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default DaysOfPreference;
