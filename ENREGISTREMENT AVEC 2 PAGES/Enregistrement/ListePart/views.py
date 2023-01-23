from django.shortcuts import render,HttpResponseRedirect
from .forms import ParticipantResgistration
from .models import User
# Create your views here.

#Cette fonction permet d'ajouter les infomations sur les participants
def index(request):
    if request.method == 'POST':
        fm = ParticipantResgistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['nom']
            pnm = fm.cleaned_data['prénom']
            nme = fm.cleaned_data['numéro']
            mail = fm.cleaned_data['adresse_email']
            reg = User(nom = nm, prénom = pnm, numéro = nme, adresse_email = mail)
            reg.save()
            fm = ParticipantResgistration()
    else:
        fm = ParticipantResgistration()
    stud = User.objects.all()
    return render(request, 'store/index.html', context={'form':fm, 'stu':stud})


    #Cette fonction permet de modifier les données du participant selectioner
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = ParticipantResgistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk =id)
        fm = ParticipantResgistration(instance=pi)
    return render(request,'store/update.html', {'form':fm})


    #Cette fonction permet des supprimer les données du participant selectioner
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

   

def liste(request):
    if request.method == 'POST':
        fm = ParticipantResgistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['nom']
            pnm = fm.cleaned_data['prénom']
            nme = fm.cleaned_data['numéro']
            mail = fm.cleaned_data['adresse_email']
            reg = User(nom = nm, prénom = pnm, numéro = nme, adresse_email = mail)
            reg.save()
            fm = ParticipantResgistration()
    else:
        fm = ParticipantResgistration()
    stud = User.objects.all()
    return render(request, 'store/liste.html', context={'form':fm, 'stu':stud})
