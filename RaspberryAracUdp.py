from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.internet import task
import struct, time, socket, threading
import RPi.GPIO as GP

GP.setmode(GP.BOARD) ##
GP.setup(12,GP.OUT) ## Servo PWM
GP.setup(40,GP.OUT) ## Led Pin
GP.setup(16,GP.OUT) ## SağMotor İleri
GP.setup(18,GP.OUT) ## SağMotor Geri
GP.setup(35,GP.OUT) ##  SağMotor PWM
GP.setup(3,GP.OUT)  ## SolMotor İleri
GP.setup(5,GP.OUT)  ##  SolMotor Geri
GP.setup(33,GP.OUT) ##  Sol Motor PWM

Servo=GP.PWM(12,50)
Servo.start(0)
SgM=GP.PWM(35,50)
SlM=GP.PWM(33,50)
SgM.start(0)
SlM.start(0)

Joys=[0,0,0,0,0,0,0,0]
active = False


class Client(DatagramProtocol):
    def __init__(self, host, port,tHost):
        if host == "localhost":
            host="127.0.0.1"
        self.id= host,port
        self.address = None
        self.server = tHost, port
        print("Working on id", self.id)
    
    def startProtocol(self):
        self.transport.write("ready".encode('utf-8'),self.server)

    def datagramReceived(self, data, addr):
        global Joys, active
        active = True
        if addr == self.server:
            numOfValues = len(data) / 8
            mess=struct.unpack('>' + 'd' * round(numOfValues), data)
            Joys = [ round(element,6) for element in mess ]
            print(Joys)

def timeout():
    global active, Joys
    if not active:
        Joys = [0,0,0,0,0,0,0,0]
    active = False      
            

def sendCommands():
    global joysticks,Led,Joys,active,GP,Servo

    try:
        while True:
            if active:
                Servo.ChangeDutyCycle(Joys[2])
                GP.output(40, Joys[5])
                AracHareket(Joys[4],Joys[1])

    

                
    except Exception as error:
        print ("Error on sendCommands thread: "+str(error))
        #sendCommands()

def AracHareket(x,p):
    global SgM,SlM,GP
    if (x==0):
        GP.output(16, 1)
        GP.output(18, 0)
        GP.output(3, 1)
        GP.output(5, 0)
    if (x==1):
        GP.output(18, 0)
        GP.output(18, 1)
        GP.output(18, 0)
        GP.output(18, 1)
    SgM.ChangeDutyCycle(p)
    SlM.ChangeDutyCycle(p)

def LedYak(k):
    global GP
    if (k==1):
        GP.output(40,1)
    else:
        GP.output(40,0)        

if __name__== '__main__' :
    try:
        port= 51001
        hostTarget="192.168.1.118"
        vehicleThread = threading.Thread(target=sendCommands)
        vehicleThread.daemon=True
        vehicleThread.start()
        l = task.LoopingCall(timeout)
        l.start(0.5)
        reactor.listenUDP(port,Client('localhost',port,hostTarget))
        reactor.run()

    except Exception as error:
        print ("Error on main: "+str(error))
       
    except KeyboardInterrupt:                   
        print ("Keyboard Interrupt, exiting.")
        exit()
