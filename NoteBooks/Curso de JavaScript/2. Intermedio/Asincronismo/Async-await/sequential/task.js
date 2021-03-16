/* 

Con un modulo de node llamado utils puedo optimizar el uso de callbacks en funciones  asincorns
utils provee un m{etodo llamado promisify que permite convertir funciones 
que usan callbacks a una que usen promesas o async await.




*/


// Ejecuto codigo despues de un tiempo

const  util = require('util')

// Con  promisify le paso la función sin invocar como parámetro y me duelueve la funció en modo promesa
const sleep = util.promisify(setTimeout);



module.exports ={

    async taskOne(){
        try{
// Me sirve para crear y lanzar errores
        throw new Error('SOME THING'); 
        await sleep(4000);
        return "One value"
    } catch(e){
        console.log(e);
    }


    },

    async taskTwo(){
        await sleep(2000);
        return "Two value"
    }
};

