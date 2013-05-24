import socket

sock = socket.create_connection(('127.0.0.1', 10001))

while True:
	data = raw_input('input:')
	if data:
		sock.sendall(data)
		print('>> %s' % (data))

sock.close()

