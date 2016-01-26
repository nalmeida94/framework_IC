'''
Created on 11/12/2014

@author: Marcelo
'''

class Node(object):
    '''
    classdocs
    '''
    #Definindo atributos
    __id=0
    __nome=''
    __info=''
    
    def __init__(self,nome,info,id=0):
        '''
        Constructor
        '''
        self.__id=id
        self.__nome=nome
        self.__info=info
    def getId(self):
        return self.__id
    def getNome(self):
        return self.__nome
    def getInfo(self):
        return self.__info
    def setId(self,id):
        self.__id=id
    def setNome(self,nome):
        self.__nome=nome
    def setInfo(self,info):
        self.__info=info 