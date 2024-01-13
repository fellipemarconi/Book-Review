from django.shortcuts import render, redirect, get_object_or_404
from booklist.models import Book, Comment
from django.core.paginator import Paginator
from django.db.models import Q
from booklist.forms import CommentForm
from datetime import datetime

# Create your views here.

def index(request):
    books = Book.objects.all().order_by('title')
    
    paginator = Paginator(books, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    
    return render(request, 'booklist/index.html', context)

def search(request):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('booklist:index')
    
    books = Book.objects.filter(
        Q(title__icontains=search_value) |
        Q(genre__icontains=search_value) |
        Q(year__icontains=search_value)
    ).order_by('title')
    
    paginator = Paginator(books, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_value': search_value,
    }
    
    return render(request, 'booklist/index.html', context)

def book_detail(request, book_id):
    single_book = get_object_or_404(
        Book.objects, pk=book_id
    )
    book_name = single_book.title
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=single_book)
        
        context = {
            'book': single_book,
            'site_title': book_name,
            'form': form,
        }

        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['body']
            comment = Comment(book=single_book, name=name, body=body, data_added=datetime.now())
            comment.save()
            return redirect('booklist:book', book_id=book_id)
    
        return render(request, 'booklist/book_detail.html', context)
        
    context = {
    'book': single_book,
    'site_title': book_name,
    'form': CommentForm(),
    }
    
    return render(request, 'booklist/book_detail.html', context)
