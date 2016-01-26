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
        sql = "INSERT INTO snapshot(`VALUE`, SNAPSHOT, tag_idTAG) VALUES (%f"%snapshot.getValor()+",'"+snapshot.getDataHora()+"',%d"%snapshot.getIdTag()+");"
        return self.__banco.exe(sql)
    def remove(self,id):
        sql = "DELETE FROM snapshot WHERE idSNAP= %d"%id
        return self.__banco.exe(sql)
    def update(self,snapshot):
        sql = "UPDATE snapshot SET `VALUE`=%f"%snapshot.getValor()+",SNAPSHOT='"+snapshot.getDataHora()+"' WHERE tag_idTAG= %d"%snapshot.getIdTag()
        return self.__banco.exe(sql)
    def retrieve(self,id):
        sql = "SELECT * FROM snapshot WHERE tag_idTAG= %d"%id
        self.__banco.exe(sql)
        stringSnapshot=self.__banco.cursor.fetchone()
        return Snapshot(stringSnapshot[1], stringSnapshot[2], stringSnapshot[3], stringSnapshot[0])
        