from django.shortcuts import render,redirect
from .models import pro_store
from home.models import comment



# Create your views here.
def proindex(request):
    u_id=request.GET['id']
    pro_var = pro_store.objects.get(id = u_id)
    return render(request,'product.html',{'uid':pro_var})
def comm(request):
    user=request.GET['user']
    pro=request.GET['pro']
    com=request.GET['cmt']
    commtvar = comment.objects.create(body=com,u_name=user,product_id=pro)
    commtvar.save();
    return redirect('/')
     