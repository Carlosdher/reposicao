from django.shortcuts import render
from .models import Planejamento
from .form import SolicitacaoForm
# Create your views here.

def requerimento(request):
    form = SolicitacaoForm()
    context = {
        'form': form,
    }
    template_name = 'requeri.html'
    return render(request,template_name,context)

def home(request):
    template_name = 'index.html'
    return render(request,template_name)
