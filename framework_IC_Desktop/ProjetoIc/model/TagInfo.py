'''
Created on 23/02/2015

@author: Marcelo
'''

class TagInfo(object):
    '''
    classdocs
    '''
    
    __idTagInfo=0
    __nome=''
    __descricao=''

    def __init__(self, nome,descricao,idTagInfo=0):
        '''
        Constructor
        '''
        self.__idTagInfo=idTagInfo
        self.__nome=nome
        self.__descricao=descricao

    def getIdTagInfo(self):
        return self.__idTagInfo
    def getNome(self):
        return self.__nome
    def getDescricao(self):
        return self.__descricao

    def setIdTagInfo(self, value):
        self.__idTagInfo = value
    def setNome(self, value):
        self.__nome = value
    def setDescricao(self, value):
        self.__descricao = value