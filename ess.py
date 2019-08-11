# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:44:21 2019

@author: Rapha
"""
import cv2
import socket

cap=cv2.VideoCapture(0)  
while True:
    cam=(0)
    if(cam is not -1):
        ret, frame = cap.read()    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        host, port = ('localhost',5566)
        data=(str(gray))
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:        
            o=False
            while o==False:
                try:
                    print("o")
                    print(o)            
                    socket.connect((host, port))
                    o=True
                except :
                    print("except")
                    o=False
                finally:
                    if(o is not False):
                        o=True
           
            data = data.encode("utf8")
            socket.sendall(data)
        except ConnectionRefusedError:
            print("Error no connection")
        finally:        
            socket.close()                  