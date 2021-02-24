export{};

enum PhotoOrientation{
    Landscape,
    Portrait,
    Square,
    Panorama
}

class Picture {

    // Propiedades
    private id: number;
    private title: string;
    private orientation: PhotoOrientation;
    
    // Al definir una clase necesitamos un constructor para poder crear objetos a partir de la abstración
    constructor(id: number, 
                title: string, 
                orientation: PhotoOrientation){
            this.id = id;
            this.title = title ;
            this.orientation = orientation;
    }

// Comportamiento está dado por otras funciones, 

public toString() {
    return `[id: ${this.id}
            title: ${this.title}
            orientation: ${this.orientation}]`;
    };
};

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