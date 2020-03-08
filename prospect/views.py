from django.shortcuts import render
from .forms import ProspetForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Prospet
import datetime

# Template crud create read update delete.
def index(request):
    return render(request,'./index/index.html')

def create(request):
    if request.method == 'POST':
        form = ProspetForm(request.POST)
        if form.is_valid():
            prospet = Prospet()
            prospet.nom=form.cleaned_data["nom"]
            prospet.prenom=form.cleaned_data["prenom"]
            e = form.cleaned_data["date_de_naissance"]
            prospet.date_de_naissance = e 
            prospet.save()
            return HttpResponseRedirect('')
    else:
            form = ProspetForm()
            return render(request,'./prospect/create.html',{'form':form})



def info(request, prospet_id):
    prospet = Prospet.objects.get(pk=prospet_id)
    return render(request, './prospect/info.html', {'prospet': prospet})