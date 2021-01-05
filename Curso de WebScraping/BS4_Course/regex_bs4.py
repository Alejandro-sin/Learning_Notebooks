from bs4 import BeautifulSoup
import requests as rq
import re

#Sandbox
URL= " http://www.pythonscraping.com/pages/page3.html"
TEST= "https://en.wikipedia.org/wiki/Lists_of_writers"
response = rq.get(URL)
response_test = rq.get(TEST)

html = response.text
soup = BeautifulSoup(html, "html.parser")

test_html = response_test.text
tsoup = BeautifulSoup(test_html,"html.parser")


'''
Muchas ocasiones es necesario no depender de las posiciones en el layout
de lo que busco extraer, o a veces mediante solo los atributos, puedo traer cosasa que no me interersan.
Para traer lo que quiero busco patrones.
 
Ejemplo: 

<img src="../img/gifts/img3.jpg">

El patrón de esta etiqueta en términos de regex dice:

\.\.\/img\/gifts\/img.*\.jpg

Lo que estoy haciendo es que uso re para compilar una expresión regular, lo uqe es pasado como un valor en un diccionario de llave src.
src, hace referencia al atributo source de la etiqueta img.
BS4 me deuvele un objeto conjunto itereable.

'''


images = soup.find_all('img',{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
print(type(images))
for image in images:
    print(image['src'])
