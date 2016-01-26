'''
Created on 24/02/2015

@author: Marcelo
'''

class Snapshot(object):
    '''
    classdocs
    '''
    __idSnapshot=0
    __valor=''
    __snapshot=''#TODO: timestap arrumar um formato de data para o python
    __nome_Tag=''
    __tag__IdTag=0

    def __init__(self, valor,snapshot,tag_IdTag,idSnapshot=0):
        '''
        Constructor
        '''
        self.__idSnapshot=idSnapshot
        self.__valor=valor
        self.__snapshot=snapshot
        self.__tag__IdTag=tag_IdTag

    def getIdSnapshot(self):
        return int(self.__idSnapshot)
    def getValor(self):
        return float(self.__valor)
    def getDataHora(self):
        return self.__snapshot
    def getIdTag(self):
        return int(self.__tag__IdTag)

    def setIdsnapshot(self, value):
        self.__idSnapshot = value
    def setValor(self, value):
        self.__valor = value
    def setSnapshot(self, value):
        self.__snapshot = value
    def setIdTag(self, value):
        self.__tag__IdTag = value