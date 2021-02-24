"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// Definir enumerado
var PhotoOrientation;
(function (PhotoOrientation) {
    PhotoOrientation[PhotoOrientation["Landscape"] = 0] = "Landscape";
    PhotoOrientation[PhotoOrientation["Portrait"] = 1] = "Portrait";
    PhotoOrientation[PhotoOrientation["Square"] = 2] = "Square";
    PhotoOrientation[PhotoOrientation["Panorama"] = 3] = "Panorama";
})(PhotoOrientation || (PhotoOrientation = {}));
// Probamos la herencia:
var album = {
    id: 1,
    title: "Anymadversion",
    description: "This is an album and sin heredad la descripción."
};
var picture = {
    id: 2,
    title: "Anymad",
    orientation: PhotoOrientation.Portrait
};
var newPicture = {};
newPicture.id = 30;
// Podemos cambiar los estados, esto significa que puedo reasingar las propiedades de estos objetos.
console.log('album', album);
console.log('picture', picture);
console.log('picture', newPicture);
