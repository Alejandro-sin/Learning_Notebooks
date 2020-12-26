
import requests as rq
from bs4 import BeautifulSoup as bs

# JS source to scrape
URL = 'https://www.guru99.com/javascript-interview-questions-answers.html'
question_selector = "#g-mainbar > div:nth-child(1) > div > div > div > div > div > div:nth-child(3) > p:nth-child(6)"
answer_selector = "#g-mainbar > div:nth-child(1) > div > div > div > div > div > div:nth-child(3) > p:nth-child(8)"


# Get the data with requests

response = rq.get(URL).content
soup = bs(response,"html.parser")
title = soup.find_all("h1")
