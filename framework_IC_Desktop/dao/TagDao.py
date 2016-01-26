'''
Created on 19/04/2015

@author: Marcelo
'''

from model.Tag import Tag
 
class TagDao(object):
    '''
    classdocs
    '''
    __banco=''
    def __init__(self, banco):
        '''
        Constructor
        '''
        self.__banco = banco    
    def add(self,tag):
        sql = "INSERT INTO tag(DESVIO, TEMPO_MAX, CONV_RATE, tagInfo_idtagInfo1, datasource_idESTACAO_METEO) VALUES (%f"%tag.getDesvio()+",%d"%tag.getTempoMax()+",%d"%tag.getConvRate()+",%d"%tag.getTagInfo()+",%d"%tag.getIdEstacaoMeteo()+");"
        return self.__banco.exe(sql)
    def remove(self,id):
        sql = "DELETE FROM tag WHERE idTAG= %d"%id
        return self.__banco.exe(sql)
    def update(self,tag):
        sql = "UPDATE tag SET DESVIO=%f"%tag.getDesvio()+", TEMPO_MAX=%d"%tag.getTempoMax()+",CONV_RATE=%d"%tag.getConvRate()+",tagInfo_idtagInfo1=%d"%tag.getTagInfo()+", datasource_idESTACAO_METEO=%d"%tag.getIdEstacaoMeteo()+" WHERE idTAG= %d"%tag.getIdTag()
        return self.__banco.exe(sql)
    def retrieve(self,id):
        sql = "SELECT * FROM tag WHERE idTag= %d"%id
        self.__banco.exe(sql)
        stringTag=self.__banco.cursor.fetchone()
        return Tag(stringTag[1], stringTag[2], stringTag[3], stringTag[4], stringTag[5],stringTag[0])
    def getAll(self):
        sql = "SELECT idTAG FROM `tag`ORDER BY idTAG"
        self.__banco.exe(sql)
        stringTag = self.__banco.cursor.fetchall()
        cont=0
        idTagList=''
        while True:
            try:
                if stringTag[cont][0]!=None:
                    idTagList += "%d "%stringTag[cont][0]
                    cont=cont+1
            except Exception:
                break
        return idTagList