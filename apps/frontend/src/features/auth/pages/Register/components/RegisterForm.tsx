import { Button, DateInput, EmailInput, InputField, NumberInput, PasswordInput, SelectInput } from '@/shared/components';
import { LOCALITY_OPTIONS } from '@/shared/constants';
import { useState } from 'react';
import axios from 'axios';

const API_URL = "http://127.0.0.1:8000/api/users/register"; // 🔹 ajustá según tu ruta real
const RegisterForm = () => {
    const [birthDate, setBirthDate] = useState('');
    const [locality, setLocality] = useState('');

    return (
        <main className="py-6">
            <form className="flex flex-col gap-4">
                <InputField label="Nombre" id="firstName" type="text" name="firstName" placeholder="Nombre" />

                <InputField label="Apellido" id="lastName" type="text" name="lastName" placeholder="Apellido" />

                <DateInput label="Fecha de nacimiento" id="birthdate" name="birthdate" value={birthDate} onChange={(dateString) => setBirthDate(dateString)} required />

                <EmailInput label="Correo electrónico" id="email" name="email" placeholder="Correo electrónico" />

                <SelectInput label="Localidad" id="gender" name="gender" value={locality} onChange={setLocality} options={LOCALITY_OPTIONS} required />

                <InputField label="Domicilio" id="address" type="text" name="address" placeholder="Domicilio" />

                <NumberInput label="Teléfono" id="phone" name="phone" placeholder="Teléfono" />

                <PasswordInput label="Contraseña" id="password" name="password" placeholder="Contraseña" />

                <PasswordInput label="Confirmar contraseña" id="confirmPassword" name="confirmPassword" placeholder="Confirmar contraseña" />

                <Button label="Continuar" variant="primary" />
            </form>
        </main>
    );
};

export default RegisterForm;
