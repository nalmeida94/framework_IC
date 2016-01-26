'''
Created on 23/12/2014

@author: Marcelo
'''

from dao.DataSourceDao import DataSourceDao
from dao.NodeDao import NodeDao
from dao.RadioTipoDao import RadioTipoDao
from dao.RadioDao import RadioDao
from dao.ValoresDao import ValoresDao
from dao.SnapshotDao import SnapshotDao
from dao.TagInfoDao import TagInfoDao
from dao.TagDao import TagDao

from model.Node import Node
from model.DataSource import DataSource
from model.RadioTipo import RadioTipo
from model.Radio import Radio
from model.Valores import Valores
from model.Snapshot import Snapshot
from model.TagInfo import TagInfo
from model.Tag import Tag

from controller.SerialPort import SerialPort
from controller.BancoDeDados import BancoDeDados
from controller.NodeSync import NodeSync
from lib2to3.fixer_util import String

bd =''
nodeSync =''

if __name__ == '__main__':
    
    bd=BancoDeDados()
    nodeSync = NodeSync(bd)
    
    #getting all serial devices detected
    #change it if necessary
    a="7&15.1&2014-02-16 6:09:08"
    b="7&15.1&2014-02-16 6:10:08"
    c="7&14.2&2014-02-16 6:11:08"
    d="7&80.1&2014-02-16 6:12:08"
   
    e="7&16.5&2014-02-16 6:13:08"
    f="7&.5&2014-02-16 6:14:08"
    g="7&84.5&2014-02-16 6:15:08"
    h="7&84.5&2014-02-16 6:16:08"
    i="7&84.5&2014-02-16 6:50:08"
    i1="7&24.5&2014-02-16 6:51:08"
    i2="7&24.5&2014-02-16 6:52:08"
    i3="7&50.5&2014-02-16 6:53:08"
    nodeSync.lerDados(a)
    nodeSync.lerDados(b)
    nodeSync.lerDados(c)
    nodeSync.lerDados(d)
    nodeSync.lerDados(e)
    nodeSync.lerDados(f)
    nodeSync.lerDados(g)
    nodeSync.lerDados(h)
    nodeSync.lerDados(i)
    nodeSync.lerDados(i1)
    nodeSync.lerDados(i2)
    nodeSync.lerDados(i3)