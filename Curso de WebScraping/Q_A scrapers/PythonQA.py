

import requests as rq
from bs4 import BeautifulSoup

URL = 'https://www.edureka.co/blog/interview-questions/python-interview-questions/'
URL_oop = ' https://www.edureka.co/blog/interview-questions/oops-interview-questions/'

response = rq.get(URL)
content = response.content
soup = BeautifulSoup(content, 'lxml')

#Uso selectores para scrapear

selector_css = "body > section.blog-body > div > div > div.col-xl-9.col-lg-9 " \
               "> div.blog-content.mt-md-4.mt-lg-4.mt-xl-4.color-4a " \
               "> h2:nth-child(9) > span > strong"

selection = soup.select(selector_css)
print(selection)