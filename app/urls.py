
from django.urls import path,include
from app import views

urlpatterns = [

    path('',views.home),
    path('real/',views.realdata)
   
]