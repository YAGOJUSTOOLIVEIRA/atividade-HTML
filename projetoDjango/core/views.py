from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def lista(request):
    return render(request, "lista.html")

def login(request):
    return render(request, "login.html")

def area_aluno(request):
    pass

# Create your views here.
 