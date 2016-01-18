'''
Created on 22/04/2015
Classe que recebe a mensagem do node sync e salva no bd.
@author: Marcelo
'''

import datetime,time
from dao.ValoresDao import ValoresDao
from dao.SnapshotDao import SnapshotDao
from dao.TagDao import TagDao

from model.Valores import Valores
from model.Snapshot import Snapshot
from model.Tag import Tag


class NodeSync(object):
    '''
    classdocs
    '''
    __bd = ''
    __valoresDao = ''
    __snapshotDao = ''
    __tagDao = ''

    def __init__(self,bd):
        self.__bd = bd
        self.__valoresDao = ValoresDao(self.__bd)
        self.__snapshotDao = SnapshotDao(self.__bd)
        self.__tagDao = TagDao(self.__bd)
        
        #TODO: Buscar valores gravados
        #self.__valorGravado = self.__valoresDao.retrieve(1)
    
    def lerDados(self,mensagem):
        print mensagem
        mensagem = mensagem.split("&")
        id = mensagem[0]
        valor = mensagem[1]
        data_Hora = mensagem[2]
        
        valorNovo = Valores(valor, data_Hora, int(id))#
        self.__valoresDao.add(valorNovo)
        
        '''
        valorAtual = self.__snapshotDao.retrieve(int(id))#valorAtual buscar no banco snapshot
        
        valorRecente = Valores(valor, data_Hora, int(id))#valorRecente ultimo lido 
        tag = self.__tagDao.retrieve(int(id))
        desv = tag.getDesvio()#desv buscar no banco em tag
        tempo = tag.getTempoMax()#tempo buscar no banco em tag
        
        if(self.testeParalelogramo(self.__valorGravado, valorAtual, valorRecente, desv, tempo)):
            
            snapshot = Snapshot(valorRecente.getValor(), valorRecente.getDataHora(), "", int(valorRecente.getIdTag()),int(valorRecente.getIdTag()))
            self.__snapshotDao.update(snapshot)
        else:
            self.__valoresDao.add(valorAtual)
            self.__valorGravado=valorAtual
            snapshot = Snapshot(valorRecente.getValor(), valorRecente.getDataHora(), "", int(valorRecente.getIdTag()),int(valorRecente.getIdTag()))
            self.__snapshotDao.update(snapshot)
        '''
    #ValorGravado Ultimo valor salvo no banco de dados.
    #ValorAtual Valor do snapshot.
    #ValorRecente Ultimo valor lido do sensor.
    
    def testeParalelogramo(self,valorGravado,valorAtual,valorRecente,desv,tempo):
        #TODO: valorProximo =valor Recente?
        if(valorGravado.getValor() <= valorRecente.getValor()):
            valorEsperado =( ((valorRecente.getValor()-valorGravado.getValor())*(self.timeToMili(valorAtual.getDataHora())-self.timeToMili(valorGravado.getDataHora())) ) / (self.timeToMili(valorRecente.getDataHora())-self.timeToMili(valorGravado.getDataHora())) )+valorGravado.getValor()
        else:
            valorEsperado = ( ((valorGravado.getValor()-valorRecente.getValor())*(self.timeToMili(valorRecente.getDataHora())-self.timeToMili(valorRecente.getDataHora()))) / (self.timeToMili(valorRecente.getDataHora())-self.timeToMili(valorGravado.getDataHora())) )+self.timeToMili(valorRecente.getDataHora())
        print "Atual: %f"%valorAtual.getValor()+"esperado: %f"%valorEsperado+"Desv: %f"%desv+"recente: %f"%valorRecente.getValor()+"gravado: %f"%valorGravado.getValor()
        if(self.timeToMili(valorRecente.getDataHora())-self.timeToMili(valorRecente.getDataHora()) <300):
            if((valorAtual.getValor()>valorEsperado+desv)or(valorAtual.getValor()<valorEsperado-desv)):
                return False
            else:
                return True
        else:
            return False
        
    def timeToMili(self,stringTime):
        a = str(stringTime)
        temp = a.split(" ")
        dateString=temp[0].split("-")
        timeString=temp[1].split(":")
        dateTime = datetime.datetime(int(dateString[0]),int(dateString[1]),int(dateString[2]),int(timeString[0]),int(timeString[1]),int(timeString[2]))
        
        miliseg = time.mktime(dateTime.timetuple())*1000
        return float(miliseg)
        