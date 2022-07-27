from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import login, authenticate, logout
from django.core.files import File
from main.models import Product
from main.models import Contact
from main.forms.form import ContactForm
from main.forms.form import LoginForm
from main.forms.form import ProductForm
from main.forms.form import SignupForm

def index(request):
    products = Product.objects.all()
    return render(request,'main/index.html', context={
                                                      "products" : products, 
                                                      "add_product" : request.user.has_perm('main.add_product'),
                                                      "delete_product" : request.user.has_perm('main.delete_product'),
                                                      })

def detail(request, id):
    product = Product.objects.get(pk=id)
    return render(request,'main/detail.html', context={"product" : product})

def add_product(request):
    if request.method == 'GET':
        form = ProductForm()
    else:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('/')
            
    return render(request, "main/add_product.html", {'form': form})

def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('/')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            contact = Contact(email=email, subject=subject,message=message)
            contact.save()
            # try:
            #     send_mail(subject, message, email, ['noemie.tandol@gmail.com'])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            return render(request,"main/contact.html", {'form': form,'success' : 'Mail envoyé avec succès !'})
            
    return render(request, "main/contact.html", {'form': form})

def connexion(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                message = 'Identifiants invalides.'
                return render(request, 'main/connexion.html', context={'form': form,'message': message})
    return render(request, 'main/connexion.html', context={'form': form})

def inscription(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect('/')
    return render(request, 'main/inscription.html', context={'form': form})

def deconnexion(request):
    logout(request)
    return redirect('/')
