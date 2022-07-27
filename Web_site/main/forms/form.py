from django.forms import ModelForm
from django import forms
from main.models import Contact
from main.models import Product
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'