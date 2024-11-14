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