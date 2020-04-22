from django.urls import path
from . import views
urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>', views.addition),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('contact/', views.contact, name='contact'),
    path('new/', views.new_article, name='new'),
    path('inscription/', views.inscription, name="inscription"),
    path('voir_contacts/', views.voir_contacts, name="voir_contacts"),
    path('nouveauprofil/', views.NouveauProfil, name="nouveauprofil"),
    path('voir_profils/', views.voir_profils, name="voir_profils"),
    path('connexion/', views.connexion, name="connexion"),
    path('deconnexion/', views.deconnexion, name="deconnexion"),
]
