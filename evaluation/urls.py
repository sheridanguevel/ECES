from django.urls import path
from . import views
from .views import VoirEtudiant

urlpatterns = [
    path('',views.acceuil,name='acceuil'),
    path('acceuil/',views.acceuil,name='acceuil'),
    path('voiretudiant/<int:pk>',VoirEtudiant.as_view(),name='voiretudiant'),
    path('etudiant/',views.etudiant,name='etudiant'),
]
