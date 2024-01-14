from django.shortcuts import render, redirect, get_object_or_404
from booklist.models import Book, Comment, BookReview
from django.core.paginator import Paginator
from django.db.models import Q
from booklist.forms import CommentForm, BookReviewForm
from datetime import datetime
from django.contrib import messages
from django.db.models import Avg

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
    
    # Rating
    rating = BookReview.objects.filter(
        book=single_book
    )
    
    average_rating = BookReview.objects.filter(
        book=single_book
    ).aggregate(rating=Avg('rating'))
    
    # Comments
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=single_book)
        form_rating = BookReviewForm(request.POST)
        
        context = {
            'book': single_book,
            'site_title': book_name,
            'form': form,
            'form': form_rating,
            'rating': rating,
            'average_rating': average_rating,
        }

        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['body']
            comment = Comment(book=single_book, name=name, body=body, owner=request.user, data_added=datetime.now())
            comment.save()
            return redirect('booklist:book', book_id=book_id)
        
        if form_rating.is_valid():
            user = request.user
            star_rating = form_rating.cleaned_data['rating']
            add_rating = BookReview(user=user, book=single_book, rating=star_rating)
            add_rating.save()
            return redirect('booklist:book', book_id=book_id)
    
        return render(request, 'booklist/book_detail.html', context)
        
    context = {
    'book': single_book,
    'site_title': book_name,
    'form': CommentForm(),
    'form_rating': BookReviewForm(),
    'rating': rating,
    'average_rating': average_rating,
    }
    
    return render(request, 'booklist/book_detail.html', context)

def delete_comment(request, comment_pk):
    if not request.user.is_authenticated:
        return redirect('booklist:login')
    
    comment = get_object_or_404(Comment, id=comment_pk, owner=request.user)
    book_id = comment.book.pk
    
    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment has been deleted')
        return redirect('booklist:book', book_id=book_id)
    
    context = {
        'comment': comment,
    }
    
    return render(request, 'booklist/book.html', context)