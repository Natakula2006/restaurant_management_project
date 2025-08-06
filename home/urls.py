from django.urls import path
from .views import home

urlpatterns = [
    path('',home,name='home'),
    path('api/menu/',MenuView.as_view(),name='menu'),
    
]