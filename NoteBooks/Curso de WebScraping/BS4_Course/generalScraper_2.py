'''

Esto tiene como propósito generar un scraper general para wikipedia que me permita usarlo recursivamente
hasta que se dé una condición dada.

En este caso queremos que el scraper busque links de un articulo inicial de  la lista retornada y
llame recursivamente getLinks sin que los links se repitan hasta
que paremos el programa o no encuentre ningun articulo en al nueva página.


1. Primero  defino un conjunto vació para almacenar mis links no repetidos.
2. Hago una función getLinks() que reciba las url
3. Hacer el request y la sopa
4. iterar a traves de la lista de links (objeto bs4) y generar un condicional:
4.1 Si el atributo href de los links no está en el conjunto definido inicialmente entonces es una
nueva página.
5. Anexo esa página a mis conjuntos, y ejecuto recursivamente.

'''


import requests
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(url):
    global pages
    html = requests.get("https://en.wikipedia.org{}".format(url))
    html_text = html.text
    s = BeautifulSoup(html_text, "html.parser")
    for links in s.find_all('a', href = re.compile("^(/wiki/)")):
        if 'href' in links.attrs:
            if links.attrs['href'] not in pages:
                new_pages = links.attrs['href']
                print(new_pages)
                pages.add(new_pages)
                getLinks(new_pages)

getLinks('')