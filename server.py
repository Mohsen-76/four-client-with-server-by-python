"""
written by : 
                    __                             __    __               _ 
   ____ ___  ____  / /_  ________  ____     ____ _/ /_  / /_  ____ ______(_)
  / __ `__ \/ __ \/ __ \/ ___/ _ \/ __ \   / __ `/ __ \/ __ \/ __ `/ ___/ / 
 / / / / / / /_/ / / / (__  )  __/ / / /  / /_/ / /_/ / /_/ / /_/ (__  ) /  
/_/ /_/ /_/\____/_/ /_/____/\___/_/ /_/   \__,_/_.___/_.___/\__,_/____/_/   
                                                                            
name of project : communication on server to 4 client
"""
from colorama import Fore,init
import socket
import os
import time
import sys
import threading
import random
from queue import Queue
init()

# variable
ip=''
port=0
server=None
client=None
addr=''

all_connection=[]

hello=['hello','hi','hey']
meeting=['good','great','fine','not bad']
good_bye=['bye','godbye','see you tommorow']

logo="""

███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
                                                 
"""
print(Fore.RED+logo)
time.sleep(0.1)
print('-----------------------------------------------')
time.sleep(0.1)
while True:
    try:
        print(Fore.YELLOW+'')
        ip = input("┌─["+"ENTER IP OF SERVER"+"""]
└──╼ """+"卐 ")
        if ip==None or ip=="" or ip=="\n":
            print(Fore.RED+'the ip is empty'.upper())
            continue
        # a.168.1.200
        condition=str(ip).split('.')
        for dot in condition:
            if not dot.isdigit():
                print(Fore.RED+'one of the octed is not correct'.upper())
                continue

        if len(condition)!=4:
            print(Fore.RED+'your ip is not correct '.upper())
            continue

        break

    except KeyboardInterrupt:
        sys.exit()    
    except:
        print(Fore.RED+'i cant get the ip'.upper())    


# print(ip)
time.sleep(0.1)
while True:
    try:
        print(Fore.YELLOW+'')
        port = input("┌─["+"ENTER PORT OF SERVER"+"""]
└──╼ """+"卐 ")
        if port==None or port=="" or port=="\n" or port=='0':
            print(Fore.RED+'the port is empty'.upper())
            continue
        if not port.isdigit():
            print(Fore.RED+'number of port is not number'.upper())
            continue
        port=int(port)
        if port<8000 and port >9000:
            print(Fore.RED+'number of port has to be between 8000 to 9000')
            continue


        break

    except KeyboardInterrupt:
        sys.exit()    
    except:
        print(Fore.RED+'i cant get the ip'.upper())  

print('-----------------------------------------------')
time.sleep(0.1)

 
try:
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,int(port)))
    server.listen(4)
    print(Fore.GREEN+'server is running on port : '.upper(),port)
except KeyboardInterrupt:
    sys.exit()    
except:
    print(Fore.RED+'i cant bind the server'.upper())    


def new_client_socket_handler(cli,addr):
    # while True:
    print('')
    print(Fore.YELLOW+'message from client '.upper(),' ',str(addr[0]))
    data=cli.recv(1234).decode()
    print(Fore.BLUE+data)
    if data in hello:
        cli.send(random.choice(hello).encode())
    elif data in good_bye:
        cli.send(random.choice(good_bye).encode())    
    elif data in ['how are you','how are you ?','how are you?']:
        cli.send(random.choice(meeting).encode())   
    elif data=='end':
        cli.send('end'.encode()) 
        cli.close()
    else:
        cli.send('ok'.encode())        

while True:
    print(Fore.MAGENTA+'---------------------------------------------')
    print(Fore.CYAN+'waiting for incoming connection'.upper())
    cli,addr=server.accept()
    cli.send('connect_seccesful'.encode())
    # start new client thread
    threading._start_new_thread(new_client_socket_handler,(cli,addr))
    

