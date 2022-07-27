from xml.parsers.expat import model
from django.db import models
from django import forms

# Produit

class Product(models.Model):
    # Titre
    titre = models.CharField(max_length=100)

    # Description
    description = models.TextField(max_length=2000)
    
    # Prix
    prix =  models.DecimalField(default=00.00,max_digits=5, decimal_places=2)
   
    # Quantité
    stock = models.IntegerField(default=0, blank=True, null=True)

    #Matière
    matiere = models.CharField(max_length=200, blank=True, null=True)
    
    #Taillle
    taille = models.CharField(max_length=200, blank=True, null=True)
    
    # Image
    image = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return self.titre

class Contact(models.Model):
    # Email
    email = models.EmailField(max_length=200,blank=False,null=False)

    # Subject
    subject = models.CharField(max_length=200,blank=False,null=False)

    # Message
    message = models.TextField(blank=False,null=False)