
/*  Generamos la ruta d ela API  */
const API = 'https://rickandmortyapi.com/api/character/';


/* getData tiene como función traer datos de la API. y hacer render de la aplciación, 
mediante async y await.
Si el llamado se hace sin id me trae la API  y si lo hago con id me genera un url


*/
const getData = async (id) => {
    const apiURL = id ? `${API}${id}` : API;
    /* LLamado al fetch , encapsular en un try y catch*/
    try {
        const response = await fetch(apiURL);
        /*  Puedo manipular la repsuesta a un objeto JSON miterable*/
        const data = await response.json();
        return data;
    }   catch(error){
        console.log("Fetch Error", error);
    }

};


export default getData;