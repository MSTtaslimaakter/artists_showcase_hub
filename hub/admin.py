from django.contrib import admin
from .models import Event_s,Artist, ArtPiece,Category, ArtPieceCategory, UserProfile,Painting,Illustration,AbstractArt,HandCraft,Photography
admin.site.register(Event_s)
admin.site.register(Artist)
admin.site.register(ArtPiece)
admin.site.register(Category)
admin.site.register(ArtPieceCategory)
admin.site.register(UserProfile)
admin.site.register(Painting)
admin.site.register(Illustration)
admin.site.register(AbstractArt)
admin.site.register(HandCraft)
admin.site.register(Photography)