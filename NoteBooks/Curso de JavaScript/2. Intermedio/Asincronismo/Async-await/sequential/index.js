// Importo las tareas desde task.js


/* 

Código seceuncial
 Cada tarea de la función toma n cantidad de tiempo en hacerse, pero son dependientes del paso anteiro
 Lo correcto sería encpasular la tarea en un código try cathc

*/

const {taskOne, taskTwo} = require('./task');

async function main(){
    try {
        console.time("Medida")
    // Despues de importaarse debe usarse el await porque son asincornos.
        const valueOne = await taskOne();
        const valueTwo = await taskTwo();
        console.timeEnd("Medida")
        console.log(valueOne)
        console.log(valueTwo)
    } catch(error) {
        console.log(error);
    }

// Para medir cuanto dura el tiempo usamos console.tim
}


main();
