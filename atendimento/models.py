from django.db import models
 
 
class Ocorrencia(models.Model):
 
    TIPO_CHOICES = [
        ("EM", "Emergencial"),
        ("NE", "Não Emergencial"),
    ]
 
    nome_solicitante = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    resumo = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.nome_solicitante