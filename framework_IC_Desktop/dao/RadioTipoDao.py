'''
Created on 24/02/2015

@author: Marcelo
'''
from model.RadioTipo import RadioTipo

class RadioTipoDao(object):
    '''
    classdocs
    '''
    __banco=''

    def __init__(self,banco):
        '''
        Constructor
        '''
        self.__banco=banco
        
    def add(self, radioTipo):
        sql="INSERT INTO radiotipo (nome, descricao) VALUES ('"+radioTipo.getNome()+"','"+radioTipo.getDescricao()+"');"
        return self.__banco.exe(sql)
    def remove(self,id):
        sql="DELETE FROM radiotipo WHERE idradioTipo=%d"%id
        return self.__banco.exe(sql)
    def update(self,radioTipo):
        sql="UPDATE radiotipo SET nome='"+radioTipo.getNome()+"',descricao='"+radioTipo.getDescricao()+"' WHERE idradioTipo=%d"%radioTipo.getIdRadioTipo()
        return self.__banco.exe(sql)
    def retrieve(self,id):
        sql="SELECT * FROM radiotipo WHERE idradioTipo=%d"%id
        self.__banco.exe(sql)
        stringRadioTipo=self.__banco.cursor.fetchone()
        return RadioTipo(stringRadioTipo[1],stringRadioTipo[2],stringRadioTipo[0])