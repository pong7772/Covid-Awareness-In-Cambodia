from django.http import response
from django.shortcuts import render

def home(request):
    return render(request, 'home/main.html')
def login(request):
    return render(request, 'login/login.html')
def signup(request):
    return render(request, 'signup/signup.html')
def covid(request):
    return render(request, 'covid/covid.html')
# Create your views here.
