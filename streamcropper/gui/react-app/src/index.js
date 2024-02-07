import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import StubInteractor from "./interactor/stub/stub_interactor";
import RemoteInteractor from "./interactor/remote/remote_interactor";
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import IndexPage from "./page/IndexPage";
import StreamPage from "./page/StreamPage";
import ErrorPage from "./page/ErrorPage";

global.interactor = new StubInteractor()

if (process.env.REACT_APP_ENV === 'dev') {
    global.interactor = new StubInteractor()
    global.title = 'Global DEV Title'
}

if (process.env.REACT_APP_ENV === 'prod') {
    global.interactor = new RemoteInteractor()
    global.title = 'Global PROD Title'
}

const router = createBrowserRouter([
    {
        path: "/",
        element: <IndexPage/>,
    },
    {
        path: "stream/:streamId",
        element: <StreamPage/>,
    },
    {
        path: "error",
        element: <ErrorPage/>,
    },
]);


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
