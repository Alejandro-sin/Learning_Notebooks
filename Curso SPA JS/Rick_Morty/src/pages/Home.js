import getData from '../utils/getData';

/* Inyección de getData mediante lamado ayncrono. */
const Home = async () => {
  /*Hace llamado a la api estandar.  */
    const characters = await getData();

    /* Convertimos tempalte para que haga una iteración opor todos los elementos.
    hagohago asignación de lso personajes dnetro del snipet html, esta en la propiedad results.
    hago map para tenornar un nuevo arreglo con la estructura.
  
  
    ${characters.results.map()}   Me retorna todos lso personajes iterados + el tempalteta o palntilla
    de html creada.

    <a href="#/${character.id}/">  Con esta lñinea modifico dinamicamente la url para que me traiga
    del personaje el id.


    join('') Manipula el string para que el html que es un bloque venga sin comillas y se me represente como
    lenguaje po ( XML) En el navegador.

    */
    const view = `
      <div class="Characters">
      ${characters.results.map(character => `
      <article class="Character-item">
          <a href="#/${character.id}/">
            <img src="${character.image}" alt="${character.name}">
            <h2>${character.name}</h2>
          </a>
        </article>
      `).join('')}
        
      </div>
    `;
    return view;
  };
  
  export default Home;
