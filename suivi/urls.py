from  django.urls import  path
from  . import views

urlpatterns = [
   #Url de la fiche de prelevement
    path('home', views.home, name='home'),
    path('LignePlan/', views.itemsliste, name='itemsliste'),  
    path('LignePlan/Ajout/', views.addplanitems, name='addplanitems'),
    path('LignePlan/Edit/<int:id>/', views.editplanitems, name='editplanitems'),
    path('LignePlan/Dossier', views.dossier, name='dossier'),
    path('LignePlan/Dossier/Liste', views.listdoc, name='listdoc'),
    path('LignePlan/AddDossier/<int:id>/', views.adddossier, name='adddossier'),
    path('LignePlan/EditDossier/<int:dossier_id>/', views.editdossier, name='editdossier'),
    path('LignePlan/Dossier/Addlot/<int:id>/', views.adddlot, name='adddlot'),
    path('LignePlan/EditLot/<int:id>/', views.editlot, name='editlot'),
    path('LignePlan/Dossier/<int:dossier_id>/lots/', views.list_dossier_lots, name='dossier_lots'),
    path('LignePlan/Dossier/Suivi', views.suivi, name='suivi'),
    path('LignePlan/Dossier/Traitement', views.process_dossier, name='process_dossier'),
]




    