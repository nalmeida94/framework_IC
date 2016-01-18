'''
Created on 10/12/2014

@author: Marcelo
'''
import MySQLdb

class BancoDeDados(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        #Lendo o Arquivo de configuracao
        self.arquivo = open('config.txt','r')
        self.config = self.arquivo.readlines()
        
        #Inicializa as variaveis do objeto com as configuracoes
        self.tipoBanco = self.config[0].split(':')
        self.tipoBanco = self.tipoBanco[1].lower().strip()
        
        self.host = self.config[1].split(':')
        self.host = self.host[1].strip()
        
        self.user = self.config[2].split(':')
        self.user = self.user[1].strip()
        
        self.senha = self.config[3].split(':')
        self.senha = self.senha[1].strip()
        
        self.bd = self.config[4].split(':')
        self.bd = self.bd[1].strip()

        #Verifica Qual o banco de dados escolhido e o inicializa a conexao
        if "mysql"==self.tipoBanco:
            self.cnx = MySQLdb.connect(self.host,self.user,self.senha,self.bd)
            self.cursor = self.cnx.cursor()
    
    def __del__(self):
        #Finaliza a conexao
        if "mysql"==self.tipoBanco:
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
    
    def exe(self,sql):
        #Executa o script sql
        if "mysql"==self.tipoBanco:
            self.cursor.execute(sql)
            #self.cnx.commit()