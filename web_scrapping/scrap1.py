from pydoc import html
import requests
from bs4 import BeautifulSoup


#url to the scrapped site
url = "https://docs.python.org/3/library/array.html#array.array.append"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
    
methods = soup.findAll('dl',attrs={'class':'py method'})


for method in methods:
    print(method.text)