import { useState } from 'react';
import TypesOfQuery from './TypesOfQuery';
import { Button, SelectInput } from '@/shared/components';
import DaysOfPreference from './DaysOfPreference';
import TimeBand from './TimeBand';

const CENTER_OPTIONS = [
    { label: 'Centro Médico Belgrano', value: 'belgrano' },
    { label: 'Hospital Italiano', value: 'italiano' },
    { label: 'Clínica Santa Fe', value: 'santa_fe' },
];

const AdvancedSearch = () => {
    const [medicalCenter, setMedicalCenter] = useState('');

    return (
        <section className="mt-6 flex flex-col gap-5 w-full">
            {/* Tipo de consulta */}
            <TypesOfQuery />

            {/* Lugar o selección */}
            <SelectInput label="Centro médico" id="medicalCenter" name="medicalCenter" value={medicalCenter} onChange={setMedicalCenter} options={CENTER_OPTIONS} required />

            {/* Días de preferencia */}
            <DaysOfPreference />

            {/* Banda horaria */}
            <TimeBand />

            {/* Botón Buscar */}
            <Button label="Buscar" variant="primary" />
        </section>
    );
};

export default AdvancedSearch;
