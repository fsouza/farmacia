# Create your views here.
from models import Remedio
from django.shortcuts import render_to_response
from django.template import RequestContext

def listar_remedios(request):
    remedios = Remedio.objects.all()
    return render_to_response('listar_remedios.html', {
            'remedios' : remedios
        }, context_instance=RequestContext(request)
    )
