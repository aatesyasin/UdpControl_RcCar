from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from random import randint
import struct, time, socket
import pygame
import math,threading
joysticks =[]
Joys=[0,0,0,0,0,0,0,0]
Led=False
class Client(DatagramProtocol):
    def __init__(self, host, port):
        self.address =  host,port       
        
    def datagramReceived(self, data, addr):
        data=data.decode('utf-8')
        dr=0
        if addr == self.address and dr==0:
            reactor.callInThread(self.send_message)
            print(addr,":",data)
            dr=1
        else:
            print(addr,":",data)
    
    def send_message(self):
        global Joys
        while True:
            if Joys[6]==1:
                reactor.callFromThread(reactor.stop)
                reactor.stop
                exit()
            buf = bytes()
            for val in Joys:
                buf +=struct.pack('>' + 'd', val)           
            
            self.transport.write(buf, self.address)
            time.sleep(0.0001)
    
        
        

def sendCommands():
    global Joys,joysticks,Led
    k=int(input("Araç Hazır Olunca 1 Yazınız.. "))
    while(k>0):
    
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameExit=True
            if event.type == pygame.JOYBUTTONDOWN:
                if(event.button==0):
                    k=0
                    Joys[6]=1
                    exit()
                if(event.button==5):
                    if Led==False:
                        Joys[5]=1
                        Led=True
                    else:
                        Joys[5]=0
                        Led=False

            axes = joysticks[-1].get_numaxes()
            for i in range(axes):
                if joysticks[-1].get_axis(i)<0.02 and joysticks[-1].get_axis(i)>-0.02:
                    Joys[i]=0
                else:
                    if (i==1):
                        if(round(joysticks[-1].get_axis(i),3)*(-1)>0):
                            Joys[4]=1
                        elif(round(joysticks[-1].get_axis(i),3)*(-1)<0) :
                            Joys[4]=-1

                        Joys[i]= abs(round(joysticks[-1].get_axis(i),3))*100
                    elif(i==2):
                        
                        Joys[i]= round(((round((joysticks[-1].get_axis(i)*-1),3)+1)*3.5)+2,1)
                        

                    else:
                        Joys[i]= round(joysticks[-1].get_axis(i),3)                       

                    
                
            print(Joys)


            
if __name__== '__main__' :
    import pygame
    pygame.init()
    for i in range(0,pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[-1].init()
        print("Bulunan jotstick '",joysticks[-1].get_name(),"'")
    vehicleThread = threading.Thread(target=sendCommands)
    vehicleThread.daemon=True
    vehicleThread.start()
    
    port= 51001
    reactor.listenUDP(port,Client('192.168.1.4',port))
    reactor.run()


  
