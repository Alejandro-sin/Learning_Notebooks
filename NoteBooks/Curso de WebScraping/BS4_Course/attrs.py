from bs4 import BeautifulSoup
import requests as rq
import re

# Sandbox
URL = " http://www.pythonscraping.com/pages/page3.html"
TEST = "https://en.wikipedia.org/wiki/Lists_of_writers"
response = rq.get(URL)
response_test = rq.get(TEST)

html = response.text
soup = BeautifulSoup(html, "html.parser")

test_html = response_test.text
tsoup = BeautifulSoup(test_html, "html.parser")

'''
Uso de attrs tiene como propósito acceder a los atributos de mi etiqueta.

1. Quiero traer todos los hipervinculso de manera arbitraria de wipedia de la etiqueta a.
# Traigo todos las etiquetas a

s_tag = tsoup.find_all('a')
for link in s_tag:
    print(link)

2. Necesito decirle que si el atributo href está dentro del diccionario de atributos de mi objeto BS4
me devuelva el valor de ese atributo, en cuyo caso serán la URL

# Traigo todos las etiquetas a

s_tag = tsoup.find_all('a')
for link in s_tag:
    if 'href' in link.attrs:
        print(link['href'])
        
Notar que si quiero especificamente las URL que cumplen con alguna caracteristica requiero:

* Encontrar los patrones por los que `puede modelarse la usqueda d emi interés.

'''



'''
# Quiero extraer mediante una expresión regular solo los links de escritores

1. Expresión regular del link de mi interés

ejemplo: /wiki/List_of_Sudanese_writers
regex: \/wiki\/writers

2.  Debo acotar la busqueda, las etiquetas a de la página están dentro de un div
que tiene clase "div-col" y en general dentro d eun id= bodyContent que lso alberga a todos.
El patrón es que todas las listas de mi interés terminan en la palabra writers.

'''

regex = '\/wiki\/\w+writers'

for link in tsoup.find('div',{'id':"bodyContent"}).find_all('a', href= re.compile(regex)):
    if 'href' in link.attrs:
        print(link.attrs['href'])