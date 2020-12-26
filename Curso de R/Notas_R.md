
# **Indice**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


+ [Hipervínculo](url)
 + + [Hipervínculo](url)
+ [Hipervínculo](url)
+ + + [Hipervínculo](url)
+ + +  [Hipervínculo](url)
+ [Hipervínculo](url)

■________________________________________________________________ set() ■





******************************************************
#    **WALL:R programming**
******************************************************
* LECTURAS MAESTRAS:
* RESUMEN MAESTRO:
* GLOSARIO UNIVERSAL DE TÉRMINOS:
* ATAJOS:

###    **NOTAS:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


##   **BRICK: Introudcción a R**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **CHUNK:Programación y Data Science**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
La ciencia de datos es muy útil para cualquier área laboral. Actualmente estamos viviendo la cuarta revolución industrial gracias a la masiva cantidad de datos que generamos día a día, las empresas con estos datos buscan satisfacer de mejor forma nuestras necesidades, aquí nace el Big Data.

Big Data se compone de tres componentes claves:

Volumen: tiene una cantidad de datos mucho mayor a la soportada dentro de un Excel.
Velocidad: mayor a la acostumbrada con anterioridad.
Variedad: se manejan datos estructurados y no estructurados como fotos, mensajes, etc.
Un científico de datos necesita tener los conocimientos de:

Matemáticas y estadística.
Programación.
Conocimiento del negocio o contexto.
Habilidad para visualizar los datos y capacidad para comunicarlos.

###    **CHUNK:R y proyecto economía naranja.**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Para la ciencia de datos es común utilizar dos lenguajes: R y Python.
En este curso veremos R, un lenguaje especializado en manejar datos de manera estadística creado en 1993 en la universidad de Auckland Nueva Zelanda.

A lo largo del curso veremos:

Estructuras, tipos de datos y sintaxis.
EDA: Exploratory data analysis.
Estadística descriptiva.
Ajuste de datos.
Visualización de datos.
Organización de información con R Markdown.


+ Proyecto: ¿Qué es la economía naranja?
_____________________________

Es donde se mezclan las industrias culturales con las áreas de soporte como el desarrollo de aplicaciones o software.

Buscaremos responder a la pregunta:
Si tienes un startup que hace software, ¿en qué país abrirías una oficina?

El dataset de economía naranja fue creado por la profesora con las siguientes variables:

Aporte de servicios a PIB.
Aporte de economía naranja a PIB.
Penetración de internet.
Inflación.
Tasa de desempleo.
Población debajo de la línea de pobreza.
Edad mediana de la población.
Porcentaje de la población entre 25-54 años.
Inversión en educación %PIB.

Si tengo una pregunta, el data set no va a estar. Debo  empaparme d elos datos.

CIA FACTBOOK para extraer datos.


https://github.com/sap0408/Orange-Economy


###    **CHUNK:Variables, tipos de datos y estructuras**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
En esta clase vamos a hacer unos cuantos cálculos dentro de R Studio para ir acostumbrándonos a su sintaxis y comandos útiles.

Dos comandos que utilizaras muy seguidos son:

(Ctrl + L): Se encarga de borrar la consola.
(Ctrl + Enter): Realiza la operación que selecciones.
Asignar un valor a una variable dentro de R se hace mediante el par de signos <- quedando, por ejemplo:

x <- 10
La función View nos muestra nuestro dataset en forma de tabla.

Con alt+94  podemsos usar caret, circunclejo.

View(orangeec) me permite ver mi data set
Puedo usar y asignar variables en R.

== en R es <-
 
 Además de trabajar con el dataset de Orange Economy vamos a necesitar el dataset de mtcars.

Dentro de la consola de R Studio, la función install.packages nos va a ayudar a instalar paquetes, como su nombre lo indica, en este caso intentaremos instalar mtcars.

En caso de no estar disponible para tu versión de R, puedes ir al Github de la profesora y descargarlo.

La función str nos va a mostrar la estructura que tiene el dataset que le pasemos.
Dentro de la consola podemos obtener más información sobre nuestro dataset anteponiendo el signo ? quedando ?mtcars

En el dataset mtcars podemos ver que hay datos de tipo int y num, la diferencia es que num son números con decimal mientras que int son enteros.

