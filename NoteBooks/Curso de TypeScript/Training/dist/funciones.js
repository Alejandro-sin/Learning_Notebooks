"use strict";
//
// Queremos una fnción para crear una fotografía// TS
function createPicture(title, data, size) {
    //Se crea foto ...
    // TS mejora la legibilidad del código y lo hace robusto-
    console.log('create pic', title, data, size);
}
createPicture('The_love_of_my_life', '2021-20-12', '100x100');
// Queremos una fnción para crear una fotografía// TS
function createPictures(title, date, size) {
    //Se crea foto ...
    // TS mejora la legibilidad del código y lo hace robusto-
    console.log('create pic', title, date, size);
}
createPicture('The_love_of_my_life', '2021-20-12', '100x100');
// FLAT ARRAY FUNCTIONS
// Estamos creando un objetipo JSON literal
var createPictureFlatArray = function (title, date, size) {
    return {
        //#AtributosObjeto: Estado de las variables ya signa valor.
        title: title,
        date: date,
        size: size
    };
    //ES6
    /* return {
        title,date, size
    } */
};
var picturesFLAT = createPictureFlatArray('Foto', '2000-12-1', '100x100');
console.log('picture: ', picturesFLAT);
// Tipo de retorno con TS
/*
Las funcioens puedne devovler cosas predeterminadas

*/
function handleError(code, message) {
    // Procesameinto del código...lógica para definri de qué manera se ejccuta la función
    if (message === 'error') {
        throw new Error(message + ". Code error: " + code);
    }
    else {
        return 'An error has occured';
    }
}
// Capturo el error independientemente de si tengo un string o si tengo un never.
try {
    // Verificar la combianción de tipos
    var result = handleError(200, 'ok');
    console.log('result: ', result); // Retorna a string
    // Miros como se comporta al invocar la misma función al enviar un código de error.
    result = handleError(404, 'error');
    console.log('result: ', result); // Retorna un NEVER, nunca retorna un valor vñalida.
}
catch (error) {
}
