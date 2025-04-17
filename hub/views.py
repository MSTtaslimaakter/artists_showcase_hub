from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ArtistForm
from django.shortcuts import render, get_object_or_404
from .forms import *
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
def artist_profile_details(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'artist_profile_details.html', {'artist': artist}) 
def upload_artist(request):
   form = ArtistForm()
   if request.method == 'POST':
       form = ArtistForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('home')
   context = {'form':form}
   return render(request, template_name = 'artist_form.html', context= context)
def update_artist(request,id):
   artist = Artist.objects.get(pk = id)
   form = ArtistForm(instance = artist)
   if request.method == 'POST':
       form = ArtistForm(request.POST, request.FILES,instance =artist)
       if form.is_valid():
           form.save()
           return redirect('home')
   context = {'form':form}
   return render(request, template_name = 'artist_form.html', context= context)
def delete_artist(request,id):
   artist = Artist.objects.get(pk=id)
   if request.method == 'POST':
       artist.delete()
       return redirect('home')
   return render(request, template_name = 'store\delete_artist.html')

def paintings_view(request):
    paintings = Painting.objects.all()  # Fetch all events from the correct model
    context = {
        'paintings': paintings
    }
    return render(request, 'paintings.html', context)

def illustrations_view(request):
    illustrations = Illustration.objects.all()  # Fetch all events from the correct model
    context = {
        'illustrations': illustrations
    }
    return render(request, 'event.html', context)

def handcraft_view(request):
    handcrafts = HandCraft.objects.all()  # Fetch all events from the correct model
    context = {
        'handcrafts': handcrafts
    }
    return render(request, 'event.html', context)

def abstractart_view(request):
    abstractarts = HandCraft.objects.all()  # Fetch all events from the correct model
    context = {
        'abstractarts': abstractarts
    }
    return render(request, 'abstractart.html', context)

def photography_view(request):
    photos = HandCraft.objects.all()  # Fetch all events from the correct model
    context = {
        'photos': photos
    }
    return render(request, 'photography.html', context)
   
