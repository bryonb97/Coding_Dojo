from django.shortcuts import render, HttpResponse
from apps.books_authors_app.models import *

# Create your views here.
def index(request):
    c_sharp = Book.objects.create(title='C Sharp', desc='A description')
    java = Book.objects.create(title='Java', desc='A description')
    python = Book.objects.create(title='Python', desc='A description')
    php = Book.objects.create(title='PHP', desc='A description')
    ruby = Book.objects.create(title='Ruby', desc='A description')

    jane = Author.objects.create(name="Jane Austen")
    emily = Author.objects.create(name='Emily Dickinson')
    fyodor = Author.objects.create(name='Fyodor Dostoevsky')
    william = Author.objects.create(name='William Shakespeare')
    lau = Author.objects.create(name='Lau Tzu')

    jane.books.add(c_sharp, java)
    emily.books.add(c_sharp, java, python)
    fyodor.books.add(c_sharp, java, python, php)
    # fyodor.books.add(Book.objects.get().all())

    context = {
        'all_authors': Author.objects.all(),
    }
    return render(request, 'books_authors_app/index.html', context)