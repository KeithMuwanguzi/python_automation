import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/"

res = requests.get(url)

if res.status_code == 200:
    print("Continue with this")
    soup = BeautifulSoup(res.text,"html.parser")
    print(soup.prettify())
else:
    print("Just stop bro")