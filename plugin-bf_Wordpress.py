import requests
import sys
from os import path

def main():
    
    
    if path.exists('wp-plugins.txt'):
        file = open('wp-plugins.txt', 'r',encoding='utf-8')
        file = file.read().split('\n')
        lista = []
        url = "URL"
        
        for plugin in file:
            peticion = requests.get(url = url+'/'+plugin)
            print("(-) Trying "+peticion.url)
            
            if peticion.status_code == 200:
                print("(+) Se encontro el plugin: "+plugin)
                posicion = peticion.url.index('plugins')
                plugins_encontrado = peticion.url[posicion+1]
                lista.append(plugins_encontrado)
        for i in lista:
            print(f"(*) Se encontro el plugin: {i}")
            
                
    else:
        print("Error: No se encontro el archivo wp-plugins.txt")  

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

