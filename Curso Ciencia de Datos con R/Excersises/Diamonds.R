View(diamonds)

#Muestro las variables carat y price con geometria de puntos
ggplot(diamonds)+
       geom_point(aes(carat,price))
#ver dimensión de diamons
dim(diamonds)

#Quiero extraer un vector de mi DS sin las columnas de la 1 a la 4, porque son de tipo factor o string. 
#Osea limipo de caracteres.
#al plotear la gráfica requerimos el valor máximo y mínimo.
data <-diamonds[c(1:1),-(1:4)]
data

#Sobreescribir con rbin
data <- rbind(rep(400,5),rep(0,5), data)
