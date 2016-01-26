'''
Created on 04/12/2014
@author: Marcelo
'''

from model.DataSource import DataSource

class DataSourceDao(object):

    '''
    classdocs
    '''
    __banco = ''
    
    def __init__(self,banco):
        '''
        Constructor     
        '''
        self.__banco = banco
    def add(self,dataSource):
        sql = "INSERT INTO datasource(NOME_ESTACAO, FABRICANTE, MODELO, node_idNODE)VALUES ('"+dataSource.getNome_Estacao()+"','"+dataSource.getFabricante()+"','"+dataSource.getModelo()+"',%d);"%dataSource.getNode_idNode()
        return self.__banco.exe(sql)
    def remove(self,id):
        sql = "DELETE FROM datasource WHERE idESTACAO_METEO= %d"%id
        return self.__banco.exe(sql)
    def update(self,dataSource):
        sql = "UPDATE datasource SET NOME_ESTACAO='"+dataSource.getNome_Estacao()+"',FABRICANTE='"+dataSource.getFabricante()+"',MODELO='"+dataSource.getModelo()+"',node_idNODE=%d"%dataSource.getNode_idNode()+" WHERE idESTACAO_METEO=%d"%dataSource.getIdEstacao_Meteo()
        return self.__banco.exe(sql)
    def retrieve(self,id):
        sql = "SELECT * FROM datasource WHERE idESTACAO_METEO=%d"%id
        self.__banco.exe(sql)
        stringDataSource=self.__banco.cursor.fetchone()
        return DataSource(stringDataSource[1], stringDataSource[2], stringDataSource[3], stringDataSource[4], stringDataSource[0])