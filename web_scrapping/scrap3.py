#Quotes to scrape
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
quotes = soup.findAll('span',attrs={'class':'text'})
authors = soup.findAll('small',attrs={'class':'author'})

for quote in quotes:
    print(quote.text)
    
for author in authors:
    print(author.text)