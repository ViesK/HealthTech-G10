import { useEffect, useState } from 'react';
import { api } from '../../../lib/api';

export default function Home() {
    const [msg, setMsg] = useState('...');
    useEffect(() => {
        api<{ message: string }>('/health')
            .then((d) => setMsg(d.message))
            .catch(() => setMsg('API off'));
    }, []);
    return <div className="p-6">Estado API: {msg}</div>;
}
