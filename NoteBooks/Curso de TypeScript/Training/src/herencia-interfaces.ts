// Sirve para no causar conflicto por llamar a mi enum en otro archivo.
export {};

// Definir enumerado
enum PhotoOrientation{
    Landscape,
    Portrait,
    Square,
    Panorama
}

// Entidad album para agrupar fotografias
interface Album  extends Entity{
/*     id: number;
    title: string;
    Ya no se necesitan porque son una copia de los atributos de entity
 */
    description: string;
}

interface Picture extends Entity{
/*     id: number;
    title: string; */
    orientation: PhotoOrientation
}

/* 
Ambas interfaces comparten el id, y el title.   
¿Como mejorar el código  si queremos conservar a definciión acutal de t´tulo e Id?

Usando herencia de interfaces.

Quienes serán instancia usar´n la palabra extends. Así se elacionan las interfaces con entity.


*/

interface Entity {
    id: number;
    title: string;
}


// Probamos la herencia:

const  album: Album = {
    id:1,
    title: "Anymadversion",
    description: "This is an album and sin heredad la descripción."
}

const  picture: Picture = {
    id:2,
    title: "Anymad",
    orientation: PhotoOrientation.Portrait
}

let newPicture = {} as Picture;
newPicture.id =30;
// Podemos cambiar los estados, esto significa que puedo reasingar las propiedades de estos objetos.
console.log('album', album)
console.log('picture', picture)
console.log('picture', newPicture)