from django.shortcuts import render
from .forms import AtendimentoInicialForm
from .perguntas import PERGUNTAS
 
 
def home(request):
    return render(request, "atendimento/home.html")
 
 
def emergencial(request):
    form = AtendimentoInicialForm()
    return render(request, "atendimento/emergencial.html", {"form": form})
 
 
def tipo_ocorrencia(request):
    return render(
        request,
        "atendimento/tipo_ocorrencia.html",
        {"tipos": PERGUNTAS.keys()}
    )