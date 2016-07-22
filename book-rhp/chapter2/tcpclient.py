#!/usr/bin/python

import socket as s

tgt_host = "0.0.0.0"
tgt_port = 9999

cli = s.socket(s.AF_INET, s.SOCK_STREAM)
cli.connect((tgt_host, tgt_port))
#cli.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
cli.send("odin, dva, tri, chetiruyi")

res = cli.recv(4096)
print res

cli.close()
