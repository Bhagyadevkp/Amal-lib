from django.urls import URLPattern, path
from . import views
from .views import *

urlpatterns = [
    path('Blogview/<int:id>', views.Blogview, name='Blogview'),
    path('Adminblog', views.Adminblog, name='Adminblog'),
    path('Bloglist', views.Bloglist, name='Bloglist'),
    path('Deleteblog/<int:id>', views.Deleteblog, name='Deleteblog'),
    path('Deletecomment/<int:id>', views.Deletecomment, name='Deletecomment'),
    # path('Addcomment', views.Addcomment, name='Addcomment'),


]