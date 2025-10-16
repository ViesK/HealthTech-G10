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
            <div className="w-full max-w-sm px-4">
                <Header title={title} onBack={onBack} />

                <main className="flex-1 mt-4">{children}</main>
            </div>

            {/* Navbar (la agregaremos luego) */}
        </div>
    );
};

export default AppLayout;
