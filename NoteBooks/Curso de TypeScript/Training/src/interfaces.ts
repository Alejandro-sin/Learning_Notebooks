// Funció para mostrar fotografía.


// Definir enumerado
 enum PhotoOrientation{
     Landscape,
     Portrait,
     Square,
     Panorama
 }

interface Picture {
    // Las propiedades cosnideradas son as que están en la función
    title: string;
    date: string;
    orientation: PhotoOrientation

}

// Recibe un objeto con la configuracion necesaria
/* function showPicture(picture:{title : string, date: string, orientation:PhotoOrientation}){
    console.log(`[title:${picture.title}, date:${picture.date}, orientation:${picture.orientation}]`)
}
Esta función puede usar la interface para que se amás legible. 

*/

function showPicture(picture: Picture){
    console.log(`[title:${picture.title}, date:${picture.date}, orientation:${picture.orientation}]`)
}





let myPic = {
    title: "Titulazo",
    date: "2020-30-11",
    orientation: PhotoOrientation.Landscape
}

showPicture(myPic)




showPicture({
    title: 'Test title',
    date: '23030-233',
    orientation:1
})


// COmo usar las interfaces para mejorar contrato?

/*
Los contratos peuden estar dados pro objetos, en este caso el que proviene del argumento de ShowPicture.
podemos usar este para definir la interface


Debido a estos contratos no puedo añdadir propiedades que no existen en el contrato/ interfaz, ya qu ela interfaz permtie definir las propeidades
permitirá tamién definri propiedades opciones.

*/

interface PictureConf {
    title?: string;
    date?: string;
    orientation?: PhotoOrientation
}

function generatePicture(config: PictureConf){
    const pic = {title: 'Default', date: '2020'};
    if(config.title){
        pic.title = config.title;
    }
    if (config.date){
        pic.date = config.date;
    }
    return pic;
}

let picture = generatePicture({});
console.log('picture', picture)
//Me trae el objeto con los datos ingresados, demeustra que es opcional y sobre escribe el valor por defecto.
picture = generatePicture({title:'Travel'})
console.log('picture', picture)


// Creamso una interfaz para gestionar un usario
/* 
interface User {
    id: number;
    username: string;
    isPro: boolean;
}

 */
//Creamos un tipo

let user: User;
user = {id: 10, username: "Alejandro", isPro: true}
console.log('user', user)
/* 
El objeto puede mutar, o cambiar sus atributos. Sin embargo hay operaciones que no se deberían permitir,
como cambiar el id de una base de datos , esto afectaría la persistencia de lso datos.

user.id = 20 Me permitiría reemplazarlo sin problemas... para evitar esto en TS usaremos readonly.
*/
interface User {
    readonly id: number;
    username: string;
    isPro: boolean;
}
