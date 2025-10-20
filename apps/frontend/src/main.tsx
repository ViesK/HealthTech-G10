import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
import './shared/styles/global.css';
import { store } from './app/store/store';
import Login from './features/auth/pages/Login/Login';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <Provider store={store}>
    {/* 👇 Mostramos solo el login, sin router */}
    <Login/>
  </Provider>
);