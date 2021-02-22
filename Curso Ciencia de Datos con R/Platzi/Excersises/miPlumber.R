#Debemso indicar parametros y peticiones.

#*@param msg mensa
#* @ get/echo
function(msg=""){
  list(msn=paste0("El texto es ", msg))
  
}

#En el archivo app.R se pone. 
#Para conectar en producción usamos Plumber.
#install.packages("plumber")

#Hacemos un fichero.r con funciones de API (get..post)

#Levantamos el servidor en un puerto
r <- plumb("")
r$run(port=puerto)

#Hacemos pruebas de solicitud con curl. Las pruebas se hacen en la terminal