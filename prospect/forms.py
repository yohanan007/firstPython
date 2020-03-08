from django import forms
import datetime

class ProspetForm(forms.Form):
    nom = forms.CharField(max_length = 100)
    prenom = forms.CharField(max_length = 100)
    date_de_naissance = forms.DateTimeField(initial=datetime.date.today)



