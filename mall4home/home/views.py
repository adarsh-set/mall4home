import email
from queue import Empty
from unicodedata import name
from django.contrib.auth.models import auth,User
from django.http import request
from product.models import pro_store
from django.shortcuts import render,redirect
# json import
from django.http.response import JsonResponse
from django.db.models.query_utils import Q
# Create your views here.


def index(request):
    pro = pro_store.objects.all()
    if request.method == "POST":
        se_el = request.POST['na']
        pro=pro_store.objects.filter(Q(p_name__istartswith=se_el))
        print(pro)
        if pro :
            return render(request,'index.html',{"pro": pro})
        else:
            pr="Sorry Not in Store"
            return render(request,'index.html',{"pr": pr})
    
    else:
        print("product : ",pro)
        # cookie getting
        if 'firname' in request.COOKIES:
            sam = request.COOKIES['firname']
            return render(request,'index.html',{"pro": pro,'em':sam})
        else:
            return render(request,'index.html',{"pro": pro})

def log(request):
    if request.method == "POST":
        user= request.POST['uname']
        pa_w = request.POST['p_w']
        valid = auth.authenticate(username = user,password= pa_w)
    
        if valid is not None:
            auth.login(request,valid)
            fistname=User.objects.get(username=user)
            # cookie fetching
            re_dir=redirect('/')
            re_dir.set_cookie('firname',fistname.first_name)
            re_dir.set_cookie('valid',True)
            return re_dir
        
        else:
            msg="invalid username and password"
            return render(request,'login.html',{"lng": msg})
    else:    
        return render(request,'login.html')


def reg(request):
    if request.method == "POST":
        userw= request.POST['uname']
        f_name= request.POST['fname']
        l_name= request.POST['lname']
        emai= request.POST['email']
        pa_wo= request.POST['p_w']
        repa_wo= request.POST['re-p_w']
        if userw != '' and emai != '' and pa_wo != '':
            if User.objects.filter(username = userw).exists() or User.objects.filter(email = emai).exists():
                msg="user name or email already taken"
                return render(request,'register.html',{"lnge": msg})
            elif pa_wo != repa_wo:
                msg="re-password not same"
                return render(request,'register.html',{"lnge": msg})
            else:
                user = User.objects.create_user(username = userw,first_name = f_name,last_name = l_name,email = emai,password = pa_wo)
                user.save();
                auth.login(request,user)
                return redirect('/')
        else:
            msg="invalid"
            return render(request,'register.html',{"lnge": msg})
    else:    
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    #cookie delete
    cook_del = redirect("/")   
    cook_del.delete_cookie('firname') 
    cook_del.delete_cookie('valid') 
    return cook_del
    

def sera(request):
    if 'term' in request.GET:
        s_e = request.GET['term']
        print(s_e)
        ob_s = pro_store.objects.filter(Q(p_name__istartswith=s_e))
        ali=[]
        for i in ob_s:
            ali.append(i.p_name)
        return JsonResponse(ali,safe=False)
    return redirect("/")
 
 
 
