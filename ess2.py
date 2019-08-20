# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:46:18 2019

@author: Rapha
"""

import socket
host, port = ('',5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
o=False
while o==False:
    try:
        o=True
        socket.bind((host, port))
    except: 
        o=False
    finally:
        if(o==True):
            o=True
        

print("le serveur est dÃ©marrÃ©!")
#face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt.xml')
#recognizer = cv2.face.LBPHFaceRecognizer_create()    
socket.listen(5)
conn, adress = socket.accept()
print("en Ã©coute")
data= conn.recv(2048)
socket.close()
with open("im.png", "a")as fic:
    fic.write(str(data))