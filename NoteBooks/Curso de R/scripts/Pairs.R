# El prop�sito de esta parte es usar la funci�n pairs para mirar 
#la correlaci�n de mis pares de columnas.


pairs(mtcars[,2:6])


#Es una forma de dcirle a R que me filtre por las columnas que quiero. Inclusi�n.
newdata <- subset(mtcars, select = c(2,7:8,11,12))
pairs(newdata)

#Es una forma de dcirle a R que me filtre por las columnas que NO quiero.Exclusi�n
#pairs(mtcars[,-c(1,2,3...)])


#Sleecionar filas con filter
Caballos <- filter(mtcars,hp >=245)
Caballos

#Para ver correlaci�n de variables en las filtradas
pairs(Caballos[,2:6])


#Queda por revisar el caso del paquete string para detectar strings.
#Install Packages ("String") Me permitir� usar stringsWarning in install.packages :
# package 'String' is not available (for R version 4.0.0)

merc <- mtcars %>%
#  filter(stri_detect(model,"Merc"))
merc

setRepositories()
?setRepositories



