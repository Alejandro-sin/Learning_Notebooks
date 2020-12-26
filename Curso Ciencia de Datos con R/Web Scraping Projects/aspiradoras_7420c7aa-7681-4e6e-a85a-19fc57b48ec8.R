



library(rvest)
url<-"https://www.amazon.es/s?k=aspiradora&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
selector<-"#search > div.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.s-right-column.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(4) > div.s-result-list.s-search-results.sg-row > div:nth-child(3) > div > div > div > div:nth-child(2) > div.sg-col-4-of-12.sg-col-8-of-16.sg-col-16-of-24.sg-col-12-of-20.sg-col-24-of-32.sg-col.sg-col-28-of-36.sg-col-20-of-28 > div > div:nth-child(1) > div > div > div:nth-child(1) > h2 > a"
pagina<-read_html(url)
nodo<-html_node(pagina, selector)
nodo_text<-html_text(nodo)
nodo_links<-html_attr(nodo, "href")
nodo_links

urlcompleta<-paste0("www.amazon.es",nodo_links)
urlcompleta

#https://www.amazon.es/s?k=aspiradora&page=2&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1559659201&ref=sr_pg_2
#https://www.amazon.es/s?k=aspiradora&page=3&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1559659201&ref=sr_pg_3
library(stringr)
pag<-"s?k=aspiradora&page=2&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1559659201&ref=sr_pg_2"
lista_paginas<-c(1:10)
pag<-str_replace(pag, "page=2", paste0("page=",lista_paginas))
pag<-str_replace(pag, "sr_pg_2", paste0("sr_pg_",lista_paginas))
t
paginas<-paste0("https://www.amazon.es/", pag)

dameLinksPagina<-function(url){
  selector<-"div > div:nth-child(1) > div > div > div:nth-child(1) > h2 > a"
  pagina<-read_html(url)
  nodo<-html_nodes(pagina, selector)
  nodo_text<-html_text(nodo)
  nodo_links<-html_attr(nodo, "href")
  nodo_links
  
}
test<-dameLinksPagina(paginas[3])
linksAsp<-sapply(paginas, dameLinksPagina)
vlink<-as.vector(linksAsp)

vlinkAspiradora<-paste0("https://www.amazon.es/", vlink)
vlinkAspiradora


url<-"https://www.amazon.es/Cecotec-Conga-Duostick-Easy-Aspirador/dp/B01LYTA8KW/ref=sr_1_5?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=aspirador&qid=1558782933&s=gateway&sr=8-5"
nombre<-"#productTitle"
pagina_web<-read_html(url)
nombre_nodo<-html_node(pagina_web, nombre)
nombre_texto<-html_text(nombre_nodo)
nombre_texto

opiniones<-"#acrCustomerReviewText"
opiniones_nodo<-html_node(pagina_web, opiniones)
opiniones_texto<-html_text(opiniones_nodo)
opiniones_texto

precio<-"#priceblock_ourprice"
precio_nodo<-html_node(pagina_web, precio)
precio_texto<-html_text(precio_nodo)
precio_texto

tabla<-"#prodDetails > div.wrapper.ESlocale > div.column.col1 > div > div.content.pdClearfix > div > div > table"
tabla_nodo<-html_node(pagina_web, tabla)
tabla_tab<-html_table(tabla_nodo)
tabla_tab
class(tabla_tab)
val<-tabla_tab$X2
val
res_tabla<-data.frame(t(val))
res_tabla
tabla_name<-tabla_tab$X1
tabla_name
colnames(res_tabla)<-tabla_name
res_tabla
str(res_tabla)

resultado_aspiradoras<-c(nombre_texto, precio_texto, opiniones_texto, as.character(res_tabla$`Peso del producto`), as.character(res_tabla$Potencia), as.character(res_tabla$`Dimensiones del producto`), as.character(res_tabla$Volumen))


getArticulo<-function(url){
  pagina_web<-read_html(url)
  nombre_nodo<-html_node(pagina_web, nombre)
  nombre_texto<-html_text(nombre_nodo)
  nombre_texto
  
  opiniones<-"#acrCustomerReviewText"
  opiniones_nodo<-html_node(pagina_web, opiniones)
  opiniones_texto<-html_text(opiniones_nodo)
  opiniones_texto
  
  precio<-"#priceblock_ourprice"
  precio_nodo<-html_node(pagina_web, precio)
  precio_texto<-html_text(precio_nodo)
  precio_texto
  
  tabla<-"#prodDetails > div.wrapper.ESlocale > div.column.col1 > div > div.content.pdClearfix > div > div > table"
  tabla_nodo<-html_node(pagina_web, tabla)
  if(!is.na(tabla_nodo)){ #SI el nodo no esta vacio!!!
    tabla_tab<-html_table(tabla_nodo)
    tabla_tab
    val<-tabla_tab$X2
    res_tabla<-data.frame(t(val))
    tabla_name<-tabla_tab$X1
    colnames(res_tabla)<-tabla_name
  }
  col<-c("Peso del producto", "Dimensiones del producto", "Volumen", "Potencia")
  if( is.na(tabla_nodo)){ #Si tabla nodo esta vacia
    #Rellenar con campos vacio
    mitab<-data.frame(colnames(col))
    mitab<-rbind(mitab, c("-1", "-1", "-1","-1"))
    colnames(mitab)<-col
  }else{
    #Evaluar cada uno de los campos
    zero<-matrix("-1", ncol=4, nrow=1)
    dfzero<-as.data.frame(zero)
    colnames(dfzero)<-col
    dfzero
    peso<-as.character(res_tabla$`Peso del producto`)
    if(length(peso)==0) peso <- "-1"
    volumen<-as.character(res_tabla$Volumen)
    if(length(volumen)==0) volumen <- "-1"
    dime<-as.character(res_tabla$`Dimensiones del producto`)
    if(length(dime)==0) dime <- "-1"
    potencia<-as.character(res_tabla$Potencia)
    if(length(potencia)==0) potencia <- "-1"
    dfzero$`Peso del producto`<-peso
    dfzero$`Dimensiones del producto`<-dime
    dfzero$Volumen<-volumen
    dfzero$Potencia<-potencia
    str(dfzero)
    mitab<-dfzero
    colnames(mitab)<-col
  }
  articulo<-c(nombre_texto, as.character(mitab$`Peso del producto`[1]), as.character(mitab$`Dimensiones del producto`[1]), as.character(mitab$Volumen[1]),as.character(mitab$Potencia[1]), opiniones_texto, precio_texto)  
  articulo
  
}
#Probamos para uno
url<-vlinkAsp[1]
getArticulo(url)
res<-sapply(vlinkAsp,getArticulo)
resultado<-as.data.frame(t(res))
#"Nombre","Peso del producto", "Dimensiones del producto", "Volumen", "Potencia", "Opiniones", "Precio"
colnames(resultado)<-c("Nombre","Peso del producto", "Dimensiones del producto", "Volumen", "Potencia", "Opiniones", "Precio")
rownames(resultado)<-c(1:200)

#Obtenemos toda la caracterizacion de los articulos
res<-sapply(vlinkAsp,getArticulo)
#Generamos un dataframe con esa info
a<-do.call("rbind", res)
aspiradoras<-as.data.frame(a)
colnames(aspiradoras)<-c("nombre", "peso" , "dimensiones", "volumen","potencia", "opiniones", "precio")  
rownames(aspiradoras)<-c(1:200)
write.csv(aspiradoras, "/home/ines/platzi/dataAmazon2.csv")




