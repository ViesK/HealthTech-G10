import { type ReactNode, type ReactElement, useState } from 'react';
import Header from '../headers/Header';
import { TabNav, type TabItem } from '../navigation';

interface LayoutProps {
    title: string;
    onBack?: () => void;
    children: ReactElement | ReactNode;
}

const tabs: TabItem[] = [
    {
        id: 'inicio',
        label: 'Inicio',
        icon: '🏠',
    },
    {
        id: 'reservar',
        label: 'Reservar',
        icon: '🗓️',
    },
    {
        id: 'resultados',
        label: 'Resultados',
        icon: '📊',
    },
    {
        id: 'indicaciones',
        label: 'Indicaciones',
        icon: '📝',
    },
];

const AppLayout = ({ title, onBack, children }: LayoutProps) => {
    const [activeTab, setActiveTab] = useState('inicio');

    return (
        <div className="min-h-screen flex flex-col items-center">
            <div className="w-full max-w-sm px-4">
                <Header title={title} onBack={onBack} />

                <main className="flex-1 mt-4">{children}</main>
            </div>

            {/* Navbar (la agregaremos luego) */}
            <TabNav tabs={tabs} activeTabId={activeTab} onTabChange={setActiveTab} />
        </div>
    );
};

export default AppLayout;
