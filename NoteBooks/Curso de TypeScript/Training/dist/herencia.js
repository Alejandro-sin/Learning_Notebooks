"use strict";
/*

asbtract: cuando requeires que una clase no sea instanciada
protected: atributo de los miembros para que puedan ser accedidos desde su propia clase y también que puedan ser solo accedidos a quienes heredan esa clase con implements(herencia)
implements: herencia claseA extends claseB { … }
static: para poder acceder a métodos/propiedades de una clase sin la necesidad de la instancia(new ClaseA()) sino const a = ClaseA.propiedad*/
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var PhotoOrientation;
(function (PhotoOrientation) {
    PhotoOrientation[PhotoOrientation["Landscape"] = 0] = "Landscape";
    PhotoOrientation[PhotoOrientation["Portrait"] = 1] = "Portrait";
    PhotoOrientation[PhotoOrientation["Square"] = 2] = "Square";
    PhotoOrientation[PhotoOrientation["Panorama"] = 3] = "Panorama";
})(PhotoOrientation || (PhotoOrientation = {}));
/// Herencia
// Supler clase 
var Item = /** @class */ (function () {
    function Item(id, title) {
        this.id = id;
        this.title = title;
    }
    return Item;
}());
// Usamos extends para dar herencia:
/*

Si las variables que herada son privadas  maracrá un erro por que no peude acceder a variables privadas d eun ambito
local diferente al de la clase, para ello usamos un intermedio entre público y privado llamado protected

*/
var Picture = /** @class */ (function (_super) {
    __extends(Picture, _super);
    function Picture(id, title) {
        // Invoca el constructor de la clase Item.
        return _super.call(this, id, title) || this;
    }
    return Picture;
}(Item));
