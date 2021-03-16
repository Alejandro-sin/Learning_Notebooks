/* 



*/


// Ejecuto codigo despues de un tiempo

const  util = require('util')

// Con  promisify le paso la función sin invocar como parámetro y me duelueve la funció en modo promesa
const sleep = util.promisify(setTimeout);



module.exports ={

    async taskOne(){
        try{
// Me sirve para crear y lanzar errores

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

