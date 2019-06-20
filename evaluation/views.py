from django.shortcuts import render
#from django.http import Http404
from django.views.generic import ListView,DetailView;
from .models import Etudiant
import datetime

def acceuil(request):
    local=datetime.date.today()
    return render(request,'pages/acceuil.html',{'local':local})

def etudiant(request):
    etudiant=Etudiant.objects.all()
    return render(request,'pages/etudiant.html',{'etudiant':etudiant})

def voiretudiant(request):
    voir=Etudiant.objects.get(pk=id)
    return render(request,'pages/voiretudiant.html',{'voir':voir})

def page_non_trouvee(request):
    return render(request,'erreur/404.html')

def erreur_serveur(request):
    return render(request,'erreur/500.html')

class VoirEtudiant(DetailView):
        model=Etudiant
        template_name='pages/voiretudiant.html'
        def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            return context
