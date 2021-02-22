'''


TEMA: Basicos
PROPÓSITO:

BeautifulSoup es una librería que sirve para sacar datos de un documento HTML y un XML.

Un HTML se enfoca en presentar los datos, un XML en tranferir los datos.
XML me permite tranferir datos entre diferntes paltaformas.


'''
from bs4 import BeautifulSoup

with open("index.html") as PATH:
    soup = BeautifulSoup(PATH, "html.parser")
    print(soup.find("h1"))
    print(soup.__doc__)
    print('■'*20)
    print(soup.handle_starttag.__doc__)
    hr = soup.handle_starttag('hr')
