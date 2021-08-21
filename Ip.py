import socket
import sys

print ("Enter your DNS or Target: ")

hostname = input()

ip = socket.gethostbyname(hostname)

print ('Host Name is: ', hostname, '\n' 'Target Ip is: ',ip)

sys.exit()
