'''
Created on 23/12/2014

@author: Marcelo
'''
from dao.BancoDeDados import BancoDeDados
from dao.NodeSync import NodeSync
import SerialPort

bd =''
nodeSync =''

if __name__ == '__main__':
    
    bd=BancoDeDados()
    nodeSync = NodeSync(bd)    
    #getting all serial devices detected
    #change it if necessary
    path = '/dev/ttyUSB*'
    
    serialPort = SerialPort(nodeSync, path)
    serialPort.sendMessage()
    
    
    """
    try:
        #creating a serial port at the first port founded
        ser = serial.Serial(path[0])
    except IndexError:
        print("None device was detected!\nVerify your Sync Node!!!")
        quit()
    #setting timeout to 0, non blocking communication
    ser.timeout = 0
    if(not ser.isOpen()):
        ser.open()    
    ################ Creating the event and listener
    event = threading.Event()
    eventSerial = MyEvent(event, ser)
    listenerSerial = MyListener(event, ser, nodeSync)
    eventSerial.start()
    listenerSerial.start()
    ################
    
    #Retrieving to user the new serial port  
    print ser    
    """
    

    
    """
    while(1):
        msg = raw_input("Type the message (Type 'exit' to exit the program): ")
        #Exiting program
        if(msg=='exit'):        
            print("Exiting...")
            listenerSerial.join(0)
            event.set()
            eventSerial.join(0)
            eventSerial.running.set()
            listenerSerial.running.set()
            ser.close()
            sys.exit()    
        try:        
            #Writing the message
            ser.write(msg)
            time.sleep(1)
        except (serial.SerialException,IOError):
            print("An IO error happened at send message!")
        except serial.SerialTimeoutException:
            print("An Timeout error happened at send message!")
    """
    