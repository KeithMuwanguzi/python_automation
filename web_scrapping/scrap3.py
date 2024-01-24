#Quotes to scrape
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
quotes = soup.findAll('span',attrs={'class':'text'})
authors = soup.findAll('small',attrs={'class':'author'})

with open('text.txt','a') as dump:
    for quote, author in zip(quotes,authors):
        dump.write(f'{quote.text} by {author.text}\n')