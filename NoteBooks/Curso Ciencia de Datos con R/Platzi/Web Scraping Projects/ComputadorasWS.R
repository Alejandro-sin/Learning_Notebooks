#PROBLEMAS ASOCIADOS POR RESOLVER DE ESTE PROYECTO:

#Al Ejectuarlo, me scrapeea datos repetidos, klas caracterisitca de un solo computador, no de todos
# Me trae solo los links de una pagina, la paginación no está recorreiendo todos los numeros
# Debe traer el procio y quitar la docluman de descripción y de Frecuencia, mostrar el nombre del producto.




library(rvest)

#Este chunk de código me scrapea el hipervinculo de un computador gamer en amazon, lo hace de solo 1 link.

url<- "https://www.amazon.com/s?k=portatil+gaming&i=computers-intl-ship&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2VF4481ASIQXS&sprefix=porta%2Ccomputers-intl-ship%2C221&ref=nb_sb_ss_organic-diversity_3_5" 
pag_amazon <- read_html(url)
selector_link_articulo <- "#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(5) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(2) > div > span > div > div > div:nth-child(2) > div.sg-col-4-of-12.sg-col-8-of-16.sg-col-16-of-24.sg-col-12-of-20.sg-col-24-of-32.sg-col.sg-col-28-of-36.sg-col-20-of-28 > div > div:nth-child(1) > div > div > div:nth-child(1) > h2 > a"
nodo <- html_node(pag_amazon, selector_link_articulo)
nodo_link <- html_attr(nodo,"href")
nodo_link

#para tener la URL completa uso paste0

urlCompleta <- paste0("www.amazon.com", nodo_link)
urlCompleta

#Diseccionando la paginación, al final de la URL  se puede apreciar la paginación de los enlaces
# s?k=portatil+gaming&i=computers-intl-ship&page=3&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2VF4481ASIQXS&qid=1591144219&sprefix=porta%2Ccomputers-intl-ship%2C221&ref=sr_pg_3
#" page ="n".....=sr_pg_1"
#".....=sr_pg_3"

#usamos library stringr, permite manipualr un substring
library(stringr)

#Hacemos el contandaor en función del numero de páginas que quiero recorrer, 
#hago una lista con un vector con todos los numeros que deben ir sustituidos del 1 al n.
pag <-"s?k=portatil+gaming&i=computers-intl-ship&page=3&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2VF4481ASIQXS&qid=1591144219&sprefix=porta%2Ccomputers-intl-ship%2C221&ref=sr_pg_3"
lista_pag <-c(1:10)
#Con funciones de stringr sustituimos lo que nos compete. En este caso page=n, le estamos diciendo que con replace en la pagina de amazon de mi interees
#Me tome de las url lo que es la paginación y me le pequegu el valor vector que es una lista del 1 al 10.
pag<- str_replace(pag,"page=3",paste0("page=",lista_pag))
pag<- str_replace(pag,"sr_pg_3",paste0("sr_pg_",lista_pag))
pag


#Una vez obtenida la paginación me interesa obtener los hipervínculos.Requiero añadirle  a todas las páginas la parte del protocolo https...

paginas<-paste0("https://www.amazon.com/", pag)
paginas

#Ahora requiero una función para recopilar los dodos de cada una de los articulos que deseo, computadoras, aspiradoras.


givemelinksPage <-function(url){
  
  #Debo remover del selector_link_articulo todo lo que sea contendio no comun, me interesa solo lo que me lleva a el factor común de dos selectores.
  selector_link_articulo <- "div > div:nth-child(1) > div > div > div:nth-child(1) > h2 > a"
  #Se usa nodes plural para poder obtener todos los links
  nodo <- html_nodes(pag_amazon, selector_link_articulo)
  nodo_link <- html_attr(nodo,"href")
  nodo_link
  
}
#Ejecturo un test de prueba
#Estoy asignando en test el resultado de mi función giveme... a la qu ele pasé las páginas[n]  con n correspondiente a la paginación
test <-givemelinksPage(paginas[0])
test

