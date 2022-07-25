from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.forms import ModelForm
from main.models import Product
from main.models import Contact

def index(request):
    products = Product.objects.all()
    return render(request,'main/index.html', context={"products" : products})

def detail(request, id):
    product = Product.objects.get(pk=id)
    return render(request,'main/detail.html', context={"product" : product})



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # try:
            #     send_mail(subject, message, email, ['noemie.tandol@gmail.com'])
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')
            return render(request,"main/contact.html", {'form': form,'success' : 'Mail envoyé avec succès !'})
            
    return render(request, "main/contact.html", {'form': form})


