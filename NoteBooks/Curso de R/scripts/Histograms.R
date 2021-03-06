
#Le damos una sola variable, porque la y va la frecuencia.
qplot(mtcars$hp,
      geom="histogram",
      xlab="Caballos de fuerza" ,
      main ="Carros seg�n caballos de fuerza")

ggplot(mtcars, aes(x= cyl))+
#Para creae un intervalor mayor, una barra mas ancha usamos el par�metro binwidth
    geom_histogram(binwidth = 1)+
    labs(x="Caballos de fuerza", y ="Cantidad de carros",title= "Caballos de fuerza 
         en carros selecionados") +
#Theme, nos permite modificar nuestro gr�fico.
    theme(legend.position ="none")
    theme(panel.background = element_blank(), panel.grid.major = element_blank(),
          panel.grid.minor =element_blank())


#Expresar la msima idea de manera diferente
ggplot()+geom_histogram(data = mtcars,
                        aes(x=hp),
                        fill ="green",
                        color="black",
                        binwidth = 20)+
                        labs(x="Caballos de fuerza", y ="Cantidad de carros",title= "Caballos de fuerza 
         en carros selecionados")+
  #Nuevo contenedor, ajuste, el l�mite de x.
  xlim(c(80, 280))+ 
  theme(legend.position ="none")
  theme(panel.background = element_blank(), panel.grid.major = element_blank(),
      panel.grid.minor =element_blank())

                        

str(mtcars)