#Quotes to scrape
import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"

res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
quotes = soup.findAll('span',attrs={'class':'text'})
authors = soup.findAll('small',attrs={'class':'author'})

file = open('scrapped_data.csv','w')
writer = csv.writer(file)

writer.writerow(["QUOTES","AUTHORS"])

for quote, author in zip(quotes,authors):
    writer.writerow([quote.text,author.text])
file.close()
print('Data written')