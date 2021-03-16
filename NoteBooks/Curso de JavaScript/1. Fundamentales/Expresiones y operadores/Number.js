/* 

Como parte de las buenas practicas muchas veces tenemos un string que es enviado mediante prompt.
Es bueno validar por principios de programaicón defensiva el qué e smi variable.

*/


var foo = "55A"
var miNumber = Number(foo) // Retorna False

if (isNaN(miNumber)){
    console.log("No es un número")
}

// Al usar el doble negativo estoy diciendo que si es un número.
/* if (!isNaN(miNumber)) */
 