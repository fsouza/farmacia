#coding:utf-8
from freshen import *
from delivery.models import Remedio

from ludibrio import Mock
from django.test.client import Client

@Given('que existem (\d+) remédios cadastrados no banco de dados')
def gravar_remedios(quantidade_remedios):
    scc.remedios = []
    for i in xrange(int(quantidade_remedios)):
        remedio = Remedio()
        remedio.nome = 'Remédio %d' %(i + 1)
        scc.remedios.append(remedio)

@When('eu vou para a página de listagem de remédios')
def visitar_pagina_listagem():
    with Mock() as delivery:
        from delivery.models import Remedio
        Remedio.objects.all() >> scc.remedios
    client = Client()
    scc.response = client.get('/delivery/remedios')
    delivery.validate()
