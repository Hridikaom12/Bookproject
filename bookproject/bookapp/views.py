# bookapp/views.py

from django.shortcuts import render,redirect
from .models import Book
from .forms import AuthorForm, BookForm
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q



def listBook(request):
    books = Book.objects.all() 
    paginator = Paginator(books, 5)  
    page_number = request.GET.get('page')  
    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)

    return render(request, 'listbook.html', {'books': page, 'page': page})

def detailsView(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'detailview.html',{'book':book})

def updateBook(request, book_id):
    book =Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form = BookForm(instance=book)
    return render(request, 'updateview.html', {'form': form, 'book': book})

def deleteView(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('booklist')
    return render(request,'deleteview.html',{'book':book})

def createBook(request):
    book=Book.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form = BookForm()
    return render(request, 'book.html', {'form': form,'books':book})

def createAuthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booklist') 
    else:
        form = AuthorForm()
    return render(request, 'author.html', {'form': form})

def index(request):
    return render(request,'base.html')

def searchBook(request):
    query=None
    books=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))
    else:
        books=[]
    context={'books':books,'query':query}
    return render(request, 'search.html',context)



    

