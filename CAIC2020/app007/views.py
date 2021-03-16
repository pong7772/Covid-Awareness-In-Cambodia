from django.http import response
from django.shortcuts import render

def home(request):
    return render(request, 'home/main.html')


# Create your views here.
