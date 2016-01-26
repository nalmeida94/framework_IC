'''
Created on 24/02/2015

@author: Marcelo
'''

class RadioTipo(object):
    '''
    classdocs
    '''
    __idRadioTipo=0
    __nome=''
    __descricao=''

    def __init__(self, nome,descricao,idRadioTipo=0):
        '''
        Constructor
        '''
        self.__idRadioTipo=idRadioTipo
        self.__nome=nome
        self.__descricao=descricao

    def getIdRadioTipo(self):
        return self.__idRadioTipo
    def getNome(self):
        return self.__nome
    def getDescricao(self):
        return self.__descricao
    
    def setIdRadioTipo(self, value):
        self.__idRadioTipo = value
    def setNome(self, value):
        self.__nome = value
    def setDescricao(self, value):
        self.__descricao = value