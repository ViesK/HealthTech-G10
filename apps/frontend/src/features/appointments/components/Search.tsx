import { useState } from 'react';
import SpecialtySelector from './SpecialtySelector';
import DateSelector from './DateSelector';

const Search = () => {
  const [specialty, setSpecialty] = useState('Dermatología');
  const [date, setDate] = useState('2025-10-20');

  const handleEdit = () => {
    console.log('Modificar especialidad');
  };

  return (
    <div className="bg-transparent w-full max-w-md mx-auto space-y-3">
      
      <h2 className="text-gray-900 font-semibold text-base">Búsqueda</h2>

     
      <p className="text-gray-500 text-xs mb-2">
        Buscar por especialidad o profesional
      </p>

 
      <div className="flex flex-col gap-3">
        <SpecialtySelector specialty={specialty} onEdit={handleEdit} />
        <DateSelector date={date} onChange={setDate} />
      </div>
    </div>
  );
};

export default Search;