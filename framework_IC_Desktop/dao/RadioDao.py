'''
Created on 24/02/2015

@author: Marcelo
'''
#TODO:Testar
from model.Radio import Radio
class RadioDao(object):
    '''
    classdocs
    '''
    __banco=''
#TODO: Alterar no sql todos os tipo de dados int
    def __init__(self, banco):
        '''
        Constructor
        '''
        self.__banco=banco
    def add(self,radio):
        sql= "INSERT INTO radio(endReal,radioTipo_idradioTipo,datasource_idESTACAO_METEO) VALUES ('"+radio.getEndReal()+"',%d"%radio.getIdRadioTipo()+",%d"%radio.getIdEstacaoMeteo()+");"
        print sql
        return self.__banco.exe(sql)
    def remove(self,id):
        sql= "DELETE FROM radio WHERE idradio= %d"%id
        return self.__banco.exe(sql)
    def update(self,radio):
        sql= "UPDATE radio SET endReal='"+radio.getEndReal()+"',radioTipo_idradioTipo=%d"%radio.getIdRadioTipo()+",datasource_idESTACAO_METEO=%d"%radio.getIdEstacaoMeteo()+" WHERE idradio=%d"%radio.getIdRadio()
        return self.__banco.exe(sql)
    def retrieve(self,id):
        sql= "SELECT * FROM radio WHERE idradio=%d"%id
        self.__banco.exe(sql)
        stringRadio=self.__banco.cursor.fetchone()
        return Radio(stringRadio[1],stringRadio[2],stringRadio[3],stringRadio[0])