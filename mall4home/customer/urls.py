from django.urls import path,include

from customer import views

urlpatterns = [
   path('',views.log,name='loginpage')
]