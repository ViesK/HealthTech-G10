import { Bell, MessageCircle } from "lucide-react";

type HeaderUsuarioProps = {
  nombre: string;
  avatar?: string;
};

export const HeaderUsuario = ({ nombre, avatar }: HeaderUsuarioProps) => {
  return (
    <header className="flex items-center justify-between p-4 bg-white shadow">
      
      <div className="flex items-center gap-3">
        <img
          src={
            avatar ||
            "https://images.unsplash.com/photo-1607746882042-944635dfe10e?auto=format&fit=crop&w=150&q=80"
          }
          alt={nombre}
          className="w-12 h-12 rounded-full border object-cover"
        />
        <div>
          <p className=" font-semibold text-sm">Hola,</p>
          <p className="text-gray-500 text-lg">{nombre}</p>
        </div>
      </div>

     
      <div className="flex items-center gap-3">
        <button className="p-2 hover:bg-gray-100 rounded-full transition">
          <Bell size={20} strokeWidth={2} className="text-gray-600" />
        </button>
        <button className="p-2 hover:bg-gray-100 rounded-full transition">
          <MessageCircle size={20} strokeWidth={2} className="text-gray-600" />
        </button>
      </div>
    </header>
  );
};