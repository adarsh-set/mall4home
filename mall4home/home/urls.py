from django.urls import path,include
from product.feed import pro_feed
from home import views

urlpatterns = [
   path('',views.index,name='homepage'),
   path('login1/',views.log,name='loginpage'),
   path('reg/',views.reg,name='register'),
   path('logout/',views.logout),
   path('search/',views.sera,name="ser"),
   # Feed
   path('feed/',pro_feed(),name="feed"),
   path('mail2/',views.sam),
   
]
