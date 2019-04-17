from django.shortcuts import render, redirect, HttpResponse
from apps.tv_shows_app.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def createShow(request):
    show = TVShow.objects.create(title=request.POST['titleBox'], network=request.POST['networkBox'],
                                release_date=request.POST['releaseDateBox'], description=request.POST['descBox'])
    
    return redirect('/viewShows')

def viewShows(request):
    context = {
        'shows': TVShow.objects.all(),
    }
    return render(request, 'shows.html', context)

def viewShow(request, id):
    context = {
        'shows': TVShow.objects.filter(id=id).values(),
    }
    return render(request, 'viewShow.html', context)

def editShow(request, id):
    context = {
        'show': TVShow.objects.get(id=id),
    }
    return render(request, 'editShow.html', context)

def updateShow(request, id):
    this_show = TVShow.objects.get(id=id)
    this_show.title = request.POST['titleBox']
    this_show.network = request.POST['networkBox']
    this_show.release_date = request.POST['releaseDateBox']
    this_show.description = request.POST['descBox']
    this_show.save()
    return redirect('/viewShows')

def removeShow(request, id):
    this_show = TVShow.objects.filter(id=id)
    this_show.delete()
    return redirect('/viewShows')