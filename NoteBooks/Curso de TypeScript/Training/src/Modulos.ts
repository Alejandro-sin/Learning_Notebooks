/* photo-app.ts */

export enum PhotoOrientation {
	Landscape,
	Portrait,
	Square,
	Panorama
}

export class Item {
	constructor(public readonly id: number, protected title: string) {}
}

export class User {
	private album: Album[];

	constructor(private id: number, private username: string, private firstName: string, private isPro: boolean) {
		this.album = [];
	}

	addAlbum(album: Album) {
		this.album.push(album);
	}
}

export class Album extends Item {
	private pictures: Picture[];

	public constructor(id: number, title: string) {
		super(id, title);
		this.pictures = [];
	}
	public addPicture(picture: Picture) {
		this.pictures.push(picture);
	}
}

export class Picture extends Item {
	public constructor(id: number, title: string, private _date: string, private _orientation: PhotoOrientation) {
		super(id, title);
	}
	public toString() {
		return `[id: ${this.id},
                 title: ${this.title},
                 orientation: ${this._orientation}]`;
	}
}

/* 
main.ts
 */
/* import { User, Album, Picture, PhotoOrientation } from './photo-app';

const user = new User(1, 'Erickowski', 'Erick', true);
const album = new Album(10, 'Platzi Album');
const picture = new Picture(1, 'Foto', '2020-08', PhotoOrientation.Landscape);

// Creamos relaciones
user.addAlbum(album);
album.addPicture(picture);

console.log('user', user); */