from django.contrib import admin
from .models import Planejamento, Motivo, Turma, Solicitacao

admin.site.register(Planejamento)
admin.site.register(Motivo)
admin.site.register(Turma)
admin.site.register(Solicitacao)
