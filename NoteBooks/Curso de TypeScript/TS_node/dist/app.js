"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
//Envío un hello worl al navegador.
const app = express_1.default();
/*

const  app: express.Application = express();

Al hacer referencia al objeto express . Aplication, traigo el tipo application.

*/
const add = (a, b) => a + b;
app.get('/', (req, res, next) => {
    console.log(add(5, 5));
    res.send('Hello');
});
app.listen(5000, () => console.log("Server runing"));
