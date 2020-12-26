'''

Para scrapear sitios difíciles requiero mantener una conexión mediante cookies.


¿Qué son lso cookies?


Cuando hago un logeo en una pagina, se crea un cookie para mantener el estado de log in


Averiguar el metodo sesion de request


'''

import requests as rq

from bs4 import BeautifulSoup
link = 'https://quotes.toscrape.com/login'



LOGGED_SELECTOR = '#case_login > h3'

def is_logged(html_source):
    soup = BeautifulSoup(html_source)
    elements = soup.select(LOGGED_SELECTOR)
    if len(elements) == 1:
        element = elements[0]
        if 'success' in element.get('class', []):
            return True
        else:
            return False
    elif len(elements) > 1:
        raise Exception('Something is wrong with the source')
    else:
        return False

