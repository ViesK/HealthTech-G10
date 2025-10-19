export const handleDateChange = (date: Date | null, onChange?: (dateString: string) => void) => {
    if (!date) return;
    const formatted = date.toISOString().split('T')[0]; // YYYY-MM-DD
    onChange?.(formatted);
};
