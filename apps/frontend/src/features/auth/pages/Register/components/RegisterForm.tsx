import { DateInput, SelectInput } from '@/shared/components';
import { LOCALITY_OPTIONS } from '@/shared/constants';
import { useState } from 'react';

const RegisterForm = () => {
    const [birthDate, setBirthDate] = useState('');
    const [locality, setLocality] = useState('');

    return (
        <main className="p-6">
            <form className="flex flex-col gap-4">
                <label htmlFor=""></label>
                <input type="text" placeholder="Nombre" className="w-full border border-gray-300 rounded-sm p-1 focus:outline-none focus:ring-2 focus:ring-blue-500" />

                <label htmlFor=""></label>
                <input type="text" placeholder="Apellido" className="w-full border border-gray-300 rounded-sm p-1 focus:outline-none focus:ring-2 focus:ring-blue-500" />

                <DateInput label="Fecha de nacimiento" id="birthdate" name="birthdate" value={birthDate} onChange={(dateString) => setBirthDate(dateString)} required />

                <label htmlFor=""></label>
                <input type="email" placeholder="Correo electrónico" className="w-full border border-gray-300 rounded-sm p-1 focus:outline-none focus:ring-2 focus:ring-blue-500" />

                <SelectInput label="Localidad" id="gender" name="gender" value={locality} onChange={setLocality} options={LOCALITY_OPTIONS} required />

                <label htmlFor=""></label>
                <input type="text" placeholder="Domicilio" className="w-full border border-gray-300 rounded-sm p-1 focus:outline-none focus:ring-2 focus:ring-blue-500" />

                <label htmlFor=""></label>
                <input type="number" placeholder="Telefono" className="w-full border border-gray-300 rounded-sm p-1 focus:outline-none focus:ring-2 focus:ring-blue-500" />

                <label htmlFor=""></label>
                <input type="password" placeholder="Contraseña" className="w-full border border-gray-300 rounded-sm p-1 focus:outline-none focus:ring-2 focus:ring-blue-500" />

                <label htmlFor=""></label>
                <input type="password" placeholder="Confirmar contraseña" className="w-full border border-gray-300 rounded-sm p-1 mb-6 focus:outline-none focus:ring-2 focus:ring-blue-500" />

                <button type="submit" className="w-full bg-blue-600 text-white font-semibold py-3 rounded-sm hover:bg-blue-700 transition-colors">
                    Crear cuenta
                </button>
            </form>
        </main>
    );
};

export default RegisterForm;
