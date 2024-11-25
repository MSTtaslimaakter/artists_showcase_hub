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
from .import settings
from django.conf.urls.static import static






urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='Home'),
    path('about/',views.About,name='About'),
    path('profile/',views.Profile,name='Profile'),
    path('event/', views.event_page, name='event'),
    path('sign_in/',views.Sign_in,name='Sign_in'),
    path('log_in/',views.Log_in,name='Log_in'),
    path('gallery/', views.gallery_view, name='Gallery'),
    path('artist_profile/',views.artist,name='artist_profile'),
    path('payment_process/',views.Payment_process,name='Payment_process'),
    path('purchase/',views.Purchased,name='Purchased'),
    path('paintings/', views.Paintings, name='paintings'),
    path('illustrations/', views.Illustrations, name='illustrations'),
    path('handcrafts/', views.Handcraft, name='handcrafts'),
    path('photography/', views.Photography, name='photography'),
    path('abstractart/', views.Abstractart, name='abstractart'),
    path('artist_id/<str:id>',views.artist_profile_details, name = 'artist_profile_details'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)