#Funciones sapply nos permite aplicar una función a un conjunto de datos, estamos aplicando givemelinksPgaes a las paginaciones
#saplly nos permite convertir un vector en una matriz

#Objeto con todos los links
linkCom <-sapply(paginas, givemelinksPage)
class(linkCom)
dim(linkCom)
#MUY IMPORTANTE: Las dimensiones son 14x10 14 filas 10 columnas. Para trabajar en una estructura de datos que podamos manipular debemos convertilar en un vector.
vlink<-as.vector(linkCom)
vlink

#El resultado son las 140 sub URLS a las que hay que hacerle un pasto0 con la dirrección principal.
vlinkCom <- paste0("https://www.amazon.com/", vlink)

#El resultado de este proceso es este vetor donde tenemos recopilados los hipervinculos asociados 
#a los proudctos de los que vamos a requerir información para analizar.
vlinkCom


#Obteniendo  los datos que requerimos del producto.


### Titles, Revies and Tags.

#This section  belongs to my selector choices  and targets.
url<- "https://www.amazon.com/-/es/Lenovo-Ideapad-i5-9300H-Processor-81LK00HDUS/dp/B07VC55LF5/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2VF4481ASIQXS&dchild=1&keywords=gaming+laptop&qid=1591144219&s=computers-intl-ship&sprefix=porta%2Ccomputers-intl-ship%2C221&sr=1-1"
selectorTitle <-"#productTitle"
selectorCustomerReviewText <- "#acrCustomerReviewText"
selectorTag <- "#acBadge_feature_div > div > span.ac-for-text > span > span > a"
selectorTableDet <-"#productDetails_techSpec_section_1"
pagina_web <- read_html(url)


#This chunk of code store the result of my function html_node on my variables
title_node <- html_node(pagina_web, selectorTitle)
CustomerReview <- html_node(pagina_web, selectorCustomerReviewText)
Tag <-  html_node(pagina_web, selectorTag)
Tag


#This chunk transform  my nodes on text.
title_text <- html_text(title_node)
CustomerReview_text <- html_text(CustomerReview)
Tag_text<- html_text(Tag)


#Report
title_text
CustomerReview_text
Tag_text


#Get my details of my article, a table.


TableDet_node <- html_node(pagina_web, selectorTableDet)
TableDetails <- html_table(TableDet_node)
TableDetails


#?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????LEER CON ATENCIÓN Y REPENSAR
#Una vez obtenido los datos ay que unificar en ununico vector o lista

#Creatmos dataframe val1 colnames val2 priemr arrow.

#Primer arrow.
val<-TableDetails$X2
val
class(val)

#Creamso dataframe resultado

#usa la transformada de la columna a vector fila
res_tabla <- data.frame(t(val))
res_tabla

#Colname la primera columna que teníamos en tabla.
tabla_name <-TableDetails$X1
colnames(res_tabla) <- tabla_name
res_tabla

#?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????



#Hay que limpiar los datos y meterlo en un único vector.
str(res_tabla)


#Todos los vaores son de tipo factor, hay que castearlas para meterlas en el vector. Las mias ya son caracteres

respuesta_lapVector <- c(title_text,CustomerReview_text, Tag_text, res_tabla$`Tamaño de RAM de la tarjeta gráfica`, res_tabla$`Velocidad de memoria`)
respuesta_lapVector


#Necesitamos automatizar el proceso, crear una función que me devuelva lo que estoy buscando

