'''
Created on 11/12/2014

@author: Marcelo
'''

class DataSource(object):
    '''
    classdocs
    '''
    #Definindo atributos
    __idEstacao_Meteo=0
    __Nome_Estacao=''
    __fabricante=''
    __modelo=''
    __node_idNode=0
    
    def __init__(self,nomeEstacao,fabricante,modelo,node_idNode,idEstacaoMeteo=0):
        '''
        Constructor
        '''
        self.__idEstacao_Meteo=idEstacaoMeteo
        self.__Nome_Estacao=nomeEstacao
        self.__fabricante=fabricante
        self.__modelo=modelo
        self.__node_idNode=node_idNode
    
    def getIdEstacao_Meteo(self):
        return self.__idEstacao_Meteo
    def getNome_Estacao(self):
        return self.__Nome_Estacao
    def getFabricante(self):
        return self.__fabricante
    def getModelo(self):
        return self.__modelo
    def getNode_idNode(self):
        return self.__node_idNode
    
    def setIdEstacao_Meteo(self,idEstacao_Meteo):
        self.__idEstacao_Meteo=idEstacao_Meteo
    def setNome_Estacao(self,nome_Estacao):
        self.__Nome_Estacao=nome_Estacao
    def setFabricante(self,fabricante):
        self.__fabricante=fabricante
    def setModelo(self,modelo):
        self.__modelo=modelo
    def setNode_idNode(self,idNode):
        self.__node_idNode=idNode    