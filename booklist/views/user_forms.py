from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from booklist.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.models import User
# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('booklist:index')
    
    if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('password')
        
        user = auth.authenticate(
            request, 
            username=username, 
            password=password
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successful!')
            return redirect('booklist:index')
        messages.error(request, "Login Invalid!")
        
    return render(request, 'booklist/login.html')

def logout_user(request):
    if not request.user.is_authenticated:
        return redirect('booklist:login')
       
    auth.logout(request)
    messages.success(request, 'Logout Successful!')
    return redirect('booklist:login')

def register_user(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been created')
            return redirect('booklist:login')
        
    context = {
        'form': form,
    }
    
    return render(request, 'booklist/register.html', context)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('booklist:login')
    
    form = RegisterUpdateForm(instance=request.user)
    
    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)
        
        context = {
            'form': form,
        }
        
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been updated')
            return redirect('booklist:login')
    
    context = {
            'form': form,
        }
    
    return render(request, 'booklist/user_update.html', context)

def user_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('booklist:login')
    
    user = get_object_or_404(User, pk=pk)
    confirmation = request.POST.get('confirmation', 'no')
    form = RegisterUpdateForm(instance=request.user)
        
    if confirmation == 'yes':
        user.delete()
        messages.success(request, 'User has been deleted')
        return redirect('booklist:index')
        
    context = {
        'confirmation': confirmation,
        'user': user,
        'form': form,
    }
    
    return render(request, 'booklist/user_update.html', context)
    
