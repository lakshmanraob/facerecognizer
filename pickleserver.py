import socket
import numpy as np
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((socket.gethostname(), 50000))

while True:
    data, addr = s.recvfrom(4096)
    conv = pickle.loads(data)
    print(conv)
    #print np.fromstring(conv,dtype=int)
s.close()