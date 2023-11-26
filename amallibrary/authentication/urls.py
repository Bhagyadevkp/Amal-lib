from django.urls import URLPattern, path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('Login', Login.as_view() , name='Login'),
    path('Admindashboard', views.Admindashboard, name='Admindashboard'),
    path('Adminsettings', views.Adminsettings, name='Adminsettings'),
    path('Adminuserview', views.Adminuserview, name='Adminuserview'),
    path('Studentregister', views.Studentregister , name='Studentregister'),
    path('Staffregister', views.Staffregister, name='Staffregister'),
    path('Quesadminregister', views.Quesadminregister, name='Quesadminregister'),
    path('Registrationtype', views.Registrationtype , name='Registrationtype'),
    path('Deletequesadmin/<int:id>', views.Deletequesadmin, name='Deletequesadmin'),
    path('Deletestaff/<int:id>', views.Deletestaff, name='Deletestaff'),
    path('Deletestudent/<int:id>', views.Deletestudent, name='Deletestudent'),
    path('Profile', views.Profile, name='Profile'),
    path('Logout',views.Logout,name='Logout'),
]