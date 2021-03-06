# APLICACI�N DE A LGORITMO  DE KMEANS EN THEOP y IRIRS
#El kmeans nos agrupar itemss seg�n atributos similares, podemos asocair empresas en funci�n dle numeor de compras que hacen
#En que zonas lo hacen, podemos dirirgnos mejor a sectores, clientes y publicdiad.
# Podemos evaluar que tipo de compradores tenemos y generar estrategias para mejroar el marketing y acercamiento a estos.


#El algoritmo converge cuando las uma de las distancias a los centros no var�a muhco.
# mayor distancia entre los individuos mayor error habr�.

dataset <- iris[,-5]
str(dataset)
View(dataset)
dataCluster <- kmeans(dataset,3, nstart = 10, iter.max = 20)
dataCluster



#N�mero de iteraciones que hizo
iter<-dataCluster$iter
#Tama�os de los cluster
size <-dataCluster$size
#Nos habla sobre las distancias de error. Nos devuelve las distancias medias para cada cluster. 
#Este permite medir, cuanto de bueno es la clusterizaci�n. Entre mas peque�a los valroes 
#m�s cercanos est�ran los elemntos de nuestros centros
withinss <- dataCluster$withinss


#Para calcular el Elbow, hay que hacer el analisisi el withins a lo largo del numeor clusters que moentemos.
#______________________________________________________________________
#Lo primero que ponemos a la hora de calcular la suma de distancias de un cluster es la varianza.
wss<-(nrow(dataCluster)-1)*sum(apply(dataCluster,2,var))
#Iteramos, para cada numero de clusters calculamos el withins y lo guardamos en wss
for(i in 2:4) wss[i]<-sum(kmeans(dataCluster,centers=i)$withinss)
wss
plot(1:20, wss, type="b", xlab="Numero de clusters", ylab= "withinss groups")
#______________________________________________________________________





