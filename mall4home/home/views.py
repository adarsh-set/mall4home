from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def log(request):
    return render(request,'login.html')
def reg(request):
    print("re :",request)
    return render(request,'register.html')
def sublog(request):
    user= request.GET['uname']
    pa_w = request.GET['p_w']
    print("usrname :",user,"\npassword :",pa_w)
    return render(request,'web(djano 1st).html')
def subreg(request):
    return render(request,'web(djano 1st).html')
