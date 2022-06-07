from django.shortcuts import render
from .models import pro_store
# Create your views here.
def proindex(request):
    u_id=request.GET['id']
    pro_var = pro_store.objects.get(id = u_id)
    return render(request,'product.html',{'uid':pro_var})
     