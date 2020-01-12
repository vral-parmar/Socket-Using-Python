#!/usr/bin/python3
#it will Written In Python 3.8 
import socket #import Require Package 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #carete instance
s.settimeout(50) #script timeout

host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)
