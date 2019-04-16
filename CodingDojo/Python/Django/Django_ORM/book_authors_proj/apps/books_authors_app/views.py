from django.shortcuts import render, redirect, HttpResponse
from apps.books_authors_app.models import *

# Create your views here.
def showBooks(request):
    # fyodor.books.add(Book.objects.get().all())

    context = {
        'books': Book.objects.all(),
    }

    return render(request, 'books_authors_app/index.html', context)

def createBook(request):
    book = Book.objects.create(title=request.POST['titleBox'], desc=request.POST['descBox'])

    return redirect('/')

def viewBook(request, id):
    context = {
            'books': Book.objects.filter(id=id).values(),
        }

    return render(request, 'books_authors_app/view.html', context)

def removeBook(request, id):
    this_book = Book.objects.filter(id=id)
    this_book.delete()
    return redirect('/authors')

def showAuthors(request):

    context = {
        'authors': Author.objects.all(),
    }

    return render(request, 'books_authors_app/authors.html', context)

def createAuthor(request):
    author = Author.objects.create(name=request.POST['nameBox'], notes=request.POST['noteBox'])

    return redirect('/authors')

def viewAuthor(request, id):
    context = {
            'authors': Author.objects.filter(id=id).values(),
        }

    return render(request, 'books_authors_app/viewAuthor.html', context)

def removeAuthor(request, id):
    this_author = Author.objects.filter(id=id)
    this_author.delete()
    return redirect('/authors')