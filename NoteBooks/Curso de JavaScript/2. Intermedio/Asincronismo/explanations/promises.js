/* 

Las promesas encadenan respuestas mediante los return. De manera sencuencial.


*/



/* 

then = cuando termine de ejcutarle la linea anterior,
.catch = cuando ocurre erro, sirve para manjear errores.

*/


/*  Esta funci{on retorna un id que el usuario solciita
} */
function requestHandler(req, res){
    User.findById(req,userid)
        .then(function (user){
            //res.send(user)---> Tambien puedo retornar un valro de un modelo de datos que se encadena a la siguiente tarrea 
        })
        .then(function(task){
            task.completed =true;
            return task.save();
        })
        .then(function(){
            res.send("Tareas completadas.")
        })
        /*  Captura cualuqier error */
        .catch(function(errores){
            res.send(errores);
        })

}