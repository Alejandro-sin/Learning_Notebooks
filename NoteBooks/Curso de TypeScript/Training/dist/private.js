"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var PhotoOrientation;
(function (PhotoOrientation) {
    PhotoOrientation[PhotoOrientation["Landscape"] = 0] = "Landscape";
    PhotoOrientation[PhotoOrientation["Portrait"] = 1] = "Portrait";
    PhotoOrientation[PhotoOrientation["Square"] = 2] = "Square";
    PhotoOrientation[PhotoOrientation["Panorama"] = 3] = "Panorama";
})(PhotoOrientation || (PhotoOrientation = {}));
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
/*
Podemos usar la notación de #atributo para vovler este atributo privado.

private id: number;

    #title: string;
    #orientation: PhotoOrientation;
    ----
            this.#id = id;
            this.#title = title ;
            this.#orientation = orientation;

            provate permtie acceder a conocer el estado interno del objeto
            la nueva sintaxis de # no lo permite.
*/ 
