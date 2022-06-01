from django.contrib.auth.models import auth
from django.http import request
from django.shortcuts import render,redirect

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
    valid = auth.authenticate(username = user,password= pa_w)
    #print("authentication :", valid)
    if valid is not None:
        auth.login(request,valid)
        return redirect('/')
    else:
        msg="invalid username and password"
    #print("usrname :",user,"\npassword :",pa_w)
        return render(request,'login.html',{"lng": msg})
def subreg(request):
    return render(request,'web(djano 1st).html')
def logout(request):
    auth.logout(request)
    return redirect('/')
