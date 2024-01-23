from urllib import response
import requests
from bs4 import BeautifulSoup


#url to the scrapped site
url = "https://docs.python.org/3/library/array.html#array.array.append"
response = requests.get(url)


if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content,'html.parser')
    
    print(soup.prettify())
else:
    print("This website denied you access to scrap it")