from django.shortcuts import render
from django.shortcuts import render
from .models import Market_place
def Home (request):
    return render (request,'home.html')
# Create your views here.

def home(request):
    art= Market_place.objects.all()
    context= {
        'art': art,
    }

    return render (request,'home.html',context=context)