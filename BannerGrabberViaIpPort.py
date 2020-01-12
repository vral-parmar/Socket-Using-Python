#!/usr/bin/python3
# Written In Python 3.8
import socket #import require Package

def banner(ip, port): 
    s = socket.socket() #create Instance
    s.connect((ip, int(port))) #connect With Socket
    s.settimeout(150) #timeout in second
    print(s.recv(1024)) #maximum Size Will be transfered 

def main(): #to get user input
    ip = input("Please enter an IP Address : ")
    port = str(input("Please enter the port Address: "))
    banner(ip, port)

main() 
