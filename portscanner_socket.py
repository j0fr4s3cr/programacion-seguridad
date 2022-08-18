import sys
import socket
from datetime import datetime
from colorama import Fore
def main():
    target = 'IP'
    print("-"*50)
    print(f"El target es: {target}")
    print(f"Inicio del escaneo PyNmap: {str(datetime.now())}")
    
    for port in range(1,81):
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target,port))
        
        if result == 0:
            print(f"El puerto: {Fore.GREEN} {port} open {Fore.WHITE} ")
        else:
           print(f"El puerto: {Fore.RED} {port} closed {Fore.WHITE} ") 
        sock.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
        
        