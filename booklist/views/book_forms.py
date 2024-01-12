from django.shortcuts import render, get_object_or_404, redirect
from booklist.forms import BookForm
from django.contrib import messages

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

def book_delete(request, book_id):
    return render(request, 'booklist/login.html')