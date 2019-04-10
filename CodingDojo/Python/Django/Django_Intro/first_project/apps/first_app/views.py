from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder")

def new(request):
    return HttpResponse("placeholder")

def create(request):
    return redirect("/")

def show(request, num):
    return HttpResponse("placeholder to display blog number {num}")

def edit(request, num):
    return HttpResponse("placeholder to edit blog number {num}")

def delete(request, num):
    return redirect("/")