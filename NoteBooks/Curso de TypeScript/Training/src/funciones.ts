//

/* 

Las funciones en TS

*  Los parámetros en las funcioens son tipados
* Se pueden definir parámetros opcionales
* EL tipo de retorno puede ser un tipo básico, enum, alias, tipo literal o una combinación de llos.



NOTA:  un parámetro opcional siempre debe ir al final en dado caso que existan otros parámetros obligatorios.

las funioes puede retornoar un primitivo o combinaciones de ellos.
*/


// Queremos una fnción para crear una fotografía// JS
/* function createPictureJS(title, data, size){ 
//
}

 */
type SquareSize = '100x100'|'500x500'
// Queremos una fnción para crear una fotografía// TS
function createPicture(title: String, data: String, size: SquareSize){ 
    //Se crea foto ...
    // TS mejora la legibilidad del código y lo hace robusto-
    console.log('create pic', title, data, size)
}

createPicture('The_love_of_my_life','2021-20-12','100x100');


// En TS usamos parámetros opcionales en funciones, permiten el paso de diferentes valores
// la notación es mediante el simbolo de interrogacióm

type SquareSizes = '100x100'|'500x500'
// Queremos una fnción para crear una fotografía// TS
function createPictures(title: String, date?: String, size?: SquareSizes){ 
    //Se crea foto ...
    // TS mejora la legibilidad del código y lo hace robusto-
    console.log('create pic', title, date, size)
}

createPicture('The_love_of_my_life','2021-20-12','100x100');


// FLAT ARRAY FUNCTIONS


// Estamos creando un objetipo JSON literal

let createPictureFlatArray = (title: string, date: string, size:SquareSize): object =>{
    return {
        //#AtributosObjeto: Estado de las variables ya signa valor.
        title: title,
        date: date,
        size: size
    }
    //ES6
    /* return {
        title,date, size
    } */
};


const picturesFLAT = createPictureFlatArray('Foto', '2000-12-1', '100x100')
console.log('picture: ', picturesFLAT)


// Tipo de retorno con TS
/* 
Las funcioens puedne devovler cosas predeterminadas

*/


function handleError(code: number, message: string): never | string{
    // Procesameinto del código...lógica para definri de qué manera se ejccuta la función
    if (message === 'error'){
        throw new Error(`${message}. Code error: ${code}`);
    } else{
        return 'An error has occured';
    }
}


// Capturo el error independientemente de si tengo un string o si tengo un never.
try {
    // Verificar la combianción de tipos
    let result = handleError(200, 'ok')
    console.log('result: ', result) // Retorna a string

    // Miros como se comporta al invocar la misma función al enviar un código de error.
    result = handleError(404,'error')
    console.log('result: ', result) // Retorna un NEVER, nunca retorna un valor vñalida.

} catch (error) {
}
