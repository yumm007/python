import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 10001)
sock.bind(server_addr)
sock.listen(1)
conn, client_addr = sock.accept()

while True:
	data = conn.recv(10)
	if data:
		print('<< %s' % (data))
	else :
		print('exit')
		break;

conn.close()

