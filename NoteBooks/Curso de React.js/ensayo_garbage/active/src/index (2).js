import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
//import reportWebVitals from './reportWebVitals';

/*  Importar los elementos creados desde loc componentes */
import Chapter_one from './components/Chapter_one';

/* Creo un contenedor para el Document asociado mediante su id general. */
const container = document.getElementById('app');
/*  Esta función recibo como primer <element />*/

ReactDOM.render(<Chapter_one/>, container);

//reportWebVitals();