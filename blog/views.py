from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Article
# Create your views here.

def home(request):
    return HttpResponse("""
        <h1>Bienvenue sur mon blog!</h1>
        <p>Les crêpes bretonnes servent à gagner les campagnes</p>
        """)

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2
    return render(request, 'blog/addition.html', locals())

def accueil(request):
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article':article})