from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def somi(request):
    return HttpResponse('hello somi')

def yesser(request):
    return HttpResponse('hello yasser')

def great(request, name):
    return render(request, "hello/great.html",{"name": name.capitalize()})