import sys
import json
import requests
from bs4 import BeautifulSoup
import os

def main():
    url = "URL"
    
    try:
        peticion = requests.get(url+'/wp-json/wp/v2/users',timeout=5)
        with open('json.txt','wb') as f:
            f.write(peticion.content)
        with open('json.txt','r') as json_file:
            for u in json.loads(json_file):
                user = u['slug']
                print(user)
        
       
    except requests.exceptions.ConnectionError as e:
        print("Error:")
        
       
        
            
        

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    