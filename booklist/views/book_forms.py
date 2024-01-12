from django.shortcuts import render, get_object_or_404, redirect
from booklist.forms import BookForm
from django.contrib import messages
from booklist.models import Book
from django.urls import reverse

def book_create(request):
    if not request.user.is_authenticated:
        return redirect('booklist:login')
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        
        context = {
            'form': form,
        }
        
        if form.is_valid:
            book = form.save()
            messages.success(request, 'Book has been created')
            return redirect('booklist:book', book_id=book.pk)
    
        return render(request, 'booklist/book_create.html', context)
    
    context = {
        'form': BookForm(),
    }
    
    return render(request, 'booklist/book_create.html', context)

def book_update(request, book_id):
    if not request.user.is_authenticated:
        return redirect('booklist:login')
    
    book = get_object_or_404(Book, pk=book_id)
    form_action = reverse('booklist:update', args=(book_id,))
    
    if request.method == 'POST':
        
        form = BookForm(request.POST, request.FILES, instance=book)
        
        context = {
            'form': form,
            'form_action': form_action,
        }
        
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Book has been updated')
            return redirect('booklist:book', book_id=book.pk)
        
        return render(request, 'booklist/book_update.html', context)
    
    context = {
            'form': BookForm(instance=book),
            'form_action': form_action,
        }
    
    
    return render(request, 'booklist/book_update.html', context)

def book_delete(request, book_id):
    return render(request, 'booklist/login.html')