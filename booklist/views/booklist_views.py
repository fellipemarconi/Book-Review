from django.shortcuts import render
from booklist.models import Book

# Create your views here.

def index(request):
    books = Book.objects.all().order_by('title')
    
    context = {
        'books': books,
    }
    
    return render(request, 'booklist/index.html', context)