getArticle <-function(url){
  
  #print(url)
  
  selectorTitle <-"#productTitle"
  title_node <- html_node(pagina_web, selectorTitle)
  title_text <- html_text(title_node)
  title_text

  
  selectorCustomerReviewText <- "#acrCustomerReviewText"
  CustomerReview <- html_node(pagina_web, selectorCustomerReviewText)
  CustomerReview_text <- html_text(CustomerReview)
  CustomerReview_text
  
  selectorTag <- "#acBadge_feature_div > div > span.ac-for-text > span > span > a"
  Tag <-  html_node(pagina_web, selectorTag)
  Tag_text<- html_text(Tag)
  Tag_text
  

  #Table details: Aqui habrá que curbir las casuisticas para hacer el wscrapping más pro,
  #es decir parcene casos  en lso que los datos no vienen como  queremos.
  #Y como anticiparnos.
  #Evaluamos el caso donde la tabla venga vacía o el caso en que la tabla tega una longitud mayor a 0, 
  #en caso que no aparezca dejar por defecto NA o el valor por defecto que queremos en este caso -1

  selectorTableDet <-"#productDetails_techSpec_section_1"
  TableDet_node <- html_node(pagina_web, selectorTableDet)
  if(!is.na(tabla_nodo)){
  
    TableDetails <- html_table(TableDet_node)
    TableDetails
    val<-TableDetails$X2
    res_tabla <- data.frame(t(val))
    res_tabla
    tabla_name <-TableDetails$X1
    colnames(res_tabla) <- tabla_name
    res_tabla
    
  }
  
  col<-c("Tamaño de la pantalla", "Resolución de la pantalla", "Velocidad de memoria", "Tamaño de RAM de la tarjeta gráfica")
 
   if(is.na(res_tabla)){
    #No hay detalles todo a -1
    mitab <- data.frame(colnames(col))
    mitab <- rbind(mitab, c("-1","-1","-1","-1"))
    colnames(mitab)<-col
    
  }else{
    
    #Evaluar cada uno de los atributos-campos.
    zero<- matrix("-1", ncol = 4, nrow = 1) 
    dfzero <- as.data.frame(zero)
    colnames(dfzero) <-col
    dfzero
    
    tam_pantalla <- as.character(res_tabla$`Tamaño de la pantalla`)
    if(length(tam_pantalla)==0)tam_pantalla <- "-1"
    
    resolutionScreen <- as.character(res_tabla$`Resolución de la pantalla`)
    if(length(resolutionScreen)==0)resolutionScreen <- "-1"
    
    velocidadMem <- as.character(res_tabla$`Velocidad de memoria`)
    if(length(velocidadMem)==0)velocidadMem <- "-1"
    
    ram <- as.character(res_tabla$`Tamaño de RAM de la tarjeta gráfica`)
    if(length(ram)==0)ram <- "-1"
    
    #Habien evaluado los atributos, lo asignamos a las variables del dtframe.

    dfzero$`Tamaño de la pantalla`<-tam_pantalla
    dfzero$`Resolución de la pantalla`<-resolutionScreen
    dfzero$`Velocidad de memoria`<-velocidadMem
    dfzero$`Tamaño de RAM de la tarjeta gráfica`<-ram
    
    #devolvemos mitab
    mitab<-dfzero
    colnames(mitab) <-col
 
  }

  # Creamos el vector articulo resultadoa para cada uno de nuestroc computadores.
  
    articulo <-c(title_text,CustomerReview_text,  Tag_text, as.character(mitab$`Tamaño de la pantalla`[1]),  as.character(mitab$`Resolución de la pantalla`[1]),  as.character(mitab$`Velocidad de memoria`[1]), as.character(mitab$`Tamaño de RAM de la tarjeta gráfica`[1]) )
    articulo
  
}

res <- getArticle(vlinkCom[3])
resultado_datos <-sapply(vlinkCom, getArticle)
resultado_datos

#Quiero la matriz inversa para ver como se ve, cambiando filas por columnas, por lo que seria la trasneouesta.
res <-t(resultado_datos)
View(res)

#Creamos un data frame y podremos maniular los nombres de las filas y columnas
miscomputadoras <- as.data.frame(res)
colnames(res)<-c("Nombre", "Descripción", "Calificaciones", "Categoría", "Tamaño_Pantalla", "Resolución", "Memmoria Ram")
rownames(res)<-c(1:150)
View(res)


a<-as.factor(c("12","22","32")) 
as.numeric(a)
a

