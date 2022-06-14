from django.shortcuts import render,redirect
from .models import pro_store
from home.models import comment
from django.contrib.auth.models import User
from django.core.cache import cache


# Create your views here.
# Cahce creating
def proindex(request):
    u_id=request.GET['id']
    if cache.get(u_id):
        print("DATA from CAHCE")
        pro_var=cache.get(u_id)
    else:
        print("DATA from DATABASE")
        pro_var = pro_store.objects.get(id = u_id)
        cache.set(u_id,pro_var)
    return render(request,'product.html',{'uid':pro_var})


def comm(request):
    user=request.GET['user']
    pro=request.GET['pro']
    com=request.GET['cmt']
    users= User.objects.get(id=user)
    commtvar = comment.objects.create(body=com,u_name=users.username,product_id=pro)
    commtvar.save();
    return redirect('/product/?id='+pro)
     