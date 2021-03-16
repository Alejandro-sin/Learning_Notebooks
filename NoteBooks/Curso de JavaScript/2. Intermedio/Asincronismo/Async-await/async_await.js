/* 

Casi todas las operaciones de JS son asincronas, consulta a basaes de datos, procesameinto de peticiones demoradas
Node no espera si no que delega.


Va a tomar tiempo de ejcución

Await solo está disponible en las funcioens que tengan la palabra async.
*/

async function requestHandler(req, res){
    // Manjear errores, try catch
    try {
    /*  Espere por el busqueda y luego guardela en una variable */
        const user = await User.findByid(req.userId);
        const task = await Task.findByid(user.taskId);
        task.completed =true;
        await task.save();
        res.send("Task completed")
    } catch (error) {
        res.send(error)
    }
}

