#coding:utf-8

def socket_client(impdata2, impip):
    import socket
   
    host, port = ('192.168.1.34',5567)
    
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
        data=(str(impdata2)+"<c>ip"+str(impip))
        data = data.encode("utf8")
        socket.sendall(data)
       
                  
    except ConnectionRefusedError:
        print("Error no connection")
    finally: 
       
        socket.close()        
        socket_serveur(impip)
def socket_serveur(impip):   
    
            import socket
            stop=0
            host, port = ('',5566)
            socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            o=False 
           
            #face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt.xml')
            #recognizer = cv2.face.LBPHFaceRecognizer_create()    
            socket.listen(5)
            while o==False:
                try:
                    o=True
                    print("serveur connection")
                    socket.bind((host, port))
                except: 
                    o=False
                finally:
                    if(o==True):
                        o=True
                    
            
           
            conn, adress = socket.accept()
           
            data= conn.recv(2048)
            socket.close()
                        
            data_find=(str(data).find("input"))
            data_find_br=(str(data).find("break"))
            
            data_find_print=(str(data).find("print"))    
            if(data_find_print is not -1):
                print(data)                
                sound_find=(str(data).find("sound")) 
                print(sound_find)
                if(sound_find is not -1 and stop==0):
                        import speech2
                        print("sound")
                        data_send=speech2.sound1()
                        data=str(data_send)
                        print(data)
                        print("sound module")
                        socket_client(data, impip)
            if(data_find_br is not -1):
                return 0
                stop=1
            if(data_find is not -1):
                    data_send=input(str(data))
                    print(data)
                    data=(data_send)
                    data_find=(str(data).find("who"))
                    sound_find=(str(data).find("sou"))
                    print("sound_find")
                    print(sound_find)
                    if(sound_find is not -1):
                        import speech2
                        print("sound")
                        data_send=speech2.sound1()
                        print(data_send)
                        data=str(data_send)
                        print("end sound")
                        
                    if(data_find is not -1):
                        with open("setting.txt", "r")as fic:
                            setting_set=fic.read()
                        data=(data_send+"<c>"+setting_set)
                    print("send to client")
                    print(data)
                    if(stop==0):
                        socket_client(data, impip)
                    print("client")
            
                    
                    
            
