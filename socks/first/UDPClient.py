# UDP client
import socket

target_host = '127.0.0.1'
target_port = 8080

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto('AAABBBBCCC', (target_host, target_port))
# access some data //because udp protocol don't have connection status so we use recvfrom() to replace connect()
data, addr = client.recvfrom(4096)

print data
