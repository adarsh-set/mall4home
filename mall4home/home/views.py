import email
from queue import Empty
from django.contrib.auth.models import auth,User
from django.http import request
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')
def log(request):
    if request.method == "POST":
        user= request.POST['uname']
        pa_w = request.POST['p_w']
        valid = auth.authenticate(username = user,password= pa_w)
    
        if valid is not None:
            auth.login(request,valid)
            return redirect('/')
        else:
            msg="invalid username and password"
            return render(request,'login.html',{"lng": msg})
    else:    
        return render(request,'login.html')
def reg(request):
    print("re :",request)
    return render(request,'register.html')
def subreg(request):
    userw= request.GET['uname']
    f_name= request.GET['fname']
    l_name= request.GET['lname']
    emai= request.GET['email']
    pa_wo= request.GET['p_w']
    repa_wo= request.GET['re-p_w']
    if userw != '' and emai != '' and pa_wo != '':
        if User.objects.filter(username = userw).exists() or User.objects.filter(email = emai).exists():
            msg="user name or email already taken"
            return render(request,'register.html',{"lnge": msg})
        else:
            return redirect(request,'/')
    else:
        msg="invalid"
        return render(request,'register.html',{"lnge": msg})
def logout(request):
    auth.logout(request)
    return redirect('/')
