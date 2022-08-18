import requests
from bs4 import BeautifulSoup
import sys


def main():
    url = "https://www.ho1a.com/"
    user_agent = {'User-Agent': 'Firefox'}  
    peticicion = requests.get(url = url, headers=user_agent)
    bsoup = BeautifulSoup(peticicion.text, 'html.parser')
    list_1 = []
    list_plugin = []
    
    for enlace in bsoup.find_all('link'):
        if '/wp-content/plugins/' in enlace['href']:
            href = enlace['href']
            href = href.split('/')
            posicion = href.index('plugins')
            plugin = href[posicion+1]
            list_1.append(plugin)
    for i in list_1:
        if i in list_plugin:
            pass
        else:
            list_plugin.append(i)
    for l in list_plugin:
        print(f"(+) Se encontro el plugin: {l}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
        