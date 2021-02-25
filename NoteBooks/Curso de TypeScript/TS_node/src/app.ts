import express, {Application,Request,Response,NextFunction} from 'express';


//Envío un hello worl al navegador.
const  app: Application = express();


/* 

const  app: express.Application = express();

Al hacer referencia al objeto express . Aplication, traigo el tipo application.

*/


const add = (a: number, b:number):number => a+b;


app.get('/', (req:Request, res:Response, next: NextFunction) =>{
    console.log(add(5,5))
    res.send('Hello');
});


app.listen(5000,() =>console.log("Server runing"))