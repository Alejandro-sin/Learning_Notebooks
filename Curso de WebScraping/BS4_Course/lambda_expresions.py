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
Quiero recurperar toso lso tag que tienen exactamente dos valores. Con lambda functions puedo reemplazar
la sintaxis de BS4.

'''


a= soup.find_all(lambda tag: len(tag.attrs) == 2)
# print(a)


b= soup.find_all(lambda tag : tag.get_text() =='Or maybe he\'s only resting?' )
print(b)

# Lo anterior peude lograrse.

c= soup.find_all('', text='Or maybe he\'s only resting?')
print(c)