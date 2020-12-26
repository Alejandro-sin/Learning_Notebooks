'''


Women In Science
https://en.wikipedia.org/wiki/List_of_female_scientists_in_the_20th_century
El proósito de este ejercicio es extraer de la lsita de muejres en la ciencia según Wiki,
y posterr almacenamiento de esta extracción a un CSV, luego un análisis de datos con pandas
y responder la pregunta:

* ¿Cual es la curva de creciemiento de la presencia de la mujer en la ciencia?
* Ver por profesión


Women in Chemistry


'''


import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd


URL_ws = "https://en.wikipedia.org/wiki/List_of_female_scientists_before_the_20th_century"
URL_wch = 'https://en.wikipedia.org/wiki/Women_in_chemistry'

name = []
category =[]
profesion =[]
years =[]

# Primero hago las solicitudes con requests y creo mi sopa de HTML.
response_ws = rq.get(URL_ws).content
soup = bs(response_ws, 'lxml')


# Navego a través de  mi árbol del DOM.

# Categorías
category_selector = '#Antiquity'
category = soup.select(category_selector)


# Tengo al lista entera
'''

Hasta aquí tengo al lista entera, me sale todos los hipervínculos, pero con etiquetas  y me sale toda la fila junto con 
el hipervinculo

'''
name_list = soup.find_all('li')
limit_nl = len(name_list)
for n in range(0, limit_nl):
    childs = list(name_list[n].children)
    # print(childs)


# Extraigo Los nombres de una categoría mediante  selectores e hijos.

'''
Aquí tengo el inconveniente de que algunos resultados de la lista extraida son texto sin nada por dentro, 
sin etiquetas a, por lo que me presenta problemas. Pero me trae una lista de una sola categoria.

¿Puedo escribir código para que me traiga las lista de cada categoría?

'''
for len_ws in range(0, limit_nl):
    selector = f'#mw-content-text > div.mw-parser-output > ul:nth-child(8) > li:nth-child({len_ws}) > a'
    n = soup.select(selector)
    print(list(n))



