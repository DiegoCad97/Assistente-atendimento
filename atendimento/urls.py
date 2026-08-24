from django.urls import path
from . import views
 
urlpatterns = [
 
    path("", views.home, name="home"),
 
    path(
        "emergencial/",
        views.emergencial,
        name="emergencial"
    ),
 
    path(
        "tipo/",
        views.tipo_ocorrencia,
        name="tipo_ocorrencia"
    ),
 
]
