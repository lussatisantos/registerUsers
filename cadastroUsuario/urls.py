from django.urls import path
from cadUsuario import views

urlpatterns = [
    path('',views.home, name='home'),  
    path('users/',views.users, name='listUsers') 
]
