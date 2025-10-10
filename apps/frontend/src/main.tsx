import React from 'react';
import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
// import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './shared/styles/global.css';
import Register from './features/auth/pages/Register/Register';
import { store } from './app/store/store';
// import Home from './features/home/pages/Home';

// const router = createBrowserRouter([{ path: '/', element: <Home /> }]);

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <Provider store={store}>
            {/* <RouterProvider router={router} /> */}
            <Register />
        </Provider>
    </React.StrictMode>
);
