from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
# Create your views here.
def newShow(request):
    return render(request, 'index.html')

def createShow(request):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = TVShow.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/newShow')
    else:
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
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = TVShow.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.warning(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/editShow'+id)
    else:
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