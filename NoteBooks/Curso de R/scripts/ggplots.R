#Scatter polot de dos variables
# Nota: Hubiese tenido más sentido evaluarlo como 

ggplot(mtcars, aes(hp,mpg))+
  geom_point()+
  labs(x="Caballos de fuerza", y="Millas por galón",title = "HP/mpg", 
       caption="Busca las relaciones entre los caballos de fuerza de lso automóviles según
       el consumo de gasolina gastada por milla recorrida, la tendencia es que a mayor caballos de fuerza
       recorren menos millas por galón, se gana velocidad pero se piede alcance" )
  theme_bw()
  
  

#Evaluar el peso y como incide en la potencia. 
# Siempre la variable dependiente en y. Quiero ver como depende la potencia Hp según el peso

ggplot(mtcars, aes(wt, hp))+
  geom_point()+
  labs(x="Peso", y="Potencia",title = "Wt/hp")+
theme_linedraw()

#Relación para 4 variables
# A mayor cilindraje mayores los caballos de fuerza, los carros con caja de cambios manuels son mas veolces pero recorren menos disntacias
ggplot(mtcars, aes(hp,qsec))+
    geom_point(aes(color=am, size =cyl))+
    labs(x="Caballos de fuerza",y="Tiempo en 1/4 de millas", title="Caballos-velocidad teniendo en cuenta el cilindraje y el tipo de caja de cambios, si manual o automatica")



#EDA con dataset proyecto usando gráficas de dispersión con más de dos variables - ggplot2 - plotlyggplot(mtcars, aes(hp,qsec))+
#La penetración de internet de x país aporta un y%  en economía naranja.  Cabe entender que cada X país  tiene un crecimeinto En GDP,
ggplot(orangeec, aes(Internet.penetration...population,Creat.Ind...GDP))+
  geom_point(aes(color=factor(Strong_economy),size = GDP.Growth..))+
  labs(x="Penetración Internet %",y="Aporte economía Naranja PIB", title="Internet y aporte Economía naranja según y crecimieto PIB")



# Voy hacer un EDA para 4 variables, mi variable independiente será la inversión en educación, y mi variable dependiente será la tasa de desempleo.
# el color por el que quiero diferenciar es por el factor Strong economy, que me da la población por encima o debajo dle promedio del PIB percapita.
# PIB percapita es el valro monetario de un país en base a su población, o cuanto ha producido la población para el país.
# Y quier que el tamño de mis puntos corresponda a un tamaño poblacional que sea según el índice de pobreza.
ggplot(orangeec, aes(Education.invest...GDP,Unemployment))+
  geom_point(aes(color=factor(Strong_economy), size =X..pop.below.poverty.line))+
  labs(x="Inversion en educacion", y="Tasa de desempleo (%)", title = "Relación entre la tasa de desempleo VS la inversión en educacion.", caption = "
       Ver este gráfico teniendo en cuenta el Crecimiento PIB_percapita como una variable discreta que ayuda a confirmar tendencias, así como GDP.Growth")
  

#install.packages("plotly")
my_graph <-ggplot(orangeec, aes(Internet.penetration...population,Creat.Ind...GDP, label = row.names(orangeec)))+
  geom_point(aes(color=factor(Strong_economy),size = GDP.Growth..)) +
  labs(x="Penetración Internet %", y="Aporte economía Naranja PIB" , title="Internet y aporte Economía naranja según y crecimieto PIB")
my_graph
p = ggplotly(my_graph)
p
