import socket
# import cv2
import numpy as np
import pickle

#Upload image
# img = cv2.imread('/path/to/image', 0)

#Turn image into numpy-array
arr = np.array([[1,2,3],[4,5,6]])

#Receiver ip
ip = socket.gethostname()

#Set up socket and stuff
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Loop through each array (5 for test)
for each in range(2):

    #Encode each array
    # msg = pickle.dumps(arr[each])
    msg = pickle.dumps(np.random.random((68, 1)))

    #Send msg to ip with port
    s.sendto(msg, (ip, 50000))

s.close()