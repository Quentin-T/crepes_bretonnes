from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from blog.models import Article, Contact, Profil
from .forms import ContactForm, ArticleForm, NouveauContactForm, NouveauProfilForm, ConnexionForm
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

def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article':article})

def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():

        sujet=form.cleaned_data['sujet']
        message = form.changed_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        envoi = True

    return render(request,'blog/contact.html', locals())


def new_article(request):

    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'blog/new.html',locals())


def inscription(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True
        return redirect("voir_contacts")
    return render(request, 'blog/inscription.html', {'form': form, 'sauvegarde':sauvegarde})

def voir_contacts(request):
    return render(
        request, "blog/voir_contacts.html",{'contacts': Contact.objects.all()}
    )

def NouveauProfil(request):
    form = NouveauProfilForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('voir_profils')
    return render(request, 'blog/nouveauprofil.html', locals())

def voir_profils(request):
    return render(
        request, "blog/voir_profils.html",{'profils': Profil.objects.all()}
    )

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
            else:
                error=True
    else:
        form = ConnexionForm()

    return render(request,'blog/connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse("connexion"))

def dire_bonjour(request):
    if request.user.is_authenticated:
        return HttpResponse("Salut, {0} !".forma(request.user.username))
    return HttpResponse("Salut, anonyme!")