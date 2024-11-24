from django.contrib import admin
from .models import Event_s,Artist, ArtPiece,Category, ArtPieceCategory, UserProfile
admin.site.register(Event_s)
admin.site.register(Artist)
admin.site.register(ArtPiece)
admin.site.register(Category)
admin.site.register(ArtPieceCategory)
admin.site.register(UserProfile)