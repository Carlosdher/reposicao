from django.db import models
from app.core.models import CreateUpdateModel

class Planejamento(CreateUpdateModel):
    components = models.CharField(primary_key=True,  max_length=100, verbose_name='Componente Curricular')
    team = models.ForeignKey(Turma, on_delete=models.CASCADE)
    date_class = models.DateField(verbose_name='Data da Aula')
    date_restitution = models.DateField(verbose_name='Data da Reposição')
    descripition  = models.TextField(verbose_name='Descrição')

    class Meta:
        verbose_name='Planejamento'
        verbose_name_plural = 'Planejamentos'

class Motivo(CreateUpdateModel):
    name = models.CharField(max_length=100, verbose_name='Nome')

    class Meta:
        verbose_name='Motivo'
        verbose_name_plural='Motivos'

class Turma(CreateUpdateModel):
    nome = models.CharField('nome',max_length=100)
    period = models.IntegerField(verbose_name='Período')

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'



class Solicitacao(CreateUpdateModel):
    user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE)
    justification = models.TextField(verbose_name='Justificativa')
    date_miss_start = models.DateField(verbose_name='Data da Falta Inicial')
    date_miss_end = models.DateField(verbose_name='Data da Falta Final')
    reason = models.ForeignKey(Motivo, on_delete = models.CASCADE)
    othes = models.CharField(max_length=200, null=True, blank=True, verbose_name='Outros' )
    team = models.ForeignKey(Turma, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'
