/*  

Expresión regular para un email


*/


// Estas dos líneas son lo mismo, diferentes notaciones para hablar de regex
var expresion_r = /hola/;
var expresion_r = new RegExp("hola");


// Usando el método test probamos si la cadena existe como patron de regex

var frase  = "Quiero verificar que hola se encuentre aquí"
if (expresion_r.test(frase)) {
    console.log("Si aqui está")
}

/* 
cIRCUNFLEJO eN EL PRINCIPIO
HOLA$ aL FINFAL
ho+a Una o mas veces
ho*a cero o mas veces

ho?a cero o una

hola|otra una u otra
ho.a Cualquier caracter

\wola algfanumerico

*/
