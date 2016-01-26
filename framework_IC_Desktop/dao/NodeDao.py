'''
Created on 04/12/2014
@author: Marcelo
'''

from model.Node import Node
#from _sqlite3 import SQLITE_ALTER_TABLE

class NodeDao(object):

    '''
    classdocs
    '''
    __banco = ''
    
    def __init__(self,banco):
        '''
        Constructor
        '''
        self.__banco = banco
    def add(self,node):
        sql = "INSERT INTO node( NOME, INFORMACOES) VALUES ('"+node.getNome()+"','"+node.getInfo()+"');"
        return self.__banco.exe(sql)
    def remove(self,id):
        sql = "DELETE FROM node WHERE idNode= %d"%id
        return self.__banco.exe(sql)
    def update(self,node):
        sql = "UPDATE node SET NOME='"+node.getNome()+"',INFORMACOES='"+node.getInfo()+"'WHERE idNODE=%d"%node.getId()
        return self.__banco.exe(sql)
    def retrieve(self,id):
        sql="SELECT * FROM node WHERE idNode=%d"%id
        self.__banco.exe(sql)
        stringNode=self.__banco.cursor.fetchone()
        return Node(stringNode[1], stringNode[2], stringNode[0])        