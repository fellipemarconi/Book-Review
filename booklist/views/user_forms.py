from django.shortcuts import render
from django.contrib import auth, messages

# Create your views here.

def login_user(request):
    return render(request, 'booklist/login.html')

