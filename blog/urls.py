from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.accueil, name='accueil'),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>', views.addition),
    path('article/<int:id>', views.lire, name='lire')
]
