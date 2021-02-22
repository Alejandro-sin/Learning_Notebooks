# Obetener lso datos de lo s jugaros
#https://www.laliga.com/laliga-santander

#https://www.laliga.com/estadisticas

library(rvest)
library(rjson)

clubs_list_url <- 'https://www.laliga.com/laliga-santander/clubes'
clubs_list_page <- read_html(clubs_list_url)
json_data <- html_node(clubs_list_page, '#__NEXT_DATA__')
json_data_value <- html_text(json_data)
teams_data <- fromJSON(json_data_value)

getLink <- function (lista) lista$slug

teams_urls <- lapply(teams_data$props$pageProps$teams, getLink)
teams_urls <- paste0('https://www.laliga.com/clubes/', teams_urls)

getTeamMembers <- function(team_url) {
  team_page <- read_html(team_url)
  player_links <- html_nodes(team_page, 'a[href^="/jugador/"]')
  player_urls <- html_attr(player_links, 'href')
  player_urls
}

members <- sapply(teams_urls, getTeamMembers)
b<-as.data.frame(unlist(members))
b[] <- Map(paste0, 'https://www.laliga.com',b)
b<-as.vector(unlist(b))
getJugador<-function(url){
  library(rvest)
  pagina_web<-read_html(url)
  #Nombre del jugador
  nombre<-"#__next > div.styled__SinglePlayerWrap-sc-4onsy-3.JWsgI > div.styled__Container-rwa3kw-0.styled__SinglePlayerBasicDataWrap-rwa3kw-1.jOrlgm > div.styled__PlayerNameArea-rwa3kw-2.hinFoe > div.styled__PlayerName-rwa3kw-5.ciFBaS > div.styled__PlayerNameTxt-rwa3kw-6.ijdLRB > div.styled__FirstName-rwa3kw-9.iOfZYb > p"
  nombre_nodo<-html_node(pagina_web, nombre)
  nombre_texto<-html_text(nombre_nodo)
  nombre_texto
  #Peso
  peso<-"#__next > div.styled__SinglePlayerWrap-sc-4onsy-3.JWsgI > div.styled__Container-rwa3kw-0.styled__SinglePlayerBasicDataWrap-rwa3kw-1.jOrlgm > div.styled__PlayerDataArea-rwa3kw-4.eFwlEv > div.styled__TableData-rwa3kw-13.gQCPet > div.styled__TableDataCell-rwa3kw-14.kkAyOI.cell-weight > div > div.styled__TableDataContent-rwa3kw-17.dblPfO > p"
  peso_nodo<-html_node(pagina_web, peso)
  peso_texto<-html_text(peso_nodo)
  peso_texto
  #Altura
  altura<-"#__next > div.styled__SinglePlayerWrap-sc-4onsy-3.JWsgI > div.styled__Container-rwa3kw-0.styled__SinglePlayerBasicDataWrap-rwa3kw-1.jOrlgm > div.styled__PlayerDataArea-rwa3kw-4.eFwlEv > div.styled__TableData-rwa3kw-13.gQCPet > div.styled__TableDataCell-rwa3kw-14.kkAyOI.cell-height > div > div.styled__TableDataContent-rwa3kw-17.dblPfO > p"
  altura_nodo<-html_node(pagina_web,altura)
  altura_texto<-html_text(altura_nodo)
  altura_texto
  datos<-c(nombre_texto,peso_texto,altura_texto)
  datos
}
b<-head(b,20) #Esta parte indica que usaremos solo 20 links de los 605
jugadores <- sapply(b, getJugador)
jugadores<-t(jugadores)
colnames(jugadores)<-c("Nombre","Peso","Altura")
jugadores
write.csv(jugadores,"jugadores.csv")
