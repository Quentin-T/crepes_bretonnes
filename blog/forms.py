from django import forms
from .models import Article, Profil



class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text='Cocher si vous souhaitez obtenir une copie du mail envoyé', required=False)

    def clean_message(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = self.cleaned_data.get('sujet')
        message = self.cleaned_data.get('message')

        if sujet and message:

            if "pizza" in message and "pizza" in sujet:
                raise forms.ValidationError("On ne parle pas de pizza ici !")
        return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()


class NouveauProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = '__all__'

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

