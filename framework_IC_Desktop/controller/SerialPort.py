'''
Created on 30/03/2015

@author: Nathan
'''

import glob, serial, time, sys, threading
from exceptions import IOError
from event import MyEvent, MyListener

class SerialPort():
    def __init__(self, nodeSync, path):
        self.nodeSync = nodeSync
        pathFounded = glob.glob(path)
        try:
            #creating a serial port at the first port founded
            self.ser = serial.Serial(pathFounded[0])
        except IndexError:
            print("None device was detected!\nVerify your Sync Node!!!")
            quit()
        #setting timeout to 0, non blocking communication
        self.ser.timeout = 0
        #opennig the port
        if(not self.ser.isOpen()):
            self.ser.open()    
        ################ Creating the event and listener
        self.event = threading.Event()
        self.running = threading.Event()
        self.eventSerial = MyEvent(self.event, self.ser, self.running)
        self.listenerSerial = MyListener(self.event, self.ser, self.nodeSync, self. running)
        self.eventSerial.start()
        self.listenerSerial.start()
        ##################
        
        #Showing to user the new serial port  
        print self.ser
        print "Starting output terminal in 3 seconds..."
        
        
    def sendMessage(self):
        while(1):
            msg = raw_input("Type the message (Type 'exit' to exit the program): ")
            #Exiting program
            if(msg=='exit'):
                print("Exiting...")
                self.listenerSerial.join(0)
                self.event.set()
                self.eventSerial.join(0)
                self.running.set()
                self.ser.close()
                sys.exit()    
            try:        
                #Writing the message
                self.ser.write(msg)
                time.sleep(1)
            except (serial.SerialException,IOError):
                print("An IO error happened at send message!")
            except serial.SerialTimeoutException:
                print("An Timeout error happened at send message!")
                
                
        