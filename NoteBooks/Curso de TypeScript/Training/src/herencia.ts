/* 

asbtract: cuando requeires que una clase no sea instanciada
protected: atributo de los miembros para que puedan ser accedidos desde su propia clase y también que puedan ser solo accedidos a quienes heredan esa clase con implements(herencia)
implements: herencia claseA extends claseB { … }
static: para poder acceder a métodos/propiedades de una clase sin la necesidad de la instancia(new ClaseA()) sino const a = ClaseA.propiedad*/

export{}


enum PhotoOrientation{
    Landscape,
    Portrait,
    Square,
    Panorama
}


/// Herencia



// Usamos extends para dar herencia:
/* 

Si las variables que herada son privadas  maracrá un erro por que no peude acceder a variables privadas d eun ambito
local diferente al de la clase, para ello usamos un intermedio entre público y privado llamado protected

*/

/* class Picture extends Item{
    public static phothiOrientation = PhotoOrientation
    public constructor(id: number, title:string){
        // Invoca el constructor de la clase Item.
        super(id, title)

    }
} */