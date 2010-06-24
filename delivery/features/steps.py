#coding:utf-8
from freshen import *
from freshen.checks import *
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

@Then('eu deveria ver a listagem com o nome dos (\d+) remédios')
def verificar_conteudo_listagem(quantidade_remedios):
    for remedio in scc.remedios:
        conteudo_esperado = '<li>%s</li>' % remedio.nome
        assert_true(conteudo_esperado in scc.response.content)
