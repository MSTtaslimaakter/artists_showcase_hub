"""
URL configuration for artshowcase project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hub import views 
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='Home'),
    path('about/',views.About,name='About'),
    path('profile/',views.Profile,name='Profile'),
    path('event/',views.Event,name='Event'),
    path('sign_in/',views.Sign_in,name='Sign_in'),
    path('log_in/',views.Log_in,name='Log_in'),
    path('gallery/',views.Gallery,name='Gallery'),
    path('artist_profile/',views.Artist_profile,name='Artist_profile'),
    path('joshua_smith/',views.Joshua_smith,name='Joshua_smith'),
    path('camilia_colins/',views.Camilia_colins,name='Camilia_colins'),
    path('jack_will/',views.Jack_will,name='Jack_will'),
    path('payment_process/',views.Payment_process,name='Payment_process'),
    path('purchase/',views.Purchased,name='Purchased'),
    path('camilias_art1/',views.Camilias_art1,name='Camilia_art1'),
    path('camilias_art2/',views.Camilias_art2,name='Camilia_art2'),
    path('camilias_art3/',views.Camilias_art3,name='Camilia_art3'),
    path('jacks_art1/',views.Jacks_art1,name='Jacks_art1'),
    path('jacks_art2/',views.Jacks_art2,name='Jacks_art2'),
    path('jacks_art3/',views.Jacks_art3,name='Jacks_art3'),
    path('joshuas_art1/',views.Joshuas_art1,name='Joshuas_art1'),
    path('joshuas_art2/',views.Joshuas_art2,name='Joshuas_art2'),
    path('joshuas_art3/',views.Joshuas_art3,name='Joshuas_art3'),
    path('paintings/', views.Paintings, name='Paintings'),
    path('illustrations/', views.Illustrations, name='Illustrations'),
    path('handcrafts/', views.Handcraft, name='HandCrafts'),
    path('photography/', views.Photography, name='Photography'),
    path('abstractart/', views.Abstractart, name='AbstractArt'),

    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
