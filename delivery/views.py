# Create your views here.
from models import Remedio
from django.http import HttpResponse

def listar_remedios(request):
    Remedio.objects.all()
    return HttpResponse('')
