import socket


PORT = 3333
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


server.listen()
print(f"[LISTENING] Server is listening on {SERVER}")

conn, addr = server.accept()
while True:
	msg = conn.recv(1024).decode("utf-8")
	print(f"Received: {msg}")
