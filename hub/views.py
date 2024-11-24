from django.shortcuts import render
from django.shortcuts import render
from .models import *
def Home (request):
    return render (request,'home.html')

def About (request):
    return render (request,'about.html')    

def Profile (request):
    return render (request,'profile.html')

def Event (request):
    return render (request,'event.html')

def Sign_in (request):
    return render (request,'sign_in.html')

def Log_in (request):
    return render (request,'log_in.html')

def Gallery (request):
    return render (request,'gallery.html')

def Artist_profile (request):
    return render (request, 'artist_profile.html')

def Joshua_smith (request):
    return render (request, 'josh.html')

def Camilia_colin (request):
    return render (request, 'camilia.html')

def Payment_process (request):
    return render (request, 'payment.html')

def Jack_will (request):
    return render (request, 'jack.html')

def Purchased (request):
    return render (request, 'purchase.html')

def Camilia_art1 (request):
    return render (request, 'camiliaart1.html')

def Camilia_art2 (request):
    return render (request, 'camiliaart2.html')

def Camilia_art3 (request):
    return render (request, 'camiliaart3.html')

def Jacks_art1 (request):
    return render (request, 'jackart1.html')

def Jacks_art2 (request):
    return render (request, 'jackart2.html')

def Jacks_art3 (request):
    return render (request, 'jackart3.html')

def Joshuas_art1 (request):
    return render (request, 'joshuaart1.html')

def Joshuas_art2 (request):
    return render (request, 'joshuaart2.html')

def Joshuas_art3 (request):
    return render (request, 'joshuaart3.html')

def Paintings (request):
    return render (request, 'paintings.html')
def Illustrations (request):
    return render (request, 'illustrations.html')
def Handcraft (request):
    return render (request, 'handcraft.html')
def Photography (request):
    return render (request, 'photography.html')
def Abstractart (request):
    return render (request, 'abstractart.html')


# Create your views here.

def home(request):
    art= Market_place.objects.all()
    context= {
        'art': art,
    }

    return render (request,'home.html',context=context)
def about(request):
    art= Market_place.objects.all()
    context= {
        'art': art,
    }

    return render (request,'about.html',context=context)
def artist(request):
    artists=Artist.objects.all()
    context={
       'artists': artists,
    }
    return render (request,'artist_profile.html',context=context)
    