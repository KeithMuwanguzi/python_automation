import requests
from pydoc import html
from bs4 import BeautifulSoup
import time

def scrapAllHTMLContents(url):
    res = requests.get(url)
    if res.status_code == 200:
        content = res.content
        soup = BeautifulSoup(content,'html.parser')
        
        data = soup.prettify()
        with open('web.html','w') as des:
            des.write(str(data))
        print("Data Scrapped")
    else:
        print("No access to scrap this site")
        
def main():
    web_url = input("Enter a correct url to scrap:")
    scrapAllHTMLContents(web_url)
    
if __name__ == '__main__':
    print('--------------------------------------------------')
    time.sleep(2)
    print("----------------------Starting--------------------")
    time.sleep(2)
    print('--------------------------------------------------')
    time.sleep(2)
    main()