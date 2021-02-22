'''

Esto tiene como propósito generar un scraper general para wikipedia que me permita usarlo recursivamente
hasta que se dé una condición dada.

En este caso queremos que el scraper busque links de un articulo inicial
Seleccione un articulo aleatorio de  la lista retornada y llame recursivamente getLinks hasta
que paremos el programa o no encuentre ningun articulo en al nueva página.


1. Primero defino una función que me reciba URLS
2. Hacer el requests de forma tal que el string pasado esté formateado con el argumento de al función.
3. Hacer la sopa de bs4.
4. Retornar el conjunto de bs4 que me da los links





'''

import requests
from bs4 import BeautifulSoup
import re
import random

regex_wiki ="^(/wiki/)((?!:).)*$"

def getLinks(url):
    html = requests.get("https://en.wikipedia.org".format(url))
    soup = BeautifulSoup(html.text, "html.parser")
    return soup.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile(regex_wiki))

links = getLinks('/wiki/Kevin_Bacon')

print(links)

# Añado la parte aleatoria,  condicional y recursiva

while len(links) >0:
    # Creo una lista nueva  mediante la selección de un número aleatorio, entre 0 y el la cantidad de links
    # Y de ese subconjunto quiero llamar el método atributos para que me devuelva el valor del atributo href.
    new_article = links[random.randint(0,len(links)-1)].attrs['href']
    print(new_article)
    # Recursividad
    links = getLinks(new_article)

