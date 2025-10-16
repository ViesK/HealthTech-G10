import { type ReactNode, type ReactElement } from 'react';
import Header from '../headers/Header';

interface LayoutProps {
    title: string;
    onBack?: () => void;
    children: ReactElement | ReactNode;
}

const AppLayout = ({ title, onBack, children }: LayoutProps) => {
    return (
        <div className="min-h-screen flex flex-col items-center">
            <Header title={title} onBack={onBack} />

            <main className="min-h-screen flex flex-col items-center">{children}</main>

            {/* Navbar (la agregaremos luego) */}
        </div>
    );
};

export default AppLayout;
