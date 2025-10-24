import { Stethoscope, ClipboardList, FlaskConical } from "lucide-react";

export const SeleccionarReserva = () => {
  const opciones = [
    {
      id: "consulta",
      titulo: "Consulta médica",
      icono: <Stethoscope size={32} strokeWidth={1.8} className="text-rose-400" />,
    },
    {
      id: "estudios",
      titulo: "Estudios",
      icono: <ClipboardList size={32} strokeWidth={1.8} className="text-rose-400" />,
    },
    {
      id: "laboratorio",
      titulo: "Laboratorio",
      icono: <FlaskConical size={32} strokeWidth={1.8} className="text-rose-400" />,
    },
  ];

  return (
    <section className="bg-gray-50 p-4 rounded-xl">
      <h2 className="text-lg font-semibold mb-4">Reserve su cita</h2>

      <div className="grid grid-cols-3 gap-3">
        {opciones.map((op) => (
          <button
            key={op.id}
            className="
              flex flex-col items-center justify-center
              gap-2 p-4 rounded-2xl
              bg-white shadow-sm hover:shadow-md
              transition-all duration-200
            "
          >
            {op.icono}
            <span className="text-sm font-medium text-gray-700 text-center">
              {op.titulo}
            </span>
          </button>
        ))}
      </div>
    </section>
  );
};
