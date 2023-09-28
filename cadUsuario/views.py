from django.shortcuts import render
from .models import Users

def home(request):
    return render(request, 'users/home.html')

def user(request):
    newUser = Users()
    newUser.name = request.POST.get('name')
    newUser.age = request.POST.get('age')
    newUser.save()

    users = {
        'users': Users.objects.all()
    }
    return render(request, 'users/users.html', user)