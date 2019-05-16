#  TCP client
import socket

target_host = 'www.google.com'
target_post = 80
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# AF_INET: use stander IPv4 or host
# SOCK_STREAM: this is a tcp client

# connect client-site
client.connect((target_host, target_post))
# send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
# receive some data
response = client.recv(4096)
print response
