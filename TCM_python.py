import sys
from datetime import datetime
import socket

#translate hostname to target ip 
if len(sys.argv)==2:
    target=socket.gethostbyname(sys.argv[1])#translates host name to ipv4 address
else:
    print("Invalid Syntax:exceeds arguement limit")
    print("Syntax:python <script name> <ip adress>")
    
#starting banner
print("-"*50)
print(f"Scanning on target:{target}")
print("Scanning started at:"+ str(datetime.now()))
print("-"*50)

#here is the real port scanning part
try:
    for port in range(50,91):
        socket1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=socket1.connect_ex((target,port))
        if result == 0:
            print(f"port {port} is open on {target}")
        socket1.close()
        
except KeyboardInterrupt:
    print("\nForce exit by keyboard interrupt")
    sys.exit()

except socket.gaierror:
    print("\nHost cannot be resolved")
    sys.exit()

except socket.error:
    print("\nCould not connect to the server")
    sys.exit()
    
