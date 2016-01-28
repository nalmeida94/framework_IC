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
    __lastValueTag={}

    def __init__(self,bd):
        self.__bd = bd
        self.__valoresDao = ValoresDao(self.__bd)
        self.__snapshotDao = SnapshotDao(self.__bd)
        self.__tagDao = TagDao(self.__bd)
        
        #TODO: Buscar valores gravados
        #self.__valorGravado = self.__valoresDao.retrieve(1)
    
    def lerDados(self,mensagem):
        flag=0
        mensagem = mensagem.split("&")
        id = mensagem[0]
        valor = mensagem[1]
        data_Hora = mensagem[2]
        valorRecente = Valores(valor, data_Hora, int(id))
        
        try:
            valorGravado=self.__lastValueTag[valorRecente.getIdTag()]
        except Exception:
            try:
                valorGravado = self.__valoresDao.last(valorRecente.getIdTag())
                self.__lastValueTag.update({valorRecente.getIdTag():valorGravado})
                #print "last"
            except Exception:
                self.__valoresDao.add(valorRecente)
                self.__lastValueTag.update({valorRecente.getIdTag():valorRecente})
                flag=1
                #print "valoresAdd"
        if (flag==0):
            try:
                valorAtual= self.__snapshotDao.retrieve(valorRecente.getIdTag())
                #print "retrieve"
            except Exception:
                flag=1
                self.__snapshotDao.add(Snapshot(float(valorRecente.getValor()), valorRecente.getDataHora(), int(valorRecente.getIdTag())))    
                #print "add"
                    
        if (flag==0):
            tag = self.__tagDao.retrieve(int(id))
            if not (self.testeParalelogramo(valorGravado, valorAtual, valorRecente, tag.getDesvio(), tag.getTempoMax())):
                self.__valoresDao.add(valorAtual)
                self.__lastValueTag[tag.getIdTag()]=valorAtual
            self.__snapshotDao.update(Snapshot(valorRecente.getValor(), valorRecente.getDataHora(), valorRecente.getIdTag(), valorRecente.getIdValores()))
    
    def testeParalelogramo(self,valorGravado,valorAtual,valorRecente,desv,tempo):
        if(valorGravado.getValor() <= valorRecente.getValor()):
            valorEsperado =((((valorRecente.getValor()-valorGravado.getValor())*(self.timeToMili(valorAtual.getDataHora())-self.timeToMili(valorGravado.getDataHora())))/(self.timeToMili(valorRecente.getDataHora())-self.timeToMili(valorGravado.getDataHora())))+valorGravado.getValor())
        else:
            valorEsperado = ((((valorGravado.getValor()-valorRecente.getValor())*(self.timeToMili(valorRecente.getDataHora())-self.timeToMili(valorAtual.getDataHora())))/(self.timeToMili(valorRecente.getDataHora())-self.timeToMili(valorGravado.getDataHora())))+valorRecente.getValor())
        print "Atual: %f"%valorAtual.getValor()+"esperado: %f"%valorEsperado+"Desv: %f"%desv+"recente: %f"%valorRecente.getValor()+"gravado: %f"%valorGravado.getValor()
        print "T-Atual: "+str(valorAtual.getDataHora())+"recente: "+str(valorRecente.getDataHora())+"gravado: "+str(valorGravado.getDataHora())
        if((self.timeToMili(valorRecente.getDataHora())-self.timeToMili(valorGravado.getDataHora())) <tempo):
            if(((valorAtual.getValor()>=valorEsperado+(valorEsperado*desv)))or(valorAtual.getValor()<valorEsperado-(valorEsperado*desv))):
                print "salva valor"
                return False 
            else:
                print "n salva"
                return True
        else:
            print "salva tempo- %f"%(self.timeToMili(valorRecente.getDataHora())-self.timeToMili(valorGravado.getDataHora()))
            return False
    def timeToMili(self,stringTime):
        a = str(stringTime)
        temp = a.split(" ")
        dateString=temp[0].split("-")
        timeString=temp[1].split(":")
        dateTime = datetime.datetime(int(dateString[0]),int(dateString[1]),int(dateString[2]),int(timeString[0]),int(timeString[1]),int(timeString[2]))
        miliseg = time.mktime(dateTime.timetuple())*1000
        return float(miliseg)