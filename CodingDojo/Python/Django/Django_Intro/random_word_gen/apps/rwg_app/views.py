from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'rwg_app/index.html')

def random_word(request):

    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    
    ran_str = get_random_string(length = 14)

    context = {
        "random_word" : ran_str
    }

    return render(request, "rwg_app/index.html", context)

def reset(request):
    request.session.clear()
    return redirect('/')
