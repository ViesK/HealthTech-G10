import { Calendar } from 'lucide-react';
import React from 'react';

interface DateSelectorProps {
  date: string;
  onChange: (newDate: string) => void;
}

const DateSelector: React.FC<DateSelectorProps> = ({ date, onChange }) => {
  return (
    <div className="flex flex-col gap-0.5">
      <label className="text-[11px] font-medium text-gray-800 mb-0.5">
        A partir de
      </label>
      <div className="relative">
        <Calendar size={14} className="absolute left-2.5 top-1.5 text-gray-500" />
        <input
          type="date"
          value={date}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            onChange(e.target.value)
          }
          className="w-full border border-gray-300 rounded-md pl-8 pr-2 py-1 text-[11px] focus:ring-1 focus:ring-blue-200 focus:border-blue-400 bg-white"
        />
      </div>
    </div>
  );
};

export default DateSelector;