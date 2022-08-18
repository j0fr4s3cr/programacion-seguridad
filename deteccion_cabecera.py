import requests
import argparse
import sys

parse = argparse.ArgumentParser(description="Detector de cabeceras")
parse.add_argument('-t','--target', help="Dirección URL") 
parse = parse.parse_args()


def main():
    if parse.target:
        try:
            url = requests.get(url = parse.target)
            cabeceras = dict(url.headers)
            for cabecera in cabeceras:
                print(cabecera + ":"+ cabeceras[cabecera])
            
        except:
            
            print("Error al conectar con la URL")
    else:
        print("No hay objectivo definido")



if __name__ == '__main__':
    try:
        main()
        
    except KeyboardInterrupt:
        print("\n\nSaliendo...")
        sys.exit(0)


        
        