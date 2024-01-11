from django.shortcuts import render
from booklist.models import Book
from django.core.paginator import Paginator

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