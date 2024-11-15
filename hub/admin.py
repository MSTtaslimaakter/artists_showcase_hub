from django.contrib import admin
from .models import Market_place,Artist, ArtPiece,Category, ArtPieceCategory, UserProfile
admin.site.register(Market_place)
admin.site.register(Artist)
admin.site.register(ArtPiece)
admin.site.register(Category)
admin.site.register(ArtPieceCategory)
admin.site.register(UserProfile)
# Register your models here.
