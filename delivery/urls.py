from django.conf.urls.defaults import *

urlpatterns = patterns('delivery.views',
    url(r'^remedios', 'listar_remedios', name = 'listar_remedios'),
)
