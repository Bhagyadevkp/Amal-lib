from django.urls import URLPattern, path
from . import views
from .views import *

urlpatterns = [
    # path('Questionpool', questionpool.as_view(), name='Questionpool'),
    path('Questionpool', views.Questionpool, name='Questionpool'),
    path('Adminquestion', views.Adminquestion, name='Adminquestion'),
    path('Addquestion', views.Addquestion, name='Addquestion'),
]