from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def work(request):
    return render(request, 'work.html')

def error(request):
    return render(request, 'error.html')

def noadmin(request):
    return render(request, 'noadmin.html')