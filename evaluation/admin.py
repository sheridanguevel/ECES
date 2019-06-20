from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Etudiant,EtudiantAdmin,EtudiantChamp
from django.contrib.auth.models import User, Group

# Register your models here.
class EcesAdmin(AdminSite):
    site_header='ECES ETUDIANT'
    index_title='Administration du site ECES'
    search_fields = ['nom', 'prenom']
    class Media:
        js=('js/admin/placeholder.js', )

admin.site=EcesAdmin(name='admin')
admin.site.register(Etudiant,EtudiantAdmin)
#admin.site.register(EtudiantChamp)
