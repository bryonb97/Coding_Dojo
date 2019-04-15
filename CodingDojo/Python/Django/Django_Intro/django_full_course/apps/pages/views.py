from django.shortcuts import render, HttpResponse

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")
    # return render(request, 'pages/index.html')

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")