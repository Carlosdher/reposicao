from django.conf.urls import url
from . import views
app_name = 'reposicao'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^reposicao$', views.reposicao, name='formreposicao'),
    url(r'^historico$', views.historico, name='historico'),
    url(r'^adiantamento$', views.adiantamento, name='formadiantamento'),
    url(r'^troca$', views.troca, name='formtroca'),
]