Podemos ver que las variables vs y am dentro de mtcars aunque están marcadas con int su función es de tipo boolean, para convertir estos datos utilizaremos la función as.logical

Reto: Explora la estructura del dataset orangeec. Escribe en los comentarios el número de observaciones y variables que encuentres.

se usan para  conocer la estructura de mi data set.
str(mtcar)

Se usa para llamar una ayuda contextual del data set.
?mtcars

Se usa para sabe rel tipo de clase que es algún conjunto de datos pasado por parámetro.
class(mtcars$vs)

Sirve para parsear una variable as.Lo_que quiero en que se convierta.
mtcars$vs = as.logical(mtcars$vs)
mtcars$am = as.logical(mtcars$am)

###    **CHUNK: Estructura del dataset del proyecto **
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

summary: función que nos va a mostrar un resumen del dataset que le mandemos.
transform: función para modificar los valores de un dataset.

Esta función me hace un resumen estadistico de un set de parámetros, minimo, cuartiles, promedio, maximo, d emi data set
summary(mtcars)

Con esto puedo guardar una transformación de una columna alojada en mntcars(wt)
mtcars.new<- transform(mtcars,wt=wt*1000/2)
Así puedo llamar a mi nueva "tabla"-
mtcars.new


Nota: Es como si realmente no hiciera una modificación de mi dataset original.
Si no como que R fuera un conjunto de transformaciones que puedo ejecutar 1 a 1, me guarda las variables después de ejecutarlas?

Como funcioan bien el hilo de ejecución de mis  scripts?

###    **CHUNK:Vectores**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Un vector es un ente matemático que se usa para guardar información de un mismo tipo, dentro de R se crean los vectores con la función c.

sum es una función que como su nombre lo indica, retorna la suma de los valores que le indiquemos.

num_horas_escribir = c(20,3,24,25,26)
num_horas_escribir = sum(num_horas_escribir)
num_horas_leer = c(20,3,24,25,34)
num_horas_leer = sum(num_horas_leer)
num_horas_leer
num_horas_totales = num_horas_leer + num_horas_leer
str(num_horas_totales)




###    **CHUNK:Matrices**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Una matriz debe tener mismo tipo de datos, por otro lado, un dataframe puede tener diferentes.
Para crear una matriz en R utilizaremos la función matrix cuyos argumentos son:

la información de los elementos.
nrow: número de filas.
ncol: número de columnas.
byrow: booleano para indicar si llenar la matriz por filas.
colSums es una función que por argumento recibe una matriz y te retorna la suma de los valores de sus columnas.

Cuando la tabla de n fialas y n columans posee el mismo tipo d datos son una matriz, si contiene diferentes tipos de datos es un dataframe.


dataset mtcar es dataframe no matriz. 


num_horas_escribir <- c(20,3,24,25,26)
num_horas_escribir <- sum(num_horas_escribir)
num_horas_leer <- c(20,3,24,25,34)
num_horas_leer <- sum(num_horas_leer)
num_horas_leer
num_horas_totales <- num_horas_leer + num_horas_leer
num_horas_totales
#Comentarios:
#Matriz
#Me intera el concepto de transpuestas.
#Para hacer algo en notación matricial
matrix_totales <- matrix(c(num_horas_escribir,num_horas_leer), nrow = 2 , byrow =TRUE)

#Declaro dos vectores, dias y tiempo

dias<- c( "L","M","W","J","V")
tiempo <- c("num_horas_escribir" ,"num_horas_leer" )

#sirve para darle nombres a mis columnas, a quie le digo que estos vengan de dias 
colnames(matrix_totales)<-dias
#sirve para darle nombre a las filas
rownames(matrix_totales) <- tiempo

matrix_totales
#

###    **CHUNK:Ejercicios con matrices**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
rbind: función para añadir una fila.

Reto: agrega una columna a nuestra matriz para indicar el día Sabado.

Para seleccionar rápidamente un elemento de una matriz solamente debemos indicar entre corchetes el número de la fila y de la columna.


###    **CHUNK:Operadores para comparar y ubicar datos **
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
En R cuentas con los operadores de comparación comunes como == o |, pero además cuentas con el operador:

%in% Que sirve para checar si un elemento se encuentra en el dataset
Para hacer una selección de elementos de un vector, matriz o data frame podemos usar la función subset.

