
##Vectores
#Un vector es una coleccion de elementos, utilizamos c(elem1, elem2,..., elemN)
c(10,11,15)
mivec<-c(10,11,15)
mivec/2
nuevovec<-mivec+mivec
nuevovec
c(60, nuevovec)
#Tipos de vectores
a<-c("hola", "adios")
a
b<-c(TRUE, FALSE)
b 
#Indexing vector mediante  []
a[1]
a[1]<-"caracola"
a
#Creando una serie
c<-c(7:12)
c[1:2]
#Eliminando elementos de un vector "-"
c[-4]


##LISTAS, colecciones de elementos que puede ser diferentes tipos
# Las listas se crean con list() separando campos por comas con clave/valor
# Se indexan con $ o con [[]]
milista<-list(num=42, saludo="Hola Rmundo")
milista$saludo
milista[[2]]

##Funciones basicas de analisis
class(milista)
typeof(milista)
str(mivec)


##Matrix filas y columnas de datos como tabla todos del mismo tipo
# Las columnas tienen nombre  colnames y las filas rownames
mat<-matrix(c(1,3,3,2,2,2),nrow=2, ncol=3)
mat
rownames(mat)<-c("primera", "ultima")
mat
colnames(mat)<-c("uno", "dos", "tres")
mat
#Indexado en matrices [fila, columna]
mat[1,2]

##Dataframes son matrices que pueden albergar diferentes tipos de datos en sus columnas
edad <- c(22, 34, 29, 25, 30, 33, 31, 27, 25, 25)
tiempo <- c(14.21, 10.36, 11.89, 13.81, 12.03, 10.99, 12.48, 13.37, 12.29, 11.92)
sexo <- c("M","H","H","M","M","H","M","M","H","H")
misDatos <- data.frame(edad,tiempo,sexo)
misDatos
#indica la dimensión
dim(misDatos)
str(misDatos)

#Indexando dataframes con [fila, columna] o $columna[fila]
misDatos[,1]
misDatos[2,3]
colnames(misDatos)
rownames(misDatos)
misDatos[2,3]
misDatos$sexo[2]  

#Me permtie filtrar mis datos y almacenarlos en variable
dat<-misDatos$tiempo>=12
val<-which(dat)
misDatos[val,]


##Tipo factor --> catergorias
str(misDatos)
misDatos$sexo
misDatos$sexo<-as.character(misDatos$sexo)
str(misDatos)

##Leer/escribir ficheros
write.csv(misDatos, "/tmp/datos.csv")
file<-read.csv("/tmp/datos.csv")
head(file)

#Data set Iris, e sun ds por defecto en R. 
iris
write.csv(iris, "/home/tmp/iris.csv")

