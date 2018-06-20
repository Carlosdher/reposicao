from django.db import models

class Usuario(models.Model):
    matricula = models.CharField('matricula',max_length=100)
    tipo = models.CharField('tipo',max_length=100)
    nome = models.CharField('nome',max_length=100)
    senha = models.CharField('senha',max_length=100)
    email = models.EmailField('email',max_length=254)

    class Meta:
        verbose_name_plural = 'Usuários'

class Motivo(models.Model):
    id_motivo = models.IntegerField()
    descricao = models.TextField()

class Periodo(models.Model):
    id_periodo= models.IntegerField()
    nome = models.CharField('nome',max_length=100)

    class Meta:
        verbose_name_plural = 'Períodos'

class Turma(models.Model):
    id_turma = models.IntegerField()
    nome = models.CharField('nome',max_length=100)
    id_periodo = models.ForeignKey(Periodo, on_delete = models.CASCADE)

class Solicitacao(models.Model):
    matricula = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    id_solicitacao = models.IntegerField()
    justicativa = models.TextField()
    data_falta_inicio = models.DateField()
    data_falta_fim = models.DateField()
    data_reposicao = models.DateField()
    data_aula = models.DateField()
    motivo = models.ForeignKey(Motivo, on_delete = models.CASCADE)
    outro = models.CharField('outro',max_length=200, null=True, blank=True )

    class Meta:
        verbose_name_plural = 'Solicitações'
class Planejamento(models.Model):
    id_planejamento = models.IntegerField()
    data_aula = models.ForeignKey(Solicitacao,on_delete = models.CASCADE)
    id_turma = models.ForeignKey(Turma, on_delete = models.CASCADE)
    data_reposicao = models.ForeignKey(Solicitacao, related_name='data',on_delete = models.CASCADE)
    justificativa = models.ForeignKey(Solicitacao, related_name='justifi',on_delete = models.CASCADE)
