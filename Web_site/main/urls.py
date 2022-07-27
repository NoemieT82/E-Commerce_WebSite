from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("detail/<int:id>",views.detail, name="detail"),
    path("add_product/",views.add_product, name="Ajouter"),
    path("supprimer/<int:id>",views.delete, name="supprimer"),
    path("contact/",views.contact, name="contact"),
    path("inscription/",views.inscription, name="inscription"),
    path("connexion/",views.connexion, name="connexion"),
    path("deconnexion/",views.deconnexion, name="deconnexion"),
]