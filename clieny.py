import numpy as np
import cv2
import time
import socket
import socket_client
from PIL import Image
import pickle
import pyaudio
print("start client")
x2=-660
y2=-660
id2_=(-1)
_id=(-1)
repeat=(0)
number=(0)
face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt.xml')

black_color=[0,0,0]
red_color=[255,0,0]
blue_color=(89,152,255 )
white_color=(250,250,250)
gold_color=(255,215,0)
green_color=(0,255,0)

with open("setting.txt", "r")as fic:
    setting_set=fic.read()

if(setting_set==""):
    print(" before using we need to do some settings")
    print(" it will take less than a minute")
    import setting
    setting.menu()
if(str(setting_set) is not " "):
    ip_find=(setting_set.find("ip:"))
    ip1=(setting_set[ip_find:])
    ip1_find=(ip1.find("/"))
    ip=(ip1[:ip1_find])

    
    
cap=cv2.VideoCapture(0)  
cam=(setting_set.find("cam=yes"))
while True:
    if(cam is not -1):
        ret, frame = cap.read()    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
           
        data2_cond=False
       
       
        data=("")
        face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("trainner.yml")
          
        
       
        
        
        data2_con=False
        for(x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]     
            
            id_=("undifind")
            wolf_position=("undifind")
            id_, conf= recognizer.predict(roi_gray)        
            if conf>=45 and conf<=85:
                id2_=id_
                print("_____________id________2")
                print(id_)
            
            with open("id_name.txt", "r")as fic:
                id_name=(int(fic.read())+1)
            id_name_img=(str(id_name))
            if(id_=="undfind"):
                img_item=("image/ima"+"1"+"0.png")
                cv2.imwrite(img_item, roi_gray)
                cap=cv2.VideoCapture(0)
                ret, frame = cap.read()
                img_item= ("c:/user/rapha/onedrive/desktop/face/image/ima"+id_name_img+"1.png")
                cv2.imwrite(img_item, roi_gray)
                cap=cv2.VideoCapture(0)
                ret, frame = cap.read()
                img_item= ("image/ima"+id_name_img+"1.png")
                cv2.imwrite(img_item, roi_gray)
                cap=cv2.VideoCapture(0)
                ret, frame = cap.read()
                img_item= ("image/ima"+id_name_img+"2.png")
                cv2.imwrite(img_item, roi_gray)
                number_img=(0)
                if(int(id_name_img)==int(id_name_img)):
                    x_train=[]
                    y_labels=[]
                    number_img=(0)
                    while (int(number_img)<3):
                        path=("image/ima"+str(id_name_img)+str(number_img)+".png")
                        number_img+=1
                        pil_image = Image.open(path).convert("L")
                        image_array = np.array(pil_image, "uint8")
                        print(image_array)
                        faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
                        for(x,y,w,h) in faces:
                            roi = image_array[y:y+h, x:x+w]
                            x_train.append(roi)
                            y_labels.append(id_)
                            #print(y_labels)
                            #print(x_train)
                            
                            with open("labels.picle", 'wb')as f:
                                    pickle.dump(label_ids, f)
                            recognizer.train(x_train, np.array(y_labels))
                            recognizer.save("image/trainner212.yml")
    
                with open("id_name.txt", "w")as fic:
                    fic.write(id_name_img)
            id__find=(setting_set.find("#"+str(id_)+"=="))
            print("id__find")
            print(id__find)
            print("#"+str(id_)+"==")        
                        
                        
                            
                    
            if(id_ =="undifind"):
                print("x"+str(x)+"y"+str(y))
                
            
                        
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
          
            if(data2_con==False):
                data2=("<c>"+str(x)+"<c>"+str(y)+"<c>"+str(w)+"<c>"+str(h)+"<c>ip"+ip+"<c>"+str(id_))
            if(data is not data2):
                data=("<c>"+str(x)+"<c>"+str(y)+"<c>"+str(w)+"<c>"+str(h)+"<c>ip"+ip+"<c>"+str(id_))
            if(data==data2):
                repeat+=1
            if(repeat==10):
                data=("comm=end")
                
            color=(255,0,0)
            stroke=2
            end_cord_x= x+w
            end_cord_y= y+h
            position_x=x
            position_w=w
            
                
        
        for(x,y,w,h) in faces:
            print("start line 150 socket_client.socket_client")
            socket_client.socket_client(data2)       
            print(x)
    if(cam==-1):
        ustap=input("do you want to start a conversation")
        if(ustap=="yes"):
            x=(0)
            y=(0)
            w=(0)
            h=(0)
            data2=("<c>"+str(x)+"<c>"+str(y)+"<c>"+str(w)+"<c>"+str(h)+"<c>ip"+str(ip)+"<c>"+id_)
            socket_client.socket_client(data2)
            
    
