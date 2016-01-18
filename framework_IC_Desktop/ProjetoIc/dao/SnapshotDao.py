'''
Created on 19/04/2015

@author: Marcelo
'''

from model.Snapshot import Snapshot
 
class SnapshotDao(object):
    '''
    classdocs
    '''
    __banco=''

    def __init__(self, banco):
        '''
        Constructor
        '''
        self.__banco = banco    
    def add(self,snapshot):
        sql = "INSERT INTO snapshot(VALOR, SNAPSHOT, NOME_TAG, tag_idTAG) VALUES (%f"%snapshot.getValor()+",'"+snapshot.getSnapshot()+"','"+snapshot.getNomeTag()+"',%d"%snapshot.getIdTag()+");"
        return self.__banco.exe(sql)
    def remove(self,id):
        sql = "DELETE FROM snapshot WHERE idSNAP= %d"%id
        return self.__banco.exe(sql)
    def update(self,snapshot):
        sql = "UPDATE snapshot SET VALOR=%f"%snapshot.getValor()+",SNAPSHOT='"+snapshot.getDataHora()+"',NOME_TAG='"+snapshot.getNomeTag()+"',tag_idTAG=%d"%snapshot.getIdTag()+" WHERE idSNAP= %d"%snapshot.getIdSnapshot()
        return self.__banco.exe(sql)
    def retrieve(self,id):
        sql = "SELECT * FROM snapshot WHERE idSNAP= %d"%id
        self.__banco.exe(sql)
        stringDataSource=self.__banco.cursor.fetchone()
        return Snapshot(stringDataSource[1], stringDataSource[2], stringDataSource[3], stringDataSource[4], stringDataSource[0])
