from django.shortcuts import render, redirect
from ..models import *

def Principal(request):

    return render(request,'index.html')

def Prueba(request):

    return render(request,'prueba.html')