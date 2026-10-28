from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [path('admin/', admin.site.urls), path('', views.home, name='home'), path('products/', views.products, name='products'), path('calculator/', views.calculator, name='calculator'), path('about/', views.about, name='about'), path('contact/', views.contact, name='contact'), path('privacy/', views.privacy, name='privacy')]
