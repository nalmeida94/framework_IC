'''
Created on 27/02/2015

@author: Marcelo
'''
from model.Valores import Valores

class ValoresDao(object):
    '''
    classdocs
    '''
    __banco=''

    def __init__(self, banco):
        '''
        Constructor
        '''
        self.__banco=banco
    
    def add(self,valores):
        sql = "INSERT INTO `values`(`VALUE`, `DATETIME`, `tag_idTAG`) VALUES (%f"%valores.getValor()+",'"+str(valores.getDataHora())+"',%d)"%valores.getIdTag()
        return self.__banco.exe(sql)
    def remove(self,id):
        sql = "DELETE FROM valores WHERE idValores=%d"%id
        return self.__banco.exe(sql)
    def update(self,valores):
        sql = "UPDATE valores SET VALOR=%f"%valores.getValor()+",DATAHORA='"+valores.getDataHora()+"',tag_idTAG=%d"%valores.getIdTag()+" WHERE idValores=%d"%valores.getIdValores()
        return self.__banco.exe(sql)
    def retrieve(self,id):
        sql = "SELECT * FROM valores WHERE idValores=%d"%id
        self.__banco.exe(sql)
        stringValores=self.__banco.cursor.fetchone()
        return Valores(stringValores[1],stringValores[2],stringValores[3],stringValores[0])