from django.http import response
from django.shortcuts import render

def home(request):
    return render(request, 'home/main.html')
def login(request):
    return render(request, 'login/login.html')

# Create your views here.
