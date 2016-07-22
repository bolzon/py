#!/usr/bin/python

import socket as s
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print "[*] server listening on %s:%d" % (bind_ip, bind_port)

def hnd_client(cli_sock):
  req = cli_sock.recv(1024)
  print "[*] received: %s" % req
  cli_sock.send("bonjour!")
  cli_sock.close()

while True:
  client, addr = server.accept()
  print "[*] conn accepted from %s:%d" % (addr[0], addr[1])
  cli_handler = threading.Thread(target=hnd_client, args=(client,))
  cli_handler.start()
