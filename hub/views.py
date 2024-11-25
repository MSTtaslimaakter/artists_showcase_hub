from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
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

def Payment_process (request):
    return render (request, 'payment.html')

def Purchased (request):
    return render (request, 'purchase.html')

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
    art= Event_s.objects.all()
    context= {
        'art': art,
    }

    return render (request,'home.html',context=context)
def about(request):
    art= Event_s.objects.all()
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


def gallery_view(request):
    categories = Category.objects.all()
    print(categories)  # Debug: Check if categories are being retrieved
    context = {
        'categories': categories,
    }
    return render(request, 'gallery.html', context)


def event_page(request):
    events = Event_s.objects.all()  # Fetch all events from the correct model
    context = {
        'events': events
    }
    return render(request, 'event.html', context)