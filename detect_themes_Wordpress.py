import requests
import sys
from bs4 import BeautifulSoup, Comment
import time

def main():
    
    url = "URL"
    agent = {'User-Agent': 'Firefox'}   
    r = requests.get(url, headers=agent)
    soup = BeautifulSoup(r.text, 'html.parser')
    list_1 = []
    list_temas = []
    contador = 0
     
    for enlace in soup.find_all('link'):
        if '/wp-content/themes' in enlace['href']:
            contador+=1    
            res = enlace['href']
            res = res.split('/')
            if 'themes' in res:
                posicion = res.index('themes')
                list_1.append(res[posicion+1])
            for l in list_1:
                if l in list_temas:
                    pass
                else:
                    list_temas.append(l)
                    for lf in list_temas:
                        print(f"(+) Se encontro el tema: {lf}")
                        
                        break
                    
    if contador == 0:
        
        print('---- No se encontraron temas ---- \n Estamos analizando los comentarios, Espera un momento.... \n')
        time.sleep(3)
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        for c in comments:
            if '/wp-content/themes' in c:
                conten = c.extract()
                conten = conten.split('/')
                                    
                if 'themes' in conten:
                    pos = conten.index('themes')
                    list_1.append(conten[pos+1])
            for l in list_1:
                if l in list_temas:
                    pass
                else:
                    list_temas.append(l)
            for lf in list_temas:
                print(f"(+) Se encontro el tema: {lf}")
                sys.exit()
                            
                
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
        
        