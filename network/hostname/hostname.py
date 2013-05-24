import socket

print(socket.gethostname())

for host in ['homer', 'www.163.com', 'www.python.org', 'nosuchname']:
    try:
        print('%s : %s ' % (host, socket.gethostbyname(host)))
    except socket.error, msg:
        print('%s : %s' % (host, msg))

print(socket.gethostbyaddr('82.94.164.162'))

from urlparse import urlparse
print(socket.getservbyname(urlparse('http://www.163.com').scheme))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 10001)
sock.connect(server_addr)

while True:
   data = raw_input('Input:')
   print(">> %s" % data)
   sock.send(data)

sock.close()

