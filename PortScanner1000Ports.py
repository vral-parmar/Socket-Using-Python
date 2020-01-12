#Port Scanner That Scans The First 1000 Ports
#it will Written In Python 2.7 
#!/usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(100) #Timeout is set to 100 seconds by default


host = raw_input("[=>] Enter the IP address you want to scan: ")

def portScanner(port):
    if sock.connect_ex((host, port)):
        print "Port %d is closed" % (port)
    else:
        print "Port %d is open" % (port)

#Port range can be changed here
for port in range(20, 1000):
    portScanner(port)





