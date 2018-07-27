from django import forms
from .models import Solicitacao

class SolicitacaoForm(forms.ModelForm):

    class Meta:
        model = Solicitacao

        fields = [
        'matricula',
        'id_solicitacao',
        'justicativa',
        'data_falta_inicio',
        'data_falta_fim',
        'data_reposicao',
        'data_aula',
        'motivo',
        'outro',
        'id_turma',
        'descricao',
        'Componente',
        ]

        labels = {
        'matricula': 'Matricula:',
        'justicativa': 'Justificativa:',
        'data_falta_inicio': 'Data inicial da falta:',
        'data_falta_fim': 'Data final da falta::',
        'data_reposicao': 'Data da reposição:',
        'data_aula': 'Data da aula:',
        'motivo': 'Motivo:',
        'outro': 'Outro:',
        'id_turma': 'Id da Turma:',
        'descricao': 'Descrição:',
        'Componente': 'Componente currícular:',
        }

        widgets = {
        'matricula': forms.Select(),
        'justicativa': forms.TextInput(),
        'data_falta_inicio': forms.DateInput(),
        'data_falta_fim': forms.DateInput(),
        'data_reposicao': forms.DateInput(),
        'data_aula': forms.DateInput(),
        'motivo': forms.Select(),
        'outro': forms.TextInput(),
        'id_turma': forms.Select(),
        'descricao': forms.Textarea(),
        'Componente': forms.Select(),
        }
