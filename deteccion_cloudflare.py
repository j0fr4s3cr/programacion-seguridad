import requests
import sys


def main():
    
    try:
        website = "URL"
        palabra = "cloudflare"
        url = requests.get(website)
        cabeceras = dict(url.headers)
        verificacion = False
        
        for cabecera in cabeceras:
            if palabra in cabeceras[cabecera].lower():
                verificacion = True
                break
            
        if verificacion == True:
            print("El sitio está protegido por CloudFlare")
        else:
            print("El sitio no está protegido por CloudFlare")
    except:
        print("Ocurrió un error al conectar con la URL")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
        
        