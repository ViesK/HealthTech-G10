import { type ReactNode, type ReactElement } from 'react';
import Header from '../headers/Header';

interface LayoutProps {
    title: string;
    onBack?: () => void;
    children: ReactElement | ReactNode;
}

const Layout = ({ title, onBack, children }: LayoutProps) => {
    return (
        <div className="min-h-screen flex flex-col items-center">
            <Header title={title} onBack={onBack} />

            <main className="flex-1 p-6">{children}</main>

            {/* Navbar (la agregaremos luego) */}
        </div>
    );
};

export default Layout;
