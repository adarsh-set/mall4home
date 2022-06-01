from django.urls import path,include

from home import views

urlpatterns = [
   path('',views.index,name='homepage'),
   path('login1/',views.log,name='loginpage'),
   path('reg/',views.reg,name='register'),
   path('login1/sublog/',views.sublog),
   path('reg/subreg/',views.subreg)
   #path('login/',views.)
]
