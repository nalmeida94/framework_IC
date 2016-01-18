'''
Created on 23/02/2015

@author: Marcelo
'''

class Tag(object):
    '''
    classdocs
    '''
    
    __idTag=0
    __desvio=''
    __tempo_Max=''
    __conv_Rate=0
    __tagInfo_idTagInfo=0
    __datasource_idEstacao_Meteo=0
    def __init__(self, desvio,tempoMax,convRate,IdTagInfo,idEstacaoMeteo,idTag=0):
        '''
        Constructor
        '''
        self.__idTag=idTag
        self.__desvio=desvio
        self.__tempo_Max=tempoMax
        self.__conv_Rate=convRate
        self.__tagInfo_idTagInfo=IdTagInfo
        self.__datasource_idEstacao_Meteo=idEstacaoMeteo

    def getIdTag(self):
        return self.__idTag
    def getDesvio(self):
        return self.__desvio
    def getTempoMax(self):
        return self.__tempo_Max
    def getConvRate(self):
        return self.__conv_Rate
    def getTagInfo(self):
        return self.__tagInfo_idTagInfo
    def getIdEstacaoMeteo(self):
        return self.__datasource_idEstacao_Meteo
    
    def setIdTag(self, value):
        self.__idTag = value
    def setDesvio(self, value):
        self.__desvio = value
    def setTempoMax(self, value):
        self.__tempo_Max = value
    def setConvRate(self, value):
        self.__conv_Rate = value
    def setIdTagInfo(self, value):
        self.__tagInfo_idTagInfo = value
    def setIdEstacaoMeteo(self, value):
        self.__datasource_idEstacao_Meteo = value