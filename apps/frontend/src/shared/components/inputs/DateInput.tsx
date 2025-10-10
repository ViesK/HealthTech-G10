import { handleDateChange } from '@/shared/helpers';
import ReactDatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';

interface DateInputProps {
    label?: string;
    id?: string;
    value?: string;
    onChange?: (dateString: string) => void;
    name?: string;
    required?: boolean;
    disabled?: boolean;
    helperText?: string /** Texto de ayuda o error debajo del input */;
    min?: string /** Fecha mínima permitida (YYYY-MM-DD) */;
    max?: string /** Fecha máxima permitida (YYYY-MM-DD) */;
}

export const DateInput: React.FC<DateInputProps> = ({ label = 'Fecha de nacimiento', id, name, value, onChange, required = false, helperText, disabled = false, min, max }) => {
    return (
        <div className="flex flex-col w-full gap-1">
            <label className="text-sm font-medium text-gray-700">{label}</label>

            <div className="relative w-full">
                {/* Icono calendario */}
                {/* <CalendarDaysIcon className="absolute left-2 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400 pointer-events-none" /> */}
                <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 z-10 pointer-events-none">📅</span>

                <ReactDatePicker
                    id={id}
                    name={name}
                    selected={value ? new Date(value) : null}
                    onChange={(date) => handleDateChange(date, onChange)}
                    dateFormat="yyyy-MM-dd"
                    placeholderText="1985-06-10"
                    minDate={min ? new Date(min) : undefined}
                    maxDate={max ? new Date(max) : new Date()} // no fechas futuras si no se pasa max
                    required={required}
                    disabled={disabled}
                    wrapperClassName="w-full"
                    className={`w-full border border-gray-300 rounded-sm pl-10 py-1 text-sm text-gray-900focus:outline-none focus:border-black focus:border-[1px] ${
                        disabled ? 'bg-gray-100 cursor-not-allowed' : 'bg-white'
                    } transition-colors duration-200 ease-in-out`}
                />
            </div>

            {helperText && <p className="text-xs text-gray-500 mt-1">{helperText}</p>}
        </div>
    );
};
