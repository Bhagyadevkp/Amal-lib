from django.urls import URLPattern, path
from . import views
from .views import *

urlpatterns = [

    path('Bookstall', views.Bookstall, name='Bookstall'),
    path('Returnbook/<int:id>', views.Returnbook, name='Returnbook'),
    path('Editbook/<int:id>', views.Editbook, name='Editbook'),
    path('Renewbook/<int:id>', views.Renewbook, name='Renewbook'),
    path('Deletebook/<int:id>', views.Deletebook, name='Deletebook'),
    path('Adminbook', views.Adminbook, name='Adminbook'),


]
