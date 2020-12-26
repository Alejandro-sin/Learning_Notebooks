#Cor me permite ver las correlaciones. entre disp y mpg por ejemplo hay una correlación negativa.
#Lo que quiere decir:A más disp menos millas por galón recorren los carros.-0.8475514
#La correlación no implcia causalidad!!! Cor nos permite verificar lo que dicen neustras visualiaciones.
newdata <- subset(mtcars, select = c(2,7:8,11,12))
cor(newdata)
cor(mtcars[,2:6])


#Cor para Orangeec.

str(orangeec)

pairs(orangeec[,2:6])
cor(orangeec[,2:6])

#Segundo intervalo

#Se puede interpretar qie por ejemplo para unemployment e indice
pairs(orangeec[,5:10])
cor(orangeec[,5:10],use = "complete.obs")

#Para relacionar variables o columnas no consecutivas.

fragmentdata <- subset(orangeec,select=c(5,6,10,11,12,13))
fragmentdata
pairs(fragmentdata)
cor(fragmentdata)

#Para eliminar los NA de lso datoas. usamos: use = "complete.obs", como un argumento que le pasamso a la función. 
cor(fragmentdata,use = "complete.obs")


plot(orangeec$GDP.Growth..~orangeec$Creat.Ind...GDP)
