#coding:utf-8
from freshen import *
from delivery.models import Remedio

@Given('que existem (\d+) remédios cadastrados no banco de dados')
def gravar_remedios(quantidade_remedios):
    scc.remedios = []
    for i in xrange(int(quantidade_remedios)):
        remedio = Remedio()
        remedio.nome = 'Remédio %d' %(i + 1)
        scc.remedios.append(remedio)
