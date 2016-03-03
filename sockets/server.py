
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

s.bind((host, port))
s.listen(1)

print 'Waiting for a connection'
conn, addr = s.accept()
print 'Connected to', addr

data = conn.recv(1024)
print 'Received: %s' % repr(data)

print 'Sending msg back'
conn.send(data)

print 'Closing connection'
conn.close()
s.close()
