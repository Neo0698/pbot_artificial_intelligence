import socket
import socket_client
import face_train
def menu():
    ip=([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0])
    ip_ask=input("this programme needs to use the ip of this computer y/n")
    if(ip_ask=="y"):
        print("we got the ip"+ip)
        with open("setting.txt", "w")as fic:
            fic.write("ip:"+str(ip)+"/")
    if(ip_ask=="n"):
        print("sorry but this version needs the ip, there his no sollution for this version")
    microphone_ask=input("do you use a microphone compatible with the libary pyaudio |yes|no|don't know")
    microphone_ask_find=(microphone_ask.find("know"))
    if(microphone_ask_find is not -1):
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        p= pyaudio.PyAudio()
        stream=p.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            output=True,
            frames_per_buffer=CHUNK
        )
        data =stream.read(CHUNK)
        data_int =np.array (struct.unpack(str(2* CHUNK)+ 'B', data))
        print(data_int)
    password=input("what password do you want to setup?")
    with open("setting.txt", "a")as fic:
        fic.write("pas=="+password+"/")
   
    with open("setting.txt", "a")as fic:
        fic.write("cam=yes")
    with open("setting.txt", "r")as fic:
        set_=fic.read()
    data2=("setting set"+str(set_))    
    socket_client.socket_client(data2, ip)
    opencv=input("do you have a camera:")
    if(opencv=="yes"):
        import cv2
        from PIL import Image
        import numpy as np
        import pickle
        print("ok we will take some picture.")
        print("the admin pleas go infront of the camera alone")
        found=(0)
        while found==0:
            print(found)
            print("found")
            face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt.xml')
            cap=cv2.VideoCapture(0)
            ret, frame = cap.read()    
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)            
            for(x, y, w, h) in faces:
                    roi_gray = gray[y:y+h, x:x+w]
                    img_item=("image/user1/ima10.png")
                    cv2.imwrite(img_item, roi_gray)
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    img_item= ("image/user1/ima"+"11.png")
                    cv2.imwrite(img_item, roi_gray)
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    img_item= ("image/user1/ima"+"11.png")
                    cv2.imwrite(img_item, roi_gray)
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    img_item= ("image/user1/ima12.png")
                    cap=cv2.VideoCapture(0)
                    cv2.imwrite(img_item, roi_gray)
                    ret, frame = cap.read()
                    img_item= ("image/user1/ima13.png")
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    cv2.imwrite(img_item, roi_gray)
                    img_item= ("image/user1/ima14.png")
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    cv2.imwrite(img_item, roi_gray)
                    img_item= ("image/user1/ima15.png")
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    cv2.imwrite(img_item, roi_gray)
                    found=(1)
                    
                       
    d=input("pleas put another face")
    found=(0)
    while found==0:
            print(found)
            print("found")
            face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt.xml')
            cap=cv2.VideoCapture(0)
            ret, frame = cap.read()    
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)            
            for(x, y, w, h) in faces:
                    roi_gray = gray[y:y+h, x:x+w]
                    img_item=("image/user2/ima10.png")
                    cv2.imwrite(img_item, roi_gray)
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    img_item= ("image/user2/ima"+"11.png")
                    cv2.imwrite(img_item, roi_gray)
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    img_item= ("image/user2/ima"+"11.png")
                    cv2.imwrite(img_item, roi_gray)
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    img_item= ("image/user2/ima12.png")
                    cap=cv2.VideoCapture(0)
                    cv2.imwrite(img_item, roi_gray)
                    ret, frame = cap.read()
                    img_item= ("image/user2/ima13.png")
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    cv2.imwrite(img_item, roi_gray)
                    img_item= ("image/user2/ima14.png")
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    cv2.imwrite(img_item, roi_gray)
                    img_item= ("image/user2/ima15.png")
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    cv2.imwrite(img_item, roi_gray)
                    number_img=(0) 
                    face_train.train()
                    print("we recomande you to restart the program")
                    found=1
                    








