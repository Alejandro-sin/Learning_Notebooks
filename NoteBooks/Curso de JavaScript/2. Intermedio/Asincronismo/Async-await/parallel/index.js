/*  Aqui usamso un arreglo para decirle todas las tareas que necesito qe ejecute 

De forma paralela el tiempo que tarda disminuye drásticamente porque hace dos tareas 
en tiempo distintas

*/

const {taskOne, taskTwo} = require('./task');

async function main(){
    try {
        console.time("Medida");
        
        // Le doy un
        const results = await Promise.all([taskOne(), taskTwo()])

    // Despues de importaarse debe usarse el await porque son asincornos.
        const valueOne = await taskOne();
        const valueTwo = await taskTwo();

        console.timeEnd("Medida");
        console.log(results[0]);
        console.log(results[1]);

    } catch(error) {
        console.log(error);
    }

// Para medir cuanto dura el tiempo usamos console.tim
}


main();
