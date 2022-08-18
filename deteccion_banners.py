import socket
import sys

def banner(ip,port):
    so = socket.socket()
    so.connect((ip,port))
    print(str(so.recv(1024))) 
      


def main():
    ip = "IP a escanear"
    port = 22   
    banner(ip,port)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
        
        