"use strict";
// Get y Set
Object.defineProperty(exports, "__esModule", { value: true });
var PhotoOrientation;
(function (PhotoOrientation) {
    PhotoOrientation[PhotoOrientation["Landscape"] = 0] = "Landscape";
    PhotoOrientation[PhotoOrientation["Portrait"] = 1] = "Portrait";
    PhotoOrientation[PhotoOrientation["Square"] = 2] = "Square";
    PhotoOrientation[PhotoOrientation["Panorama"] = 3] = "Panorama";
})(PhotoOrientation || (PhotoOrientation = {}));
/*



*/
var Picture = /** @class */ (function () {
    // Al definir una clase necesitamos un constructor para poder crear objetos a partir de la abstración
    function Picture(id, title, orientation) {
        this._id = id;
        this._title = title;
        this._orientation = orientation;
    }
    Object.defineProperty(Picture.prototype, "id", {
        // Añadimos un get para identificar el estdo
        get: function () {
            return this._id;
        },
        // Metodo accesor, cambia el estado dle identificador.
        set: function (id) {
            this._id = id;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Picture.prototype, "title", {
        get: function () {
            return this._title;
        },
        set: function (title) {
            //return this._title;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Picture.prototype, "orientation", {
        get: function () {
            return this._orientation;
        },
        enumerable: false,
        configurable: true
    });
    /*   set orientation(orientation: PhotoOrientation){
          return this._orientation = orientation;
      } */
    // Comportamiento está dado por otras funciones, 
    Picture.prototype.toString = function () {
        return "[id: " + this.id + "\n                title: " + this.title + "\n                orientation: " + this.orientation + "]";
    };
    ;
    return Picture;
}());
;
var Album = /** @class */ (function () {
    function Album(id, title) {
        this.id = id;
        this.title = title;
        this.pictures = [];
    }
    Album.prototype.addPicture = function (picture) {
        this.pictures.push(picture);
    };
    return Album;
}());