Podemos renombrar una variable de nuestro dataset orangeec, para ello debemos tener instalado el paquete plyr. En caso de no tener el paquete instalado solamente corremos en la consola el código install.packages(“plyr”).

== igual
!= No igual. Diferente
< Menor que
..
!no
| o
%in% Que esté en el data set.

###  **CHUNK:Factores, listas y echar un vistazo al dataset**

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
head: es una función que nos retorna los primeros elementos de un dataset, por defecto nos retorna los primeros 6.
tail: función similar a head solamente que esta función nos retorna los últimos elementos.
Además de poder visualizar un dataset con str podemos instalar el paquete dplyr: install.packages(“dplyr”). Una vez instalado usamos la función glimpse.

Una lista es un vector genérico que puede contener objetos de todo tipo, en R para crear una lista solamente debes llamar a la función list y pasarle como argumentos los elementos.

Factor es un tipo de dato que tiene labebls.
Para armar un factor
palabra <- c ("x"....)

dplyer nosr permtie hacer glimpse,  muestra el data set es como str.

La lsita es un super objeto que nos permite meter lo que sea
1:8 significa 1 al 8.


mv <- 1:8
matrixm <- matrix(1:9,ncol=3)
mdf <-mtcars[1:4]

matrixm
mdf

#lista:
lista <- list(mv,matrixm, mdf)
lista


###    **BRICK:EDA: Exploratory Data Analysis**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Al momento de tener nuestro dataset es importante visualizarlos en alguna grafica antes de enfocarnos en las fórmulas estadísticas.
Pueden suceder casos donde datasets distintos muestran los mismos valores estadísticos, pero sus elementos en una gráfica son totalmente diferentes. Es por ello por lo que es importante visualizarlos antes.

Cuarteto de ascombe:
La importancia de visualizar lso daos antes de enfocarse en la estidistica.

El cuarteto de Anscombe comprende cuatro conjuntos de datos que tienen las mismas propiedades estadísticas, pero que evidentemente son distintas al inspeccionar sus gráficos respectivos.

https://es.wikipedia.org/wiki/Cuarteto_de_Anscombe


###  **CHUNK: Gráficas de dispersión e histogramas.**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Existen varios tipos de gráficas para visualizar la información al momento de hacer EDA:

Histograma:

    Sirve para ver la distribución de las frecuencias de una variable, es diferente a la gráfica de barras.
    debe ir pegadas las barras y va de menor a mayor.

Gráfica de dispersión:

    Los ejes solamente pueden ser valores numéricos y los puntos no se pueden unir.
    cruzamos vraibles continuas son numeros, no variables categoricas o nada de paalbras

Box plot:
    Nos muestra elementos como el mínimo, el máximo, el primer cuartil, la mediana y el tercer cuartil.

###  **CHUNK:Box Plot y su interpretación**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

NOTA: Es fácil confundir las interpretacions de los tipo de gráficos. Entender qué gráfico representa mis datos.

1. Recibo datos
2. Hago un EDA para visualiarlos como se ven.
3. Al ver la gráfica se pueden ver concentraciones de puntos, infiriendo si hay tendencias aparentes.
4. Decidimos ordenar de menro a myor, automáticamente tienes los minimos y máximos.
5. Con la mediana obtengo el 50% de cada parte, los que fueron menors y los que fueron mayors
6. Otengo el primer cuartil que es el 25% inferior, y obtengo el tercer cuartil que es 75% superior.

La mediana permtie realziar inferencias: El 50% inferior logro esto... el 50 superior logró esto.

Los 5 puntos clave en estadística descriptiva se pueden visualizar en el box plot:

Primer cuartil: es el piso de la caja o línea inferior.
Tercer cuartil: es el techo de la caja o línea superior.
Mediana: es la línea que se encuentra dentro de la caja. Q2
Mínimo: la extensión inferior de la caja.
Máximo: la extensión superior de la caja.


###  **CHUNK:EDA con dataset proyecto - Gráficas de dispersión.**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
ara realizar EDA con una gráfica de dispersión dentro de R debemos utilizar la función plot, los argumentos que debemos pasarle son:

la información en el eje X y Y.
xlab: título para el eje x.
ylab: título para el eje y.
main: título de la gráfica.


