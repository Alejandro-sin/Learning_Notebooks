//CLASES



// Sirve para no causar conflicto por llamar a mi enum en otro archivo.
export {};

// Definir enumerado
enum PhotoOrientation{
    Landscape,
    Portrait,
    Square,
    Panorama
}


/*  Para definri clases usamos el keyword class */

class Picture {
    // Propiedades
    id: number;
    title: string;
    orientation: PhotoOrientation;
    
    // Al definir una clase necesitamos un constructor para poder crear objetos a partir de la abstración
    constructor(id: number, 
                title: string, 
                orientation: PhotoOrientation){
            this.id = id;
            this.title = title ;
            this.orientation = orientation;
    }

// Comportamiento está dado por otras funciones, 

toString() {
    return `[id: ${this.id}
            title: ${this.title}
            orientation: ${this.orientation}]`;
    };
};

// Impmenetamos la clase album


class Album{
    id: number;
    title: string;
    pictures: Picture[] = [];

    constructor(id: number, title: string){
        this.id = id;
        this.title = title
        this.pictures =[]
    }
    addPicture(picture: Picture){
        this.pictures.push(picture)
    }
}

// De esta forma creamos la relación entre album y objetos de tipo picture.
const album: Album = new Album(2,'Personal pictures', );
const picture: Picture = new Picture(1, 'TypeScript', PhotoOrientation.Square)
album.addPicture(picture)

console.log('album', album)



// ACCEDIENDO A LOS MIEMBROS PUBLICOS
picture.id =100; // El acceso es public, nada impide en cambiar lso estados
picture.title = 'Another Title'
// El archivo modificado
console.log('album', album)

// Para hacerlo de manera explícita se usa la palabra reservada public antes de las funciones, vraibles

/* 
¿Qué tan conveniente es tener todos los miembros publicos?
No todo se puede cambiar, id...

TS declara de mnera porpia mediante private miembros privados.

*/



