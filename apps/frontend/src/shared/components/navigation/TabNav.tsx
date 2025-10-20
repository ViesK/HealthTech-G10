import React from 'react';

export interface TabItem {
    id: string;
    label: string;
    icon: React.ReactNode;
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
        <nav className="w-full bg-white border-t border-gray-200">
            <div className="flex items-center justify-around">
                {tabs.map((tab) => {
                    const isActive = tab.id === activeTabId;

                    return (
                        <button
                            key={tab.id}
                            onClick={() => handleTabClick(tab)}
                            className={`flex flex-col items-center justify-center py-3 px-4 flex-1 relative transition-colors duration-200 ${
                                isActive ? 'text-blue-600' : 'text-gray-500 hover:text-gray-700'
                            }`}
                            aria-current={isActive ? 'page' : undefined}
                        >
                            {/* Icon */}
                            <div className="mb-1">{tab.icon}</div>

                            {/* Label */}
                            <span className="text-xs font-medium">{tab.label}</span>

                            {/* Active indicator */}
                            {isActive && (
                                <div className="absolute bottom-0 left-0 right-0 h-1 bg-blue-600 rounded-t-full" />
                            )}
                        </button>
                    );
                })}
            </div>
        </nav>
    );
};
