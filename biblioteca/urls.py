from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('libri/', views.lista_libri, name='lista'),
    path('libri/<int:id>/', views.dettaglio_libro, name='dettaglio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('autori/', views.autori, name='autori'),
]