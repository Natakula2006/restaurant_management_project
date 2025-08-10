from django.urls import path
from .views import menu_home

urlpatterns = [
    path('',menu_home,name='menu_home'),
    path('api/menu/',MenuView.as_view(),name='menu'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact_view,name='contact'),
    
]