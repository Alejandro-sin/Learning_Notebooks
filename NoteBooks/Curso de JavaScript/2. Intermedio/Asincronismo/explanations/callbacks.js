/* 

El lenguaje usa callbascks se usa para las peticioens asincroans.

Cuando se le hace una petición al server,  se hacen fdiferntes operacioens antes de devolver 
la respuesta.


*/

/* Función servidor de node para peticion de uan solicitud,
voy a pedir un userid y lo hago con un método como el que vemos, para manejar estas peticiones mediante
asincornimo usamos callbasck como un argumento adicional en el método findById

*/
/* 
function requestHandler(req, res){
     Consulta a base de datos 
    User.findById(req.userId, function(error, user){
    Consulto un usuario por id, cuando BD me lo devuelva voy a manejar la respuesta con esta función
      
        if(error){
            res.send(error);

        } else{
           Puedo solicitar los mimso 
        Task.findById(req.userId, function(error, task){
            if(error){
                res.send(error);
            } else {
               task.coompleted = true;
            }
    })
})

*/