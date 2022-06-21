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


#session creating

def proindex2(request):
    pro_id=request.GET['id']
    pro_var = pro_store.objects.get(id = pro_id)
    if 'priortiy_sess' in request.session:
        if pro_id in request.session['priortiy_sess']:
            request.session['priortiy_sess'].remove(pro_id)
        sess_pro = pro_store.objects.filter(id__in=request.session['priortiy_sess'])
        #pro_sort=sorted(sess_pro,key=lambda x: request.session['priortiy_sess'].index(x.id))
        print("sess store",sess_pro)
        
        request.session['priortiy_sess'].insert(0,pro_id)
        if len(request.session['priortiy_sess']) >  4 :
            request.session['priortiy_sess'].pop()
        print(request.session['priortiy_sess'])
    else:
        request.session['priortiy_sess'] = [pro_id] 
        sess_pro = pro_store.objects.filter(id = pro_id)
    request.session.modified = True
    return render(request,'product.html',{'uid':pro_var,'s_pr':sess_pro})
    
def comm(request):
    user=request.GET['user']
    pro=request.GET['pro']
    com=request.GET['cmt']
    users= User.objects.get(id=user)
    commtvar = comment.objects.create(body=com,u_name=users.username,product_id=pro)
    commtvar.save();
    return redirect('/product/?id='+pro)
     