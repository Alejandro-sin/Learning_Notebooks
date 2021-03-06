#Scatter polot de dos variables
# Nota: Hubiese tenido m�s sentido evaluarlo como 

ggplot(mtcars, aes(hp,mpg))+
  geom_point()+
  labs(x="Caballos de fuerza", y="Millas por gal�n",title = "HP/mpg", 
       caption="Busca las relaciones entre los caballos de fuerza de lso autom�viles seg�n
       el consumo de gasolina gastada por milla recorrida, la tendencia es que a mayor caballos de fuerza
       recorren menos millas por gal�n, se gana velocidad pero se piede alcance" )
  theme_bw()
  
  

#Evaluar el peso y como incide en la potencia. 
# Siempre la variable dependiente en y. Quiero ver como depende la potencia Hp seg�n el peso

ggplot(mtcars, aes(wt, hp))+
  geom_point()+
  labs(x="Peso", y="Potencia",title = "Wt/hp")+
theme_linedraw()

#Relaci�n para 4 variables
# A mayor cilindraje mayores los caballos de fuerza, los carros con caja de cambios manuels son mas veolces pero recorren menos disntacias
ggplot(mtcars, aes(hp,qsec))+
    geom_point(aes(color=am, size =cyl))+
    labs(x="Caballos de fuerza",y="Tiempo en 1/4 de millas", title="Caballos-velocidad teniendo en cuenta el cilindraje y el tipo de caja de cambios, si manual o automatica")



#EDA con dataset proyecto usando gr�ficas de dispersi�n con m�s de dos variables - ggplot2 - plotlyggplot(mtcars, aes(hp,qsec))+
#La penetraci�n de internet de x pa�s aporta un y%  en econom�a naranja.  Cabe entender que cada X pa�s  tiene un crecimeinto En GDP,
ggplot(orangeec, aes(Internet.penetration...population,Creat.Ind...GDP))+
  geom_point(aes(color=factor(Strong_economy),size = GDP.Growth..))+
  labs(x="Penetraci�n Internet %",y="Aporte econom�a Naranja PIB", title="Internet y aporte Econom�a naranja seg�n y crecimieto PIB")



# Voy hacer un EDA para 4 variables, mi variable independiente ser� la inversi�n en educaci�n, y mi variable dependiente ser� la tasa de desempleo.
# el color por el que quiero diferenciar es por el factor Strong economy, que me da la poblaci�n por encima o debajo dle promedio del PIB percapita.
# PIB percapita es el valro monetario de un pa�s en base a su poblaci�n, o cuanto ha producido la poblaci�n para el pa�s.
# Y quier que el tam�o de mis puntos corresponda a un tama�o poblacional que sea seg�n el �ndice de pobreza.
ggplot(orangeec, aes(Education.invest...GDP,Unemployment))+
  geom_point(aes(color=factor(Strong_economy), size =X..pop.below.poverty.line))+
  labs(x="Inversion en educacion", y="Tasa de desempleo (%)", title = "Relaci�n entre la tasa de desempleo VS la inversi�n en educacion.", caption = "
       Ver este gr�fico teniendo en cuenta el Crecimiento PIB_percapita como una variable discreta que ayuda a confirmar tendencias, as� como GDP.Growth")
  

#install.packages("plotly")
my_graph <-ggplot(orangeec, aes(Internet.penetration...population,Creat.Ind...GDP, label = row.names(orangeec)))+
  geom_point(aes(color=factor(Strong_economy),size = GDP.Growth..)) +
  labs(x="Penetraci�n Internet %", y="Aporte econom�a Naranja PIB" , title="Internet y aporte Econom�a naranja seg�n y crecimieto PIB")
my_graph
p = ggplotly(my_graph)
p
