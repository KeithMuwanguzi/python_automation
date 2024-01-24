from pydoc import html
import requests
from bs4 import BeautifulSoup


#url to the scrapped site
url = "https://docs.python.org/3/library/array.html#array.array.append"
res = requests.get(url)


if res.status_code == 200:
    html_content = res.content
    soup = BeautifulSoup(html_content,'html.parser')
    
    text= soup.get_text()
    with open('text.txt','w') as text_doc:
        text_doc.write(text)
else:
    print("This website denied you access to scrap it")