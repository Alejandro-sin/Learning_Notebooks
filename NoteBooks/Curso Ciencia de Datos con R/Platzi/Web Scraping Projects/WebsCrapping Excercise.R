#WEBSCRAPPING TUTORIAL WITH R.

library(rvest)

# Asigno espacio en memoria llamado URL

url_wiki <-"https://en.wikipedia.org/wiki/Web_scraping"
web_page <- read_html(url_wiki)
selectorFirstHeading <-"#firstHeading"
firstheading_node <- html_node(web_page, selectorFirstHeading)
Title_text <- html_text(firstheading_node)
#Webscrapping Title
Title_text


#I want to get Webscrapping definition.
selectorP <- "#mw-content-text > div > p:nth-child(4)"
definition_node <-html_node(web_page, selectorP)
definitionWS <- html_text(definition_node)
definitionWS



#Accedo al listado de la primera página de libros de webscrapping en Amazon.


#_______________________________Fragmento para acceder al link 


#Tengo una URL de búsqueda de libros
url_amazon <-"https://www.amazon.com/s?k=web+scraping&i=stripbooks-intl-ship&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=24E0BM0HKW3K&sprefix=web+scr%2Cstripbooks-intl-ship%2C411&ref=nb_sb_ss_organic-diversity_1_7"

#La ubico con un nodo, del que me interesa el atributo href que contiene el hipervínculo a mi x producto.
selectorPagination <-"#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(5) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(17) > span > div > div > ul > li.a-selected > a"

#Genero mi página web paseandola a un objeto XML
web_pageA <- read_html(url_amazon)

# Le paso la página XML y el selector para que me encuentre mi etiqueta.
pagination_node <- html_node(web_pageA,selectorPagination)
pagination_node

#Nos interesa tomar el atributo Href del nodo.
nodo_link <- html_attr(pagination_node,"href")
nodo_link

#Busco hacer un paste0 para tener la URL completa, de la url target de la que haré como tal el scrapping.
url_target <-paste0("www.amazon.com",nodo_link)

#Esto es el target unitario.
url_target


#_______________________________

#Hacer un listado o un vector de todos los articulos que queremos tener, para ellos jugamos con la paginación.

#El análisis que se hace es el siguiente:
#La página número 1 es donde está, y no muestra la page=1
  #https://www.amazon.com/-/es/s?k=web+scraping&i=stripbooks-intl-ship&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=24E0BM0HKW3K&qid=1591659472&sprefix=web+scr%2Cstripbooks-intl-ship%2C411&ref=sr_pg_1
#La pag 2, 3.... n y cambia el parámetro ref=sr_pg_2,3,4...
  #https://www.amazon.com/-/es/s?k=web+scraping&i=stripbooks-intl-ship&page=3&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=24E0BM0HKW3K&qid=1591659472&sprefix=web+scr%2Cstripbooks-intl-ship%2C411&ref=sr_pg_3

#Ahora debemos generar esos strings. Usamos la libreria strinr. Permite usar substrings, como nuestra urls.
library(stringr)

pag <-"s?k=web+scraping&i=stripbooks-intl-ship&page=2&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=24E0BM0HKW3K&qid=1591659472&sprefix=web+scr%2Cstripbooks-intl-ship%2C411&ref=sr_pg_2"

#Creamos un vector, lista que me guarda todos los enlaces de los substrings sutituidos.
lista_paginas <-c(1:7)

#Con funciones de string r emepzamoa a sustituir. page=2 y sr_pgm  por el contenido de lista paginas. Con replace
pag <- str_replace(pag,"page=2", paste0("page=", lista_paginas))
pag <- str_replace(pag,"sr_pg_2",paste0("sr_pg_",lista_paginas))

#De esta página tenemos todas las Sub URLS asociadas a un 
#vector es que sacamos los demás hipervínculos de los productos. Hay que completar la url con el componente https
pag

paginas <- paste0("https://www.amazon.com/-/es/", pag)
#Todas las páginas asociadas
paginas

#Haremos una función que recopile los link de cada una de los libros.
getLinkpage <- function(url){
  
  #Debemos depurar el selector con la parte que es comun Parece que tengo un problema con los selectores.
  selectorLink <-"div > div:nth-child(1) > div > div > div:nth-child(1) > h2 > a"
  
  #Genero mi página web paseandola a un objeto XML
  web_pageA <- read_html(url_amazon)
  web_pageA
  
  # AL usar html_Nodes quiero usar un solo nodo si no que quiero usar diferentes nodos.
  nodes <- html_nodes(web_pageA,selectorLink)
  nodes
  
  #Debo pasarlo a texto, para verlo.
  node_text <- html_text(node)
  node_text
  
  #Nos interesa tomar el atributo Href del nodo.
  nodo_links <- html_attr(node,"href")
  nodo_links
  
  #Todas las páginas asociadas con el paste0 para
  #paginas_link 


 
}

#Probamos la función: Tenemos como reuslta las sub URL que componen la página. Para hacer esto mismo por cada página usamos la función saply
test1 <- getLinkpage(paginas)


# Funciones que nos permiten aplicar una función a un conjunto de datos, usamos getLink a el conjunto de  datos que son los elementos d elas paginas 
# de paginación, saply nos permtie convertir de un vector a una matriz para luego tenerlo d euna manera limpia.


linkAsp <- sapply(paginas, getLinkpage)

# Me devuelve todos los links
linkAsp

# Las dimensiones son 16 *7 donde 7 son las páginas de mis libros.
class(linkAsp )
dim(linkAsp )


#Para trabajar de manera cómod requerimos trnaformar una matriz a un vector.
vlink <- as.vector(linkAsp)

#Nos devuelve 112 entradas  url que correpsonden a 122 libros de Websrapping.


vlinkAll<- paste0("https://www.amazon.com/-/es", vlink)
vlinkAll


#CARACTERISTICAS DEL PRODUCTO A SCRAPEAR

url<-"https://www.amazon.com/-/es/Web-Scraping-Python-Collecting-Modern/dp/1491985577/ref=sr_1_1?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=web+scraping&qid=1591732841&s=books&sr=1-1"
my_page <- read_html(url)
name_selector <- "#productTitle"
#nombre del libro
nombre_nodo <- html_node(my_page,name_selector)
name_text <- html_text(nombre_nodo)
name_text

#Descripción

descri_selector <-"#bookDescription_feature_div > noscript"
descri_nodo <- html_node(my_page, descri_selector)
descri_text <- html_text(descri_nodo)
descri_text


#Opiniones de clientes

opiniones_selector <-"#acrCustomerReviewText"
opiniones_nodo <- html_node(my_page, opiniones_selector)
opiniones_text<-html_text(opiniones_nodo)
opiniones_text


#Precio
precio_selector <- "#a-autoid-7-announce > span.a-color-base > span"
precio_nodo<-html_node(mypage, precio_selector)
precio_texto <- html_text(precio_nodo)
precio_texto


#Tablas
tabla_selector <- "#productDetailsTable"
tabla_nodo <- html_node(my_page,tabla_selector)
tabla_tabla <- html_table(tabla_nodo)
class(tabla_tabla)
tabla_vector <- as.matrix(tabla_tabla)
tabla_vector

#Debemos crear variable  colnames, varaibles 2 nraow

val <- tabla_tabla$X2
val




#Creamos un data frame para mostrar los libros por nombre, autor, año, precio y calificación.

wsDataframe <- data.frame()
