import sys 
import telnetlib

HOST="python.org"
PORT = "443"
tn = telnetlib.Telnet(HOST,PORT)
msg = ("GET /index.html HTTP/1.1\nHost:"+HOST+"\n\n").encode('ascii')
tn.write(msg)
print(tn.read_all())
tn.close()
