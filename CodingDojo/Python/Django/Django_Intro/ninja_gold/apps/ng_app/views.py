from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'total_buckaroos' not in request.session or 'activities' not in request.session:
        request.session['total_buckaroos'] = 0
        request.session['activities'] = []
    return render(request, 'ng_app/index.html')

def process_money(request):
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            buckaroos = random.randint(10, 21)
            request.session['activities'].append('You are earned ' + str(buckaroos) + ' buckaroos from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['building'] == 'cave':
            buckaroos = random.randint(5, 11)
            request.session['activities'].append('You are earned ' + str(buckaroos) + ' buckaroos from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        elif request.POST['building'] == 'house':
            buckaroos = random.randint(2,6)
            request.session['activities'].append('You are earned ' + str(buckaroos) + ' buckaroos from the ' + request.POST['building'] + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        else:
            buckaroos = random.randint(-50, 51)
            if buckaroos >= 0:
                request.session['activities'].append('Entered a casino and earned ' + str(buckaroos) +' buckaroos' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
            else:
                request.session['activities'].append('Entered a casino and lost ' + str(buckaroos) + ' buckaroos... Oof...' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')

        request.session['total_buckaroos'] += buckaroos

    return redirect('/')

def reset(request):
    if request.method == "POST":
        request.session['total_buckaroos'] = 0
        request.session['activities'] = []
    return redirect('/')