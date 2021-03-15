
/* 


Crearemos un Hoisting para ver como se comporta.

 */

//var hoisting = undefined -> Js creará una  variable hoisting y le asignará el valor undefined primitivo.

console.log(hoisting)// Se espera que retorne Undefined
wht();

var hoisting = "Esta variable está por fuera"

function wht(){
    console.log("Las funciones se almacenan en memoria en el contexto de ejecución")
}



console.log(initialized);
initialized ="Error de referencia"