from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def Tutorials(request):
    return render(request,'tutorials.html')
def Exercises(request):
    return render(request,'Exercises.html')
def Certificate(request):
    return render(request,'Certificate.html') 
