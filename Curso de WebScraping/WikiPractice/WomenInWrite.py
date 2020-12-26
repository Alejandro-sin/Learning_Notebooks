'''

Mujeres que escribieron
https://en.wikipedia.org/wiki/List_of_women_writers

'''


import requests as rq
from bs4 import  BeautifulSoup
import pandas as pd

URL_wr = 'https://en.wikipedia.org/wiki/List_of_women_writers'
response = rq.get(URL_wr).content
soup = BeautifulSoup(response,'lxml')

