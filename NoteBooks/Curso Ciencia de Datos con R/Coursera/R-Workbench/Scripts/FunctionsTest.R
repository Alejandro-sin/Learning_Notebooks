# Me arroja el promedio de 100 numeros aleatorios normales
functiontest <- function(){
  x <- rnorm(100)
  mean(x)
}


second <- function(x){
  x + rnorm(length(x))
}