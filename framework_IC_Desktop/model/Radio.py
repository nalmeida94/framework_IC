'''
Created on 24/02/2015

@author: Marcelo
'''

class Radio(object):
    '''
    classdocs
    '''
    __idRadio=0
    __endReal=''
    __radioTipo_IdRadioTipo=0
    __datasourse_IdEstacao_Meteo=0

    def __init__(self, endReal,radioTipo_IdRadioTipo,datasourse_IdEstacao_Meteo,idRadio=0):
        '''
        Constructor
        '''
        self.__idRadio=idRadio
        self.__endReal=endReal
        self.__radioTipo_IdRadioTipo=radioTipo_IdRadioTipo
        self.__datasourse_IdEstacao_Meteo=datasourse_IdEstacao_Meteo

    def getIdRadio(self):
        return self.__idRadio
    def getEndReal(self):
        return self.__endReal
    def getIdRadioTipo(self):
        return self.__radioTipo_IdRadioTipo
    def getIdEstacaoMeteo(self):
        return self.__datasourse_IdEstacao_Meteo

    def setIdRadio(self, value):
        self.__idRadio = value
    def setEndReal(self, value):
        self.__endReal = value
    def setIdRadioTipo(self, value):
        self.__radioTipo_IdRadioTipo = value
    def setIdEstacaoMeteo(self, value):
        self.__datasourse_IdEstacao_Meteo = value