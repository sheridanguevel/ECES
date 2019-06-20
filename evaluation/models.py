from django.db import models
from django.contrib import admin

class Etudiant(models.Model):
    #photo=models.ImageField(upload_to='static/images/')
    photo=models.ImageField()
    matricule=models.CharField(max_length=10)
    nom=models.CharField(max_length=30)
    prenom=models.CharField(max_length=60)
    adresse=models.CharField(max_length=100)
    option=models.CharField(max_length=100)
    niveau=models.CharField(max_length=50)
    description=models.TextField()
    def __str__(self):
        return self.nom.upper()+" "+ self.prenom.capitalize()

class EtudiantAdmin(admin.ModelAdmin):
    list_display=('matricule','nom','prenom','adresse','option','niveau','description','photo')

class EtudiantChamp(admin.StackedInline):
    model=Etudiant
    extra=3
