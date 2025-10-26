import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
// import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './shared/styles/global.css';
// import Register from './features/auth/pages/Register/Register';
import { store } from './app/store/store';
//import BookAppointment from './features/appointments/pages/BookAppointment';
import { BrowserRouter } from 'react-router-dom';
// import Home from './features/home/pages/Home';
// import Login from './features/auth/pages/Login/Login';
//import HomePaciente from './features/patients/HomePaciente';
import HistoryPage from './features/history/pages/HistoryPage';

// const router = createBrowserRouter([{ path: '/', element: <Home /> }]);

ReactDOM.createRoot(document.getElementById('root')!).render(
    <Provider store={store}>
        {/* <RouterProvider router={router} /> */}
        <BrowserRouter>

            <HistoryPage/>
        </BrowserRouter>
    </Provider>
);