import pyaudio
import struct
import numpy as np
import time
o=(0)
before=(0)
said=(" ")
start_end=(0)

end=(0)
data2=[]
number_time=(0)
pas=False
prob_bla=(0)
CHUNK = 1024 * 4
data_before=("")
data2_1=[]
data_numb2=(0)
similarity=(0)
stop=(0)
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
p= pyaudio.PyAudio()
def sound():
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
    data_int2=int(data_int[0])
    
    return data_int2

 


def sound1() :
    sound2=(0)
    data_in=(0)
    sound1=sound()
    cont=(0)
    data2=(" ")
    continu2=False
    pas2=False
    pas=False
   
    record=True
    data_in=sound()  
   
            
  
    while record:   
        
        data_in2=data_in        
        data_in=sound()
        time.sleep(0.01)
        print("finding noise")
        
        if(data_in>data_in2+8):# find suddent noise
            continu2=True
            print("execute")
            
            while continu2:
                sound3=sound2# record the noise and chek if it could be a syllable        
                sound1=sound()
                if(pas2==False):
                    print("__record")
                    time.sleep(sound1>sound2)
                    pas2=True
                sound3=sound2
                sound2=sound1
                sound1=sound()                     
                data2=(str(data2)+","+str((sound2-sound1)))
                cont+=1
                
                time.sleep(0.004)
                sound2=sound1
                sound1=sound()   
                data2=(str(data2)+","+str((sound2-sound1)))
                cont+=1
                
                time.sleep(0.004)
                sound2=sound1
                sound1=sound()   
                data2=(str(data2)+","+str((sound2-sound1)))
                cont+=1
                    
              
                    
                data3=("")
                data3_1=("")
                data4=("")
               
                    
                   
                    
                
               
               
                if(cont>9):
                    pas=True
                    record=False 
                    data2=(str(data2)+","+str(cont))
                    print(data2)
                    print("data2_sound_module")
                    return data2
                    break
                print("record")
                if(sound3>sound2+4 and sound2>=sound1+4):
                    pas=True
                    record=False
                    data2=(str(data2)+","+str(cont))
                    print(data2)
                    print("data2_sound_module")
                    return data2
                    break
                   
                if(int(sound2)<sound3 and sound1>sound2):# if true there is a syllable                
                    if(data_in>data_in2+10):# find suddent noise  
                        print("___________record2________")
                        
               
                if(pas==True and cont is not 0):
                    print("end_record")
                    record=False
                    print(data2)
                    data2=(str(data2)+","+str(cont))
                    print("data2_sound_module")
                    return data2
                    break
                if(pas==True):
                    print("end_record")
                    record=False
                    print(data2)
                    data2=(str(data2)+","+str(cont))
                    print("data2_sound_module")
                    return data2
                    break
 
while True:                   
    sound2=sound1()
    d=input("what")
    if(d=="oui"):
        with open("oui.txt", "a")as fic:
            fic.write(sound2)
    if(d=="non"):
        with open("non.txt", "a")as fic:
            fic.write(sound2)
            