from pydoc import html
from urllib import response
import requests
from bs4 import BeautifulSoup


#url to the scrapped site
url = "https://docs.python.org/3/library/array.html#array.array.append"
response = requests.get(url)


if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content,'html.parser')
    
    # html_data = soup.prettify()
    # with open("web_data.html",'w') as file:
    #     file.write(str(html_data))
    
    text= soup.get_text()
    with open('text.txt','w') as text_doc:
        text_doc.write(text)
else:
    print("This website denied you access to scrap it")