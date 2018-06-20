from django.forms import ModelForm
from .models import Planejamento

class SolicitacaoForm(ModelForm):
    class Meta:
        model = Planejamento
        fields = ['id_turma']
