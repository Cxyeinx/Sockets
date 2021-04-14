import socket


SERVER = "192.168.1.106"
PORT = 3333
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while True:
	message = input().encode("utf-8")
	client.send(message)

