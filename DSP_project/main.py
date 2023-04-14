
import socket
import matplotlib.pyplot as plt
import numpy as np

UDP_Ip = "10.10.10.15"
UDP_Port = 41000

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_Ip,UDP_Port)) 

data_final = []

frames = 100
while(True):
	data,add = sock.recvfrom(2020)
	print("got:",len(data),add)
	with open("dump.txt","a+b") as fp:
		fp.write(data)
	
#data_final.append(data)
	frames = frames - 1
	if (frames==0):
		break

	print(frames)

print(data_final)
	
#plt.plot(data_final)
#plt.show()
