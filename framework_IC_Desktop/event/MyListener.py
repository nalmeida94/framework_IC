'''
Created on 21/07/2015

@author: Nathan
'''

import serial, threading
from exceptions import IOError


class MyListener(threading.Thread):
    def __init__(self, event, ser, nodeSync, running):
        threading.Thread.__init__(self)
        self.event = event
        self.ser = ser
        self.rlock = threading.RLock()
        self.running = running
        self.nodeSync = nodeSync
    
    def run(self):        
        while(not self.running.is_set()):
            try:                
                self.event.wait()  
                self.rlock.acquire(1)                
                self.event.clear()
                line = self.ser.readline()
                self.ser.flushInput()                
                self.rlock.release()
                
                print("Message received: "+line)              
                self.nodeSync.lerDados(line)
                #TODO ARMENGUE TIRAR DAQUI
                mensagem = line.split("&");                
                self.nodeSync.lerDados("25&"+mensagem[1]+"&"+mensagem[2])
                
            except (serial.SerialException,IOError):
                print("An IO error happened at receive message!!!")        
            except serial.SerialTimeoutException:
                print("A Timeout error happened at receive message!!!")                
        return 0
    
    