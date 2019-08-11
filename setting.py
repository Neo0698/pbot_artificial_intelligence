import socket
import socket_client
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
    opencv=input("do you have a camera:")
    with open("setting.txt", "a")as fic:
        fic.write("cam=yes")     
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
                    img_item=("image/ima10.png")
                    cv2.imwrite(img_item, roi_gray)
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    img_item= ("c:/user/rapha/onedrive/desktop/face/image/ima"+"11.png")
                    cv2.imwrite(img_item, roi_gray)
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    img_item= ("image/ima"+"11.png")
                    cv2.imwrite(img_item, roi_gray)
                    cap=cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    img_item= ("image/ima12.png")
                    cv2.imwrite(img_item, roi_gray)
                    number_img=(0)            
                    print("if after")
                    x_train=[]
                    y_labels=[]
                    label_ids= {}
                    id_=(0) 
                    number_img=(0)
                    number_img=(0)
                    print(number_img)
                    while (int(number_img)<4):
                        print("scanning image")
                        path=("image/ima1"+str(number_img)+".png")                        
                        number_img+=1
                        pil_image = Image.open(path).convert("L")
                        image_array = np.array(pil_image, "uint8")
                        print(image_array)
                        current_id=id_
                        label=("adm")
                        label_ids[label] = current_id
                        current_id+=1
			
                
			
                        faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)                        
                        roi = image_array[y:y+h, x:x+w]
                        x_train.append(roi)
                        y_labels.append(id_)
                        #print(y_labels)
                        #print(x_train)
                        recognizer = cv2.face.LBPHFaceRecognizer_create()
                        with open("labels.picle", 'wb')as f:
                            pickle.dump(label_ids, f)
                        recognizer.train(x_train, np.array(y_labels))
                        print("saving image")
                        recognizer.save("image/trainner212.yml")
                        found=(1)
                        break



    con=input("do you have a compte?")
    if(con=="y"):
        con2=input("what his your compte?")
        pas_con=input("whar his you password")
        data2=("prog_id"+str(con2)+"pas"+str(pas_con))
        socket_client.socket_client(data2)
        autorization=socket_client.socket_serveur
        (data2)
            

