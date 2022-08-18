import requests
from bs4 import BeautifulSoup
import sys


def main():
    
    url = "URL"
    cabeceras = {'User-Agent': 'Firefox'}
    r = requests.get(url, headers=cabeceras)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    for v in soup.find_all('meta', attrs={'name': 'generator'}):
        print(v['content'])
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
        