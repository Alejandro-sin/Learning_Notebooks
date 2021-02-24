"use strict";
// Funció para mostrar fotografía.
// Definir enumerado
var PhotoOrientation;
(function (PhotoOrientation) {
    PhotoOrientation[PhotoOrientation["Landscape"] = 0] = "Landscape";
    PhotoOrientation[PhotoOrientation["Portrait"] = 1] = "Portrait";
    PhotoOrientation[PhotoOrientation["Square"] = 2] = "Square";
    PhotoOrientation[PhotoOrientation["Panorama"] = 3] = "Panorama";
})(PhotoOrientation || (PhotoOrientation = {}));
// Recibe un objeto con la configuracion necesaria
/* function showPicture(picture:{title : string, date: string, orientation:PhotoOrientation}){
    console.log(`[title:${picture.title}, date:${picture.date}, orientation:${picture.orientation}]`)
}
Esta función puede usar la interface para que se amás legible.

*/
function showPicture(picture) {
    console.log("[title:" + picture.title + ", date:" + picture.date + ", orientation:" + picture.orientation + "]");
}
var myPic = {
    title: "Titulazo",
    date: "2020-30-11",
    orientation: PhotoOrientation.Landscape
};
showPicture(myPic);
showPicture({
    title: 'Test title',
    date: '23030-233',
    orientation: 1
});
function generatePicture(config) {
    var pic = { title: 'Default', date: '2020' };
    if (config.title) {
        pic.title = config.title;
    }
    if (config.date) {
        pic.date = config.date;
    }
    return pic;
}
var picture = generatePicture({});
console.log('picture', picture);
//Me trae el objeto con los datos ingresados, demeustra que es opcional y sobre escribe el valor por defecto.
picture = generatePicture({ title: 'Travel' });
console.log('picture', picture);
// Creamso una interfaz para gestionar un usario
/*
interface User {
    id: number;
    username: string;
    isPro: boolean;
}

 */
//Creamos un tipo
var user;
user = { id: 10, username: "Alejandro", isPro: true };
console.log('user', user);
