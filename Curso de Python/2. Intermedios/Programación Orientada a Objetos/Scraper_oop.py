from bs4 import BeautifulSoup
import requests



def making_soup(url):
    response = requests.get(url)
    html_text = response.text
    html_content = response.content
    soup = BeautifulSoup(html_text,'html.parser')
    return  print(soup.prettify())

making_soup("https://elciervoherido.wordpress.com/2017/05/07/cartas-a-un-joven-poeta-carta-7-rainer-maria-rilke/")