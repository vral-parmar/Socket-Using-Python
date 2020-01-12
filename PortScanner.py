#Basic Port Scanner
#written in python 2.7 

#!/usr/bin/python  

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "Your Ip Goes Here" #enter Your Ip Here 
port = 80  #enter your port here

def portScanner(port):
    if sock.connect_ex((host, port)):
        print "Port %d is closed" % (port)
    else:
        print "Port %d is open" % (port)

portScanner(port)

