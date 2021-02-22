#* @param precio
#* @param opiniones
#* @param peso
#* @param volumen
#* @param potencia
#* @param alto
#* @param ancho
#* @param profunidad
#* @get /getCluster

#Dist me permite calcluar las distancia de dos puntos dentro de una matriz
#Nuestro porpósito es tomar los datos en un vector, con la idea de calcular las disctancia en un nuevo atributo( nuevo precio, altura)
# contra los clusters, para evluar las distancias a cada uno de ellos.
# Calculamos la distancia de la variable de entrada con el centro de cada uno de os atributos.
#Luego cada columna la metemos en una matriz, con cada una de las distancias a los centros, de tal forma que podamos sumer la distancia de cada cluster y saber cual es el mínimo.
#Plumber necesita un espacio al final d ela función apra  ue no se crashee
# Se usan matrices auxiliares para esto.


function(precio, opiniones, peso,volumen,potencia,alto,ancho,profundidad){
  library(stringr)
  #campos<-str_split_fixed(values, ",", n=8)  
  campos<-c(precio,opiniones,peso,volumen,potencia,alto,ancho,profundidad)?
  campos<-as.numeric(campos)
  mycluster$centers
  #Vamos a crear una matriz donde( almacenar por atributo la distancia a cada cluster
  midist<-matrix(0, ncol=8, nrow=8)
  
  #Nota importante, al recorrer las variables debe estar ordenadas para que las primera sean las mismas que aprecen en los clusters.
  
  for(i in 1:8){
    a<-dist(x=c(campos[i],mycluster$centers[,i])) #Calculamos  la distancia del valor a cada centro
    b<-as.matrix(a) #Lo convertimos a matriz para poder acceder a los vlaores
    distancia<-b[-1,1] #Eliminamos la distancia consigo mismo
    midist[i,]<-distancia #Objeto matriz con cada una de las distancias a los clusters.
  }
  rownames(midist)<-c("Precio" , "Opiniones","Peso del producto" ,"Volumen","Potencia", "alto", "ancho" ,"profundidad")
  dist_total<-apply(midist, 2, sum)#Sumamos las distancias, econtramso qu la distancia al cluster 4 es la menor.
  #Requerimos un metodo que me encuentre a partir d eun ector la distancia menor.Which.min 
  clus<-which.min(dist_total) #Identificamos el cluster de menor distacncia
  
  val<-paste(as.character(mycluster$centers[clus,]), collapse = ",")
  paste0("Cluster asociado es ",clus," con valores: ", val )
  
}
#Se le vantó un server y se corrió la aplicación alojada en x dirección. La petición que se manda
#Esto nos delueve el cluster 5 que eraa aquel que tenia nuestra distancia menor.
#curl "http://localhost:8000/getCluster?precio=-0.2458767&opiniones=0.3095074&peso=1.0861028&volumen=0.32609&potencia=0.1184234&alto=0.322571&ancho=0.4440596&profundidad=-0.3254523"
