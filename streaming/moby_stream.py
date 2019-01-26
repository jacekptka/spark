from socket import *
import time

mobyD = list()
with open("MobyDick.txt", 'r') as MD:
	for line in MD:
		mobyD.append(line)

HOST = 'localhost'
PORT = 9999
ADDR = (HOST, PORT)
tcpSock = socket(AF_INET, SOCK_STREAM)
tcpSock.bind(ADDR)
tcpSock.listen(5)


while True:
	c, addr = tcpSock.accept()
	print('got connection')
	for line in mobyD:
		try:
			c.send(line.encode())
			time.sleep(1)
		except:
			break
	c.close()
	print('disconnected')