¿Pregunta cómo recibe los parámetros la función plot()?

https://bookdown.org/jboscomendoza/r-principiantes4/la-funcion-plot.html

#EDA para mtcars

plot(mtcars$mpg ~ mtcars$cyl, xlab= "Millas por galón" , ylab ="Cilindros",main ="Relación dilindros 
     y millas por galón")

#Relación caballos de fuerza por millas por galón

plot(mtcars$mpg ~ mtcars$hp, xlab= "Millas por galón" , ylab ="caballos de fuerza",main ="Relación dilindros 
     y millas por galón")

#EDA oraange
plot(orangeec$Unemployment ~ orangeec$Education.invest...GDP, xlab= "Inversión educación %PIB" ,
     ylab ="Desempleo",main ="Relación inversión en educación y desempleo")


#Aporte econocmia naranja PerCapita

plot(orangeec$GDP.PC ~ orangeec$Creat.Ind...GDP, 
     xlab= "aporte economia naranaja al PIB" ,
     ylab ="PIB percapita",
     main ="Relación economía naranaja PIB percápita")



###  **CHUNK:EDA con histogramas.**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Para realizar EDA con un histograma dentro de R debemos utilizar la función qplot, los argumentos que debemos pasarle son:

la información en el eje X.
geom: describir el tipo de gráfica que se va a imprimir.
xlab: título para el eje x.
main: título de la gráfica.
Además, podemos crear histogramas con el paquete ggplot2 para ello debemos instalarlo: install.packages(“ggplot2”).


install.packages("ggplot2")
library(ggplot2)

###  **CHUNK:EDA con dataset proyecto - histogramas - ggplot2**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Ver archivo de: /mnt/c/Users/USUARIO/alejandro-sin/Data_science/R/scripts/Hist_EconomiaNaranaja.R

¿Como hago Lables apra los gráficos?

###  **CHUNK: EDA con box plot- ggplot2**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

Para realizar EDA con un box plot dentro de R debemos utilizar la función boxplot, los argumentos que debemos pasarle son:

la información que vamos a explorar.
ylab: título para el eje y.
main: título de la gráfica.
También podemos usar ggplot2 para crear un Box Plot.

Outliers son valores muy salidos
Los boxplto usan variables categoricas en x numericas en y
as.factor me toma los valores de una columna y me los toma no como valroes si no como etiquetas

Cajas estiradas quiere decir que hay datos desviados del proemdio.
Cajas chatas, datos homogenoes.

###  **CHUNK:EDA con dataset proyecto - box plot- ggplot2 - dplyr**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Bloxplot vrua variable categorica con ub nnumero







###  **CHUNK:EDA con gráficas de dispersión con más de dos variables - ggplot2**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Ver archivo de ggplots

###  **CHUNK:Buscando correlaciones con pairs**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
La función pairs nos permite cruzar todas las variables del dataset a modo de tabla donde el eje x de una gráfica corresponde a la columna donde se encuentra y el eje y a la fila.

select: función para seleccionar variables o columnas.
filter: función para filtrar datos de un dataset, retorna las filas que pasen el filtro.

Podemos cruzar todas las variables frente a todas las variables del data Set, teniendo una matriz de todos los cruces.

, significa todas las observaciones., tiene notació slicdes. Serán las columnas

https://stackoverflow.com/questions/25721884/how-should-i-deal-with-package-xxx-is-not-available-for-r-version-x-y-z-wa

###  **CHUNK:Confirmando correlaciones con la función cor**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

La función cor nos retorna la correlación entre los datos. Recordemos que el valor de una correlación va de -1 a 1, si se acerca a 0 no hay correlación.

La correlación es entre dos valores va de -1 0 1  si se acerca a cero la correlación es nula, a 1 es positiva a -1 negativa.



###  **CHUNK:Protegiéndonos de los peligros del promedio.**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Podremos encontrar casos donde dos grupos de datos distintos tengan el mismo promedio, pero sus datos son muy diferentes uno del otro. No es lo mismo un grupo de datos donde su desviación es menor a 1, que aquel donde sus datos tienen una desviación de 4 o 6 puntos.

La formula del coeficiente de variación nos es útil al momento de evaluar estos casos:
(desviación estándar)/(promedio) * 100 = coeficiente

Si el coeficiente es mayor al 25% entonces los datos no son homogéneos, varían mucho.

Dentro de R podemos sacar la desviación estándar con la función sd y el promedio con mean.






###  **CHUNK:Eliminando los NA\'s para hacer los cálculos.**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Al momento de sacar el promedio de nuestro dataset orangeec encontramos variables que tienen valores NA, para que estos no afecten nuestro cálculo solamente debemos añadir como argumento na.rm=TRUE.


###  **CHUNK:Estadística y visualización aplicada a análisis de datos de mercadeo.**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
https://medium.com/@soniaardila1/c%C3%B3mo-escogemos-nuestra-nave-espacial-una-c%C3%B3smica-historia-de-mercadeo-e26f5599263d

###  **CHUNK:Generando tablas, filtrando y seleccionando datos - dplyr-Parte 1**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

###  **CHUNK:Conociendo R Markdown y organizando los hallazgos del análisis en un documento PDF**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Es momento de generar nuestro documento con todas las gráficas y observaciones que hemos realizado a nuestro dataset, para ello necesitamos instalar el paquete rmarkdown: install.packages(“rmarkdown”). y knitr

R Markdown nos permite generar archivos en formato HTML, PDF y Word. La mejor opción es trabajar en un formato HTML para compartirlo por internet y posteriormente convertirlo ya sea a PDF o Word.

Dentro de nuestro archivo de R Markdown iremos escribiendo con sintaxis de markdown el archivo y cuando escribamos código por si solo se va a ejecutar y añadir las gráficas o cálculos a nuestro archivo.



para ampliar mis conocimientos en r:
escribir funciones
limpair dsets
importar y leer data sets
amplair correlación y pasar a regresion lienal,
Mapas de Calor
Dashboards con shiny.

###  **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###  **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###  **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###  **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###  **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###  **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###  **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###  **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###  **CHUNK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

###    **BRICK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **BRICK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **BRICK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
###    **BRICK:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■



_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________

_________________________________________________
**CONCEPTO** :
_________________________________________________














■________________________________________________________________ break() ■





#### **PREGUNTAS:**
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■




* 
* 
* 


■________________________________________________________________ break() ■

#### **RESUMEN PARCIAL**:
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
```
<code>

```



■________________________________________________________________ break() ■
## EXÁMEN:
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
Antes de hacer el exámen, asegurence de saber estás preguntas sobre los Datasets mtcars y orangec:

En mi caso tenía todas las respuestas desordenadas de los ejercicios y en lo que las búsque perdí tiempo, debería estar en una guía antes del exámen.

El exámen evalua conocimientos de los datasets más que del mismo lenguaje. Así que podríamos decir que más del 50% es sobre los DataSets

¿Cuál es el máximo PIB Percápita en los paises de latam (GDP.PC )?


Al hacer un histograma de los cilindros de los carros, con un binwith de 1, vemos que hay más carros de…
Al hacer un histograma del aporte de la economía naranja al pib (Creat.Ind) con binwith de 1, vemos que hay más países que con la economía naranja aportan…

En un scatter plot (gráfica de dispersión) en donde relacionamos los caballos de fuerza (hp) en el eje X y el tiempo en recorrer un cuarto de milla (qsec) en el eje Y, en el dataset mtcars, los puntos parecen…


En el dataset orangeec, al usar pairs, vemos que en la relación entre el aporte de los servicios al pib (Services…GDP) y el PIB per cápita (GDP.PC), los puntos:



En la lectura vemos que cuando el tráfico al punto de venta aumenta
c

En el dataset mtcars, la correlación entre las variables cilindros (cyl) y caballos de fuerza (hp) es de:
0.8324475 b



Si hacemos dos box plot según el tipo de país (Strong_economy) para ver la penetración de internet en la población de sus países, veremos que…
b NO ---c


EDA (Exploratory data analysis) significa:
c

Para eliminar los N.A’s o missing values, después de la variable escribimos:
b NO--c
http://uc-r.github.io/na_exclude


Podemos dar un vistazo a un dataset usando…
b

En un scatter plot (gráfica de dispersión) en donde relacionamos la inversión en educación(Education.invest…GDP) en el eje X y el aporte de la economia naranja al pib (Creat.Ind…GDP) en el eje Y, en el dataset orangeec, coloreando los puntos según la variable Strong_economy, la cantidad de puntos rosados que aparecen son:

d 3

Al hacer un histograma de los cilindros de los carros, con un binwith de 1, vemos que hay más carros de…
c


El dataset mtcars…
c

Una variable nos ahorra tiempo porque…
b


Si al explorar las edades de los estudiantes de este curso, descubrimos que el tercer cuartil es 28, entonces diremos que:

a NO d 


El ambiente en donde escribimos el código (R Script) se encuentra en:

c


El peso (wt) en el dataset mtcars, es un dato de tipo…
d


¿Qué país o países aportan con su economía naranja más del 5% al PIB y además tienen una tasa de desempleo menor al 5%?
c NO--b


En el dataset orangeec, al usar pairs, vemos que en la relación entre el aporte de los servicios al pib (Services…GDP) y el PIB per cápita (GDP.PC), los puntos:
a


En la lectura vemos que cuando el tráfico al punto de venta aumenta

c

En un scatter plot (gráfica de dispersión) en donde relacionamos los caballos de fuerza (hp) en el eje X y el tiempo en recorrer un cuarto de milla (qsec) en el eje Y, en el dataset mtcars, los puntos parecen…
c

¿Cuál es el máximo PIB Percápita en los paises de latam (GDP.PC )?
c

Los scatter plots o diagramas de dispersión visualizan:
a

Cuando creamos un documento en R Markdown, el dataset que procesa R por default es
d

En el dataset orangeec, la correlación entre el crecimiento del pib de un pais (GDP.Growth…) y el aporte de la economía naranja al pib del país (Creat.Ind…GDP) es de:****
d NO --c

Al hacer un scatter plot con el dataset orangeec usando facet_wrap cruzando dos variables (numéricas) , al escribir al final facet_wrap(~Crecimiento_GDP), lo que veremos será:
c


Al hacer un diagrama de dispersión con las variables Aporte de economía naranja al PIB (Creat.Ind…en eje X) y crecimiento del pib del país (GDP Growth en eje y), la forma de los datos…
b NO... d

Para ubicar un dato dentro de una matriz, después de [ el primer número corresponde a…
d...NO recibe un vector  ---C NO ... b fila, columanmatriz[fila,columna]

https://bookdown.org/jboscomendoza/r-principiantes4/matrices-y-arrays.html

Al hacer un histograma del aporte de la economía naranja al pib (Creat.Ind) con binwith de 1, vemos que hay más países que con la economía naranja aportan…
b NO---d

correlacion mtcars cyl y hp
0.83

Cuando hacemos subset y usamos select, estamos
d


■________________________________________________________________ break() ■
#### **REFERENCIAS INTERESANTES**:
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

+ [Hipervínculo](url)
+ [Hipervínculo](url)
+ [Hipervínculo](url)
+ [Hipervínculo](url)
+ [Hipervínculo](url)
+ [Hipervínculo](url)

■________________________________________________________________ exit() ■


Operaciones con datos: vectores, listas y matrices
Vectores
Dentro de R podemos crear vectores a través de la función c().
Los vectores solamente pueden contener elementos del mismo tipo de variable, no puedes mezclar valores numéricos con texto dentro de un vector.
Para acceder a un elemento en particular puedes usar los corchetes e indicar el índice del elemento, dentro de R los índices comienzan en 1 en lugar de 0 como en otros lenguajes de programación.
Puedes eliminar un elemento anteponiendo signo de menos al índice de un elemento: c[-4]
Listas
Puedes crear listas a través de la función list().
A diferencia del vector, una lista permite almacenar diferentes elementos sin importar su tipo valor.
Para acceder a uno de los elementos debes usar el signo $.
Matrices
Las matrices son tablas que contienen filas y columnas del mismo tipo.
Puedes crear matrices a través de la función matrix() e indicarle el número de columnas de filas con los parámetros nrow y ncol.

Operaciones con datos: dataframe y ficheros

Dataframe
Un dataframe es una matrix donde podemos almacenar diferentes tipos de datos, es la estructura de datos que más utilizaremos.
Para crear un dataframe utilizaremos la función data.frame().
Podemos leer y asignar los datos de un fichero a un dataframe con la función read.csv().