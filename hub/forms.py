from django.forms import ModelForm
from .models import *


class ArtistForm(ModelForm):
   class Meta:
       model = Artist
       fields = '__all__'