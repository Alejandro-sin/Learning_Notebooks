

/*  Hay que garantizar que si importamos*/

import  router from './routes';


/*  Uso window un valro que esta disponible, permite saber si está en el cotnexto de la palicación
y escucho. si los elemnetos están listos y cargados.

Estoy trayendo toda la lógica de routes.


*/

window.addEventListener('load', router);

/* Genero un event Listeenr que escuche las rutas, el hash al que me estoy movineindo. 
Cuando cambie un hash le pasamos una función de rutas

*/

window.addEventListener('hashchange', router);