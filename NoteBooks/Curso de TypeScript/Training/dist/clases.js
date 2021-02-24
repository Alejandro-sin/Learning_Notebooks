"use strict";
//CLASES
Object.defineProperty(exports, "__esModule", { value: true });
// Definir enumerado
var PhotoOrientation;
(function (PhotoOrientation) {
    PhotoOrientation[PhotoOrientation["Landscape"] = 0] = "Landscape";
    PhotoOrientation[PhotoOrientation["Portrait"] = 1] = "Portrait";
    PhotoOrientation[PhotoOrientation["Square"] = 2] = "Square";
    PhotoOrientation[PhotoOrientation["Panorama"] = 3] = "Panorama";
})(PhotoOrientation || (PhotoOrientation = {}));
/*  Para definri clases usamos el keyword class */
var Picture = /** @class */ (function () {
    // Al definir una clase necesitamos un constructor para poder crear objetos a partir de la abstración
    function Picture(id, title, orientation) {
        this.id = id;
        this.title = title;
        this.orientation = orientation;
    }
    // Comportamiento está dado por otras funciones, 
    Picture.prototype.toString = function () {
        return "[id: " + this.id + "\n            title: " + this.title + "\n            orientation: " + this.orientation + "]";
    };
    ;
    return Picture;
}());
;
// Impmenetamos la clase album
var Album = /** @class */ (function () {
    function Album(id, title) {
        this.pictures = [];
        this.id = id;
        this.title = title;
        this.pictures = [];
    }
    Album.prototype.addPicture = function (picture) {
        this.pictures.push(picture);
    };
    return Album;
}());
// De esta forma creamos la relación entre album y objetos de tipo picture.
var album = new Album(2, 'Personal pictures');
var picture = new Picture(1, 'TypeScript', PhotoOrientation.Square);
album.addPicture(picture);
console.log('album', album);
// ACCEDIENDO A LOS MIEMBROS PUBLICOS
picture.id = 100; // El acceso es public, nada impide en cambiar lso estados
picture.title = 'Another Title';
// El archivo modificado
console.log('album', album);
// Para hacerlo de manera explícita se usa la palabra reservada public antes de las funciones, vraibles
/*
¿Qué tan conveniente es tener todos los miembros publicos?
No todo se puede cambiar, id...

TS declara de mnera porpia mediante private miembros privados.

*/
