from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Nice!')
    # return render(request, 'products/index.html')
