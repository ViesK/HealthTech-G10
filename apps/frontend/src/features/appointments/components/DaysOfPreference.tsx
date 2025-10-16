import { DAYS_OF_PREFERENCE } from '@/shared/constants';
import { useState } from 'react';

const DaysOfPreference = () => {
    const [selectedDays, setSelectedDays] = useState<string[]>([]);

    const toggleDay = (day: string) => {
        setSelectedDays((prev) => (prev.includes(day) ? prev.filter((d) => d !== day) : [...prev, day]));
    };

    return (
        <div className="flex flex-col gap-2">
            <span className="text-sm font-medium">Días de preferencia</span>
            <div className="flex gap-2 flex-wrap">
                {DAYS_OF_PREFERENCE.map((day) => (
                    <button
                        key={day}
                        onClick={() => toggleDay(day)}
                        className={`px-3 py-1 rounded-lg border text-sm transition-all duration-200 ${
                            selectedDays.includes(day) ? 'bg-blue-100 border-blue-500 text-blue-600' : 'border-gray-300 text-gray-700 hover:bg-gray-100'
                        }`}>
                        {day}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default DaysOfPreference;
