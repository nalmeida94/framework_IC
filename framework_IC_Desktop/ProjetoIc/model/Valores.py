'''
Created on 24/02/2015

@author: Marcelo
'''

class Valores(object):
    '''
    classdocs
    '''
    __idValores=0
    __valor=0
    __dataHora=''
    __tag_IdTag=0
    
    def __init__(self,valor,dataHora,tag_IdTag,idValores=0):
        '''
        Constructor
        '''
        self.__idValores=idValores
        self.__valor=valor
        self.__dataHora=dataHora
        self.__tag_IdTag=tag_IdTag

    def getIdValores(self):
        return self.__idValores
    def getValor(self):
        return float(self.__valor)
    def getDataHora(self):
        return self.__dataHora
    def getIdTag(self):
        return self.__tag_IdTag

    def setIdValores(self, value):
        self.__idValores = value
    def setValor(self, value):
        self.__valor = value
    def setDataHora(self, value):
        self.__dataHora = value
    def setIdTag(self, value):
        self.__tag_IdTag = value        