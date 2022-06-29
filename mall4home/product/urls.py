from django.urls import path,include
from product import views


urlpatterns = [
    path('', views.proindex2),
    path('comment/',views.comm),
    path('mail/',views.sam),
]