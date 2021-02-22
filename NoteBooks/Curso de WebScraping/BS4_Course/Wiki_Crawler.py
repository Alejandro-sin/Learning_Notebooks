'''
Este código tiene como propósito crear un crawler que me adquiera datos de las páginas de wikipedia


0. Librerías
1. Defino un set para almacenar mis resultados únicos
2. Creo una función que me llame mi conjunto globl, me haga la solicitud HTTP,y la sopa.
3. Manejo las excepciones para poder que lo que no encuentre el siguiente requisito no sea un conflicto:

Se requiere de este scraper:

* Encabezado
* Encontrar todas las etiquetas 'p' e imprimir la primera etiqueta p encontrada.
* El hipervinculo de las etiquetas span.

4. Recorrer el objeto bs4 para encontrar todos los link d ela página y si no está en el pages() añadirlo.
5. Ejecutar recursivamente.

'''

import requests
import re
from bs4 import BeautifulSoup


pages = set()

def getLink(url):
    global pages
    html = requests.get("https://en.wikipedia.org{}".format(url))
    bs = BeautifulSoup(html.text, "html.parser")
    try:

        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0].get_text())

        # Le digo que primero me encuntre lo que tenga un id: ca-edit.
        # Le pido que me traiga la etiqueta span y navego hasta el valor del atributo.
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print("This page is missing something")

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                new_pages = link.attrs['href']
                print('▬'*20)
                pages.add(new_pages)
                getLink(new_pages)

getLink('')
