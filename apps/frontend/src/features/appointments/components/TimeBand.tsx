import { TIMES_BANDS } from '@/shared/constants';
import { useState } from 'react';

const TimeBand = () => {
  const [selectedTime, setSelectedTime] = useState<string | null>(null);

  const toggleTime = (label: string) => {
    setSelectedTime((prev) => (prev === label ? null : label));
  };

  return (
    <div className="flex flex-col gap-2">
      <span className="text-sm font-medium text-gray-800">Banda horaria</span>

      <div className="flex gap-2 flex-wrap">
        {TIMES_BANDS.map((time) => (
          <button
            key={time.label}
            onClick={() => toggleTime(time.label)}
            className={`flex-1 flex items-center justify-center gap-2 px-4 py-1 border rounded-full text-sm transition-all duration-200 shadow-sm
              ${
                selectedTime === time.label
                  ? 'bg-blue-50 border-blue-300 text-blue-800 shadow-[0_0_6px_rgba(37,99,235,0.2)]'
                  : 'bg-white border-blue-200 text-blue-600 hover:bg-blue-50 hover:border-blue-300'
              }`}
          >
            <span>{time.icon}</span>
            {time.label}
          </button>
        ))}
      </div>
    </div>
  );
};

export default TimeBand;