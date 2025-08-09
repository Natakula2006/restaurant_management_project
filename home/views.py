from django.contrib import settings
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'restaurant_name':settings.RESTAURANT_NAME}
    return render(request,'home.html',context)
