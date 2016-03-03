
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

s.connect((host, port))
s.send(b'Hello world!')

data = s.recv(1024)
print 'Received:\n%s' % repr(data)

print 'Closing connection'
s.close()
