from bs4 import BeautifulSoup
import requests as rq

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

Puedo usar el poder de las expresioens regulares  y pasarlas como argumentos en funciones de BS4.

'''



