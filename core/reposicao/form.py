from django import forms
from .models import Solicitacao

class SolicitacaoForm(forms.ModelForm):

    class Meta:
        model = Solicitacao

        fields = [
        'justification',
        'date_miss_start',
        'date_miss_end',
        'reason',
        'othes',
        'team',
        ]

        labels = {
        'justification': 'Justificativa:',
        'date_miss_start': 'Data inicial da falta:',
        'date_miss_end': 'Data final da falta:',
        'reason': 'Motivo:',
        'othes': 'Outro:',
        'team': 'Turma:',
        }

        widgets = {
        'justification': forms.TextInput(),
        'date_miss_start': forms.DateInput(),
        'date_miss_end': forms.DateInput(),
        'reason': forms.Select(),
        'othes': forms.TextInput(),
        'team': forms.Select(),
        }
