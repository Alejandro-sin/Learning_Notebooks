// ASERCIONES DE TIPO

/* 

Cuando el programador conoce más que TS sobre el valor de una variable
"Confía en mi sé lo que hago.." Parece casteo pero no es lo mismo, se usan dos sintáxisi

angle-bracket y variable as-


*/

// <> Angle bracket syntax

let username: any;
username = "Alejandro";
// Podemos asumoir que tenemos una cadena al concoer más del código, le pedicmos al compilador que confíen en nosotros.

/* 
Sirve para, declaro una variable mensaje que será una string y sé que lo que le paso como 
parámetro es un string del que quiero su largo mayor a 5. Lo tienes o no?

Si si me saluda, si no... me dice que el usuario es muy corto.


* (<string>username).length Esta estructura me permtie decirle a lo que está aquí es de tipo string y por eso puedo acceder a lenght


*/
let message : string = (<string>username).length > 5 ?
                        `Welcome ${username}`:`Username is too short`;
console.log('message', message)


let usernameWithId: any = "Alejandro 1"; // En algunas circunstancias las API nos devuelven el username y el id asíesoaciacios.

//¿Como obtengo el username=

username = ( <string>usernameWithId).substring(0,10)
console.log('user', username)




// SYNTAX AS

/* 
Es otra forma de aserción o afirmación en TS.

*/

message = (username as string).length > 5 ?  `Welcome ${username}`:`Username is too short`;

let helloUser: any;
helloUser = "Mi nombre"
username =  (helloUser as string).substring(0,6);
console.log('username', username);


/* 
La prioridad de usar as por encima de <> es desde la versión 1.6 de Typescript debido a que había ambigüedad en archivos .jsx

{
  rules: {
    "no-angle-bracket-type-assertion": true
  }
} */