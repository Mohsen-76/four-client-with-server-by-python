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



init()


# variable
ip=''
port=0
server=None
connection=None

logo="""

 ██████╗██╗     ██╗███████╗███╗   ██╗████████╗
██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝
██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║   
██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║   
╚██████╗███████╗██║███████╗██║ ╚████║   ██║   
 ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                              
"""
print(Fore.RED+logo)
time.sleep(0.1)
print(Fore.CYAN+'-----------------------------------------------')
time.sleep(0.1)
while True:
    try:
        print(Fore.YELLOW+'')
        ip = input("┌─["+"ENTER IP OF SERVER"+"""]
└──╼ """+"卐 ")
        if ip==None or ip=="" or ip=="\n":
            print(Fore.RED+'the ip is empty'.upper())
            continue
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
            print(Fore.RED+'number of port has to be between 8000 to 9000'.upper())
            continue

        break

    except KeyboardInterrupt:
        sys.exit()    
    except:
        print(Fore.RED+'i cant get the ip'.upper())  


time.sleep(0.1)
     
while True:
    try:
        print(Fore.CYAN+'-----------------------------------------------')
        connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connection.connect((ip,int(port)))
        print(Fore.GREEN+'i connected to server'.upper())
        print(Fore.GREEN+connection.recv(1234).decode())
        print(Fore.YELLOW+'')
        message=input("┌─["+"ENTER YOUR MESSAGE"+"""]
└──╼ """+"卐 ")
        connection.send(message.encode())
        data=connection.recv(1234).decode()
        print(data)
        if data=='end':
            print(Fore.RED+'connection finished'.upper())
            connection.close()
            break
        # connection.close()
    except:
        print(Fore.RED+'i cant connect to server'.upper()) 
        break