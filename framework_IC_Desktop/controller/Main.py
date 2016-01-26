'''
Created on 23/12/2014

@author: Marcelo
'''

from controller.SerialPort import SerialPort
from controller.BancoDeDados import BancoDeDados
from controller.NodeSync import NodeSync

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
    