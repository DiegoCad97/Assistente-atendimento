from django import forms
 
 
class AtendimentoInicialForm(forms.Form):
 
    nome = forms.CharField(
        label="Nome do solicitante",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "Digite o nome completo"
        })
    )
 
    telefone = forms.CharField(
        label="Telefone",
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "(00) 00000-0000"
        })
    )
 
    estado = forms.CharField(
        label="Estado",
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "Ex.: São Paulo"
        })
    )
 
    endereco = forms.CharField(
        label="Endereço",
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control form-control-lg",
            "placeholder": "Rua, número, bairro..."
        })
    )
 
    referencia = forms.CharField(
        label="Ponto de referência",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 4,
            "placeholder": "Ex.: Em frente ao mercado..."
        })
    )