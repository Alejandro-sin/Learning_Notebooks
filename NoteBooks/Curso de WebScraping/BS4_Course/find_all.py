from bs4 import BeautifulSoup
import requests as rq

URL= "https://en.wikipedia.org/wiki/Lists_of_writers"
response = rq.get(URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")


'''
Función find_all y find()

'''
#Puedo pasarle una lista de etiquetas para que las scrapee.
titles = soup.find_all(["h1","h2","h3"])


# Puedo buscar un conjunto de atributos especificos usando el atributo Keyword de la función
by_atributes = soup.find_all(id ="toc", class_="toc")


# Puedo hacer exactamente lo mismo usando un diccionario.
by_dict = soup.find_all("",{"id":"toc"})
print(by_dict)