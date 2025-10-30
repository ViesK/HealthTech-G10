import { useState } from 'react';
import { Pencil } from 'lucide-react';

interface SpecialtySelectorProps {
  specialty: string;
  onEdit: () => void;
}

const SpecialtySelector = ({ specialty, onEdit }: SpecialtySelectorProps) => {
  const [selected, setSelected] = useState(true);

  return (
    <div className="flex justify-between items-center w-full">
 
      <button
        onClick={() => setSelected(!selected)}
        className={`flex items-center gap-1 px-2.5 py-1 rounded-full border text-[11px] font-medium transition-all hover:cursor-pointer duration-200 shadow-sm ${
          selected
            ? 'bg-blue-50 border-blue-200 text-blue-800 shadow-[0_0_4px_rgba(37,99,235,0.2)]'
            : 'border-blue-100 text-blue-500 hover:bg-blue-50 hover:border-blue-300'
        }`}
      >
        <span className="text-blue-600 text-sm">💙</span>
        <span>{specialty}</span>
      </button>

      <button
        onClick={onEdit}
        className="flex items-center text-blue-600 hover:underline text-[11px] font-medium ml-2"
      >
        <Pencil size={12} className="mr-1" />
        Modificar
      </button>
    </div>
  );
};

export default SpecialtySelector;