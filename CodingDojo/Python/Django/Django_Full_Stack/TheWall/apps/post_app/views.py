from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
from .models import *
# from apps.LogRegApp.models import*


def index(request):
    # if 'email' in request.session.keys():
    context = {
        'user':User.objects.get(email=request.session['email']),
        'post_data':Posts.objects.all(),
        'comment_data':Comments.objects.all(),
    }
    
    return render(request, 'WallIndex.html',context)   
    # return redirect('/success')

def success(request):
    context = {
        'user':User.objects.get(email=request.session['email']),
        'post_data':Posts.objects.all(),
        'comment_data':Comments.objects.all(),
    }
    
    return render(request, 'WallIndex.html',context)

def createPost(request):
    if Posts.objects.post_validator(request.POST, request):
        isValid = True
        user = User.objects.get(email=request.session['email']) # User.get gets one object. User.get gets an array of users
        request.session['email'] = user.email
        request.session['id'] = user.id
        Posts.objects.create(post=request.POST['postBox'], user = user, user_likes=False)
        messages.success(request,'Message posted successfully.')
        return redirect('/wall')
    else:
        isValid = False
        return redirect('/')

def comment(request):
    Comments.objects.create(comment=request.POST['commentBox'],user=User.objects.get(email=request.session['email']),post=request.POST.get('post_id'))
    return redirect('/success')

def delete_post(request, id):
    m = Posts.objects.get(id=id)
    m.delete()
    return redirect('/wall') 

def logout(request):
    request.session.clear()
    return redirect('/')