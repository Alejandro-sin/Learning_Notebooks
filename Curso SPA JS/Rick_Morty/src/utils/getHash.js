/* Cuando solo vamos a usar una lóguica no hacnefalta los brakects 

Con esto obtengo el hash y debo parsear los elementos que va a necesitar.

1. Slice:
2. toLocateLowerCase() para que me devuelva en minusculoa
3.Split nos va a convertir el string a un arreglo, y nos elimine lso slash incorporado, solo dejando el elmento que necesito. Devuelve hasata aqui ['','1','']
4. Necdesito solo el lemento del medio, por lo que accederé mediante posiciones arrya[n]
5. En dado caso de no enronctrada usamos el OR
*/
const getHash = () => 
    location.hash.slice(1).toLocaleLowerCase().split('/')[1] || '/';

    export default getHash;



