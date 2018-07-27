from django.shortcuts import render

def home(request):
    template_name = 'home.html'
    return render(request,template_name)

def reposicao(request):
    template_name = 'formreposicao.html'
    return render(request,template_name)

def historico(request):
    template_name = 'historico.html'
    return render(request,template_name)

def adiantamento(request):
    template_name = 'formadiantamento.html'
    return render(request,template_name)

def troca(request):
    template_name = 'formtroca.html'
    return render(request,template_name)
