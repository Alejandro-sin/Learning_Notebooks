
#Le damos una sola variable, porque la y va la frecuencia.
qplot(orangeec$GDP.PC,
      geom="histogram",
      xlab="Caballos de fuerza" ,
      main ="Carros seg�n caballos de fuerza")

ggplot(orangeecs, aes(x=GDP.PC))+
  #Para creae un intervalor mayor, una barra mas ancha usamos el par�metro binwidth
  geom_histogram(binwidth = 1)+
  labs(x="pib PERCAPITA", y ="Cantidad de paises",title= "PIB percapita en paises latam") +
  #Theme, nos permite modificar nuestro gr�fico.
  theme(legend.position ="none")
theme(panel.background = element_blank(), panel.grid.major = element_blank(),
      panel.grid.minor =element_blank())


#Expresar la msima idea de manera diferente
ggplot()+geom_histogram(data = orangeec,
                        aes(x=GDP.PC),
                        fill ="green",
                        color="black",
                        binwidth = 2000)+
  labs(x="pib PERCAPITA", y ="Cantidad de paises",title= "PIB percapita en paises latam")+
theme(legend.position ="none")
theme(panel.background = element_blank(), 
      panel.grid.major = element_blank(),
      panel.grid.minor =element_blank())


#Expresar la distribuci�n el aporte de l econo�a naranja al PIB
ggplot()+geom_histogram(data = orangeec,
                        aes(x=Creat.Ind...GDP),
                        fill ="green",
                        color="black",
                        binwidth = 1)+
  labs(x="Aporte econom�a naranja al PIB%", y ="Cantidad de paises",title= "Contribuci�n econom�a Naranja en paises latam")+
  theme(legend.position ="none")
  theme(panel.background = element_blank(), 
      panel.grid.major = element_blank(),
      panel.grid.minor =element_blank())

#Veamos distribuci�n de frecuencias en cuanto a la penetraci�n ene internet.
ggplot()+geom_histogram(data = orangeec,
                          aes(x=Internet.penetration...population),
                          fill ="blue",
                          color="black",
                          binwidth = 5)+
    labs(x="Penetraci�n internet como % poblaci�on", y ="Cantidad de paises",
         title= "Penetraci�n  de internet en paises latam")+
    theme(legend.position ="none")
    theme(panel.background = element_blank(), 
        panel.grid.major = element_blank(),
        panel.grid.minor =element_blank())
    
#boxplot
    boxplot(mtcars$hp,
            ylab="Caballos fuerza",
            main ="Caballos de fuerza en mtcars")
    
    
#    

ggplot(mtcars, aes(x=as.factor(cyl),y =hp, fill=cyl))+
    geom_boxplot(outlier.colour = "red", alpha=0.7)+
    labs(x="Cilindraje", y ="Caballos de fuerza",
       title= "Caballos de fuerza seg�n mtcars")
    theme_classic()

#    
ggplot(mtcars, aes(x=am,y =mpg, fill=am))+
      geom_boxplot()+
      labs(x="Tipo de caja", y ="Millas por gal�n",
           title= "Millas por gal�n seg�n tipo de caja-mtcars")
    theme_classic()
    
#Para cambiar la variable logica a numerica
  mtcars$am <- factor(mtcars$am, levels = c(TRUE, FALSE),
                      labels =c("automatic", "manual"))
  
  
  #Percapita por encima de promeido.
  
economy <- mean(orangeec$GDP.PC)
economy
#pARA AHCER EL CAMBIO DEBEMSO USAR DEPLOYER PACKAGE.

#Funcion pipe %>% De un data set a otro, Mutate  es de dplyr me cambiar� una nueva variable
orangeec <-  orangeec %>%
  mutate(Strong_economy = ifelse(GDP.PC < economy, "  economy < Xmean PIB_Per c�pita","economy > Xmean PIB_Per c�pita"))



#Aporte econom�a Narana pro debajo y encima de PIB

ggplot(orangeec, aes(x=Strong_economy,y =Creat.Ind...GDP, fill=Strong_economy))+
  geom_boxplot(alpha=0.4)+
  labs(x="Tipo de pa�s", y ="Aporte econom�a naranja al pib",
        title= "Aporte econom�na naranja en PIB por pa�s/latam, alto y bajo PIB percapita.")
  theme_classic()
  
  

#Penetraci�n de internet en esto paises.
  
  ggplot(orangeec, aes(x=Strong_economy,y =Internet.penetration...population, fill=Strong_economy))+
    geom_boxplot(alpha=0.4)+
    labs(x="Tipo de pa�s", y ="%Penetraci�n internet",
         title= "Penetraci�n de interernet con alto y bajo PIB percapita.")
  theme_classic()
  

  str(orangeec)
