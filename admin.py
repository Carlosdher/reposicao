from django.contrib import admin
from .models import Usuario, Motivo, Periodo, Turma, Solicitacao, Planejamento

admin.site.register(Usuario)
admin.site.register(Motivo)
admin.site.register(Periodo)
admin.site.register(Turma)
admin.site.register(Solicitacao)
admin.site.register(Planejamento)
