from django.shortcuts import render
from django.http import HttpResponse
from . models import login

# Create your views here.
def Account(request):
    email=request.GET.get('email')
    password=request.GET.get('password')
    e=login(email=email,password=password)
    e.save()
    return render(request,'SignUp.html')
def Auth(request):
    email=request.GET.get('email')
    password=request.GET.get('password')
    res=login.objects.all().values()
    print(res)
    if res[0]['email']==email and res[0]['password']==password:
        return render(request,'w3.html')
    else:
        return HttpResponse("Error matched email and password")
def Login(request):
    return render(request,'login.html') 
def Signup(request):
    return render(request,'SignUp.html')