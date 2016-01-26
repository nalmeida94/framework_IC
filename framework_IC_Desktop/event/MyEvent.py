'''
Created on 21/07/2015

@author: Nathan
'''

import threading, time

class MyEvent(threading.Thread):
    def __init__(self, event, ser, running):
        threading.Thread.__init__(self)
        self.event = event
        self.ser = ser
        self.running = running;
    
    def run(self):
        while(not self.running.is_set()):
            while(not(self.ser.inWaiting() == 0)):
                time.sleep(0.1)
                self.event.set()
                time.sleep(0.1)
                self.event.clear()
        return 0
    