import subprocess
import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Indica el sitio web \n (Ejemplo: http://www.google.com)")
parser = parser.parse_args()


def main():
    if parser.target:
        subprocess.run("wad -u "+parser.target + "> tecnologias.txt",shell=True)
        file = open('tecnologias.txt','r')
        tecnologias = file.read()
        tecnologias = tecnologias.split("[")
        tecnologias = tecnologias[1].split("]")
        tecnologias = tecnologias[0]
        tecnologias = tecnologias.split('{')
        
        
        for tecnologia in tecnologias:
            nuevo = tecnologia.replace('\n','')
            nuevo = nuevo.replace('            ','')
            nuevo = nuevo.replace('"','')
            nuevo = nuevo.split('}')
            nuevo = nuevo[0]
            nuevo = nuevo.replace(',','\n')
            print(nuevo)
            print("-"*50)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
        
