// Get y Set

// usamos los métodos accesores.


export{};



enum PhotoOrientation{
    Landscape,
    Portrait,
    Square,
    Panorama
}

/* 



*/
class Picture {

    // Propiedades
    private _id: number;
    private _title: string;
    private _orientation: PhotoOrientation;
    
    // Al definir una clase necesitamos un constructor para poder crear objetos a partir de la abstración
    public constructor(id: number, 
                title: string, 
                orientation: PhotoOrientation){
            this._id = id;
            this._title = title ;
            this._orientation = orientation;
    }

    // Añadimos un get para identificar el estdo
    get id(){
        return this._id;
    }
    // Metodo accesor, cambia el estado dle identificador.
    set id(id: number){
        this._id =id;
    }
    get title(){
        return this._title;
    } 
    
    set title(title:string){
        //return this._title;
    }
    get orientation(){
        return this._orientation
    }
  /*   set orientation(orientation: PhotoOrientation){
        return this._orientation = orientation;
    } */



    // Comportamiento está dado por otras funciones, 

    public toString() {
        return `[id: ${this.id}
                title: ${this.title}
                orientation: ${this.orientation}]`;
    };
};

class Album {
    private id: number;
    private title: string;
    private pictures: Picture[]
    
    public constructor(id: number, title: string) {
        this.id =id;
        this.title =title;
        this.pictures =[]

    }

    public addPicture(picture: Picture){
        this.pictures.push(picture);
    }
}