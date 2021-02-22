
#Le damos una sola variable, porque la y va la frecuencia.
qplot(orangeec$GDP.PC,
      geom="histogram",
      xlab="Caballos de fuerza" ,
      main ="Carros según caballos de fuerza")

ggplot(orangeecs, aes(x=GDP.PC))+
  #Para creae un intervalor mayor, una barra mas ancha usamos el parámetro binwidth
  geom_histogram(binwidth = 1)+
  labs(x="pib PERCAPITA", y ="Cantidad de paises",title= "PIB percapita en paises latam") +
  #Theme, nos permite modificar nuestro gráfico.
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


#Expresar la distribución el aporte de l econoía naranja al PIB
ggplot()+geom_histogram(data = orangeec,
                        aes(x=Creat.Ind...GDP),
                        fill ="green",
                        color="black",
                        binwidth = 1)+
  labs(x="Aporte economía naranja al PIB%", y ="Cantidad de paises",title= "Contribución economía Naranja en paises latam")+
  theme(legend.position ="none")
  theme(panel.background = element_blank(), 
      panel.grid.major = element_blank(),
      panel.grid.minor =element_blank())

#Veamos distribución de frecuencias en cuanto a la penetración ene internet.
ggplot()+geom_histogram(data = orangeec,
                          aes(x=Internet.penetration...population),
                          fill ="blue",
                          color="black",
                          binwidth = 5)+
    labs(x="Penetración internet como % poblaciñon", y ="Cantidad de paises",
         title= "Penetración  de internet en paises latam")+
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
       title= "Caballos de fuerza según mtcars")
    theme_classic()

#    
ggplot(mtcars, aes(x=am,y =mpg, fill=am))+
      geom_boxplot()+
      labs(x="Tipo de caja", y ="Millas por galón",
           title= "Millas por galón según tipo de caja-mtcars")
    theme_classic()
    
#Para cambiar la variable logica a numerica
  mtcars$am <- factor(mtcars$am, levels = c(TRUE, FALSE),
                      labels =c("automatic", "manual"))
  
  
  #Percapita por encima de promeido.
  
economy <- mean(orangeec$GDP.PC)
economy
#pARA AHCER EL CAMBIO DEBEMSO USAR DEPLOYER PACKAGE.

#Funcion pipe %>% De un data set a otro, Mutate  es de dplyr me cambiará una nueva variable
orangeec <-  orangeec %>%
  mutate(Strong_economy = ifelse(GDP.PC < economy, "  economy < Xmean PIB_Per cápita","economy > Xmean PIB_Per cápita"))



#Aporte economía Narana pro debajo y encima de PIB

ggplot(orangeec, aes(x=Strong_economy,y =Creat.Ind...GDP, fill=Strong_economy))+
  geom_boxplot(alpha=0.4)+
  labs(x="Tipo de país", y ="Aporte economía naranja al pib",
        title= "Aporte economína naranja en PIB por país/latam, alto y bajo PIB percapita.")
  theme_classic()
  
  

#Penetración de internet en esto paises.
  
  ggplot(orangeec, aes(x=Strong_economy,y =Internet.penetration...population, fill=Strong_economy))+
    geom_boxplot(alpha=0.4)+
    labs(x="Tipo de país", y ="%Penetración internet",
         title= "Penetración de interernet con alto y bajo PIB percapita.")
  theme_classic()
  

  str(orangeec)
