'''
Created on 27/02/2015

@author: Marcelo
''' 
from model.TagInfo import TagInfo

class TagInfoDao(object):
    '''
    classdocs
    '''
    __banco=''

    def __init__(self, banco):
        '''
        Constructor
        '''
        self.__banco=banco
    
    def add(self,tagInfo):
        #TODO: Warning: Data truncated for column 'DATAHORA' at row 1
        sql = "INSERT INTO taginfo(NOME, DESCRICAO) VALUES  ('"+tagInfo.getNome()+"','"+tagInfo.getDescricao()+"');"
        return self.__banco.exe(sql)
    def remove(self,id):
        sql = "DELETE FROM taginfo WHERE idtagInfo=%d"%id
        return self.__banco.exe(sql)
    def update(self,tagInfo):
        sql = "UPDATE taginfo SET NOME='"+tagInfo.getNome()+"', DESCRICAO='"+tagInfo.getDescricao()+"' WHERE idtagInfo=%d"%tagInfo.getIdTagInfo()
        return self.__banco.exe(sql)
    def retrieve(self,id):
        sql = "SELECT * FROM taginfo WHERE idtagInfo=%d"%id
        self.__banco.exe(sql)
        stringValores=self.__banco.cursor.fetchone()
        return TagInfo(stringValores[1],stringValores[2],stringValores[0])