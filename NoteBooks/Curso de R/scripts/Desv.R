#Desviaci�n est�ndar, el coeficiente de variaci�n y los peligros del promedio.

sd(mtcars$mpg)
mean(mtcars$mpg)

#Coeficiente de varaicion;
desv <- sd(mtcars$mpg)
prom <-mean(mtcars$mpg)
coeficiente_v = (desv/prom)*100
# Al estar por encima del promedio, 29% est� muy alejado del promedio.
coeficiente_v


#Eliminando los NA\'s para hacer los c�lculos.

desv_o <- sd(orangeec$Internet.penetration...population, na.rm =TRUE)
prom_o <- mean(orangeec$Internet.penetration...population,  na.rm =TRUE)
coeficiente_vo = (desv_o/prom_o)*100
# Para el Data Set de Orangeec sucede que est� al 25.24 de dispersi�n,  no son muy consistentes
coeficiente_vo
#Quiere decir que es mejor apoyarse en la mediana o los cuartiles.
#Despues del sumary podmeos inferir que la mitad d elos paises en latam tiene una penetraci�n por encima del 70%...etc.
#en el sumary puedo ver lso missing values.
#Para quitar el NA...
mean(orangeec$Creat.Ind...GDP, na.rm =TRUE)


#Mejorar visualizaciones
#arrange sirve para crear arreglos.
#Ranking


orangeec %>%
  arrange(desc(Creat.Ind...GDP))

#Filtrara y buscar� lo que est� in
topNaranjas <- orangeec %>% 
  filter(Country %in% c("Mexico", "Panama"))

topNaranjas %>%
  arrange(desc(Creat.Ind...GDP))

#He visto "supuestas" mejoras a las variables. las hacen conriviento con mutate o filtrar por.
#Si yo guardo estas variables, lo mejor no ser�a encontrar el m�ximo , m�nimo, almacenarlas y luego usarlas?


#Reto: Sacar los modelos m�s pesados de mi data set
ggplot(maspesados, aes(x=hp, y=mpg))+
    geom_point()
    facet_wrap(~model)
#Face_wrap(~variable) sirve dentro de ggplot para filtrame por variable del Dataset

#El paquete RColorBrewer sirve para mejorar una escala de colores.
    #instrcuccion es brewer.pal(#,"")

    








