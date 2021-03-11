/* 

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment

Este chunk tiene como propósito explicar  la desestrcutraicón en JS

Puedo empaquetar y desempaquetar sin problemas
*/



let a,b, rest;

[a,b,...rest] = [1,2,3,4,5,5,6]
console.log(a,b,rest)


// Puedo hacerlo con toda una expresión
let a, b, rest
({a,b,...rest} = {a:10, b:20,c:30, d:40})
console.log(a)
console.log(rest)


// Asignación de variables
/* 
Puedo empaaquetar valores de un arreglo en un arreglo de variables. Así:

*/
const foo =["one","two","three"]
const [verde,azul,blue]  = foo

console.log(verde)


/* 

Valores Default

Puedo crear valores default pra las variables

*/

let a,b ;

[a =5, b=3] = [1]
// Me dará 1 y 3
console.log(a,b)


