import React from 'react';

export interface TabItem {
    id: string;
    label: string;
    icon?: React.ReactNode | string;
    onClick?: () => void;
}

interface TabNavProps {
    tabs: TabItem[];
    activeTabId: string;
    onTabChange?: (tabId: string) => void;
}

export const TabNav: React.FC<TabNavProps> = ({ tabs, activeTabId, onTabChange }) => {
    const handleTabClick = (tab: TabItem) => {
        if (tab.onClick) {
            tab.onClick();
        }

        if (onTabChange) {
            onTabChange(tab.id);
        }
    };

    return (
        <nav className="fixed bottom-0 left-1/2 -translate-x-1/2 w-full max-w-sm bg-white shadow-[0_-2px_10px_rgba(0,0,0,0.1)] z-50">
            <div className="flex items-center justify-around px-4">
                {tabs.map((tab) => {
                    const isActive = tab.id === activeTabId;

                    return (
                        <button
                            key={tab.id}
                            onClick={() => handleTabClick(tab)}
                            className={`flex flex-col items-center justify-center py-2 px-2 flex-1 relative transition-colors duration-200 min-w-0 ${
                                isActive ? 'text-blue-600' : 'text-gray-500 hover:text-gray-700'
                            }`}
                            aria-current={isActive ? 'page' : undefined}>
                            {/* Icon */}
                            <div className="mb-0.5 text-lg">{tab.icon}</div>

                            {/* Label */}
                            <span className="text-[10px] font-medium leading-tight truncate max-w-full">{tab.label}</span>
                        </button>
                    );
                })}
            </div>
        </nav>
    );
};
