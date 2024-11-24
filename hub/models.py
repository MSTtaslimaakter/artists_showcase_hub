from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Market_place(models.Model):
    Artname=models.TextField(max_length=100)
    Arttype=models.TextField(max_length=100)
    Price=models.DecimalField(max_digits=10, decimal_places=2)
    Artid=models.IntegerField()
   

    def __str__(self):
        return self.Artname



class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='artist_pics/')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100)
    social_links = models.JSONField(blank=True, null=True)  # Store links as JSON (e.g., Instagram, Twitter)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ArtPiece(models.Model):
    art_piece_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    artist = models.ForeignKey(Artist, related_name='art_pieces', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    medium = models.CharField(max_length=50)  
    size = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='art_pieces/')
    creation_date = models.DateField()
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    url_name = models.CharField(max_length=100, default='default_url')

    def __str__(self):
        return self.name


class ArtPieceCategory(models.Model):
    art_piece = models.ForeignKey(ArtPiece, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['art_piece', 'category']

    def __str__(self):
        return f"{self.art_piece.title} - {self.category.name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username