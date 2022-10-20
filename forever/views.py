import imp
from django.shortcuts import render,redirect
from django.urls import reverse
from numpy import imag
from .forms import ContactForm
from .models import Video,Image,About,Homee





# Create your views here.
 


def Videos(request):
    video = Video.objects.all()
    return render(request,"forever/videos.html",{'video':video})


def Pictures(request):
    pics = Image.objects.all()
    return render(request,"forever/pictures.html",{'pics':pics})
    

def About_me(request):
    imag = About.objects.all()
    return render(request,"forever/about_me.html",{'imag':imag})

def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('forever:thank_you'))
    else:
        form = ContactForm()    
    return render(request,'forever/contact.html',context={'form':form})


def Home(request):
    
    imagee = Homee.objects.all()
    
    return render(request,"forever/home.html",{'imagee':imagee})

   

def Thank_you(request):
    return render(request,"forever/Thank_you.html")