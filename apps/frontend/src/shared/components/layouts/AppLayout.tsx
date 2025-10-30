import { type ReactNode, type ReactElement, useState } from 'react';
import Header from '../headers/Header';
import { TabNav, type TabItem } from '../navigation';
import { HomeIcon, Calendar, HeartPulse, ClipboardList } from 'lucide-react';

interface LayoutProps {
  title: string;
  onBack?: () => void;
  children: ReactElement | ReactNode;
}

const tabs: TabItem[] = [
  {
    id: 'home',
    label: 'Inicio',
    icon: <HomeIcon size={22} strokeWidth={2} className="text-black" />,
  },
  {
    id: 'reservar',
    label: 'Reservar',
    icon: <Calendar size={22} strokeWidth={2} className="text-black" />,
  },
  {
    id: 'resultados',
    label: 'Resultados',
    icon: <HeartPulse size={22} strokeWidth={2} className="text-black" />,
  },
  {
    id: 'historial',
    label: 'Historial',
    icon: <ClipboardList size={22} strokeWidth={2} className="text-black" />,
  },
];

const AppLayout = ({ title, onBack, children }: LayoutProps) => {
  const [activeTab, setActiveTab] = useState('home'); 
  return (
    <div className="min-h-screen flex flex-col items-center bg-gray-50">
      <div className="w-full max-w-sm px-4 pb-20">
        <Header title={title} onBack={onBack} />
        <main className="flex-1 mt-4 space-y-4 transition-all duration-300">
          {children}
        </main>
      </div>

      {/* Navbar */}
      <TabNav tabs={tabs} activeTabId={activeTab} onTabChange={setActiveTab} />
    </div>
  );
};

export default AppLayout;