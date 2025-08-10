from django.contrib import settings
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'restaurant_name':getattr(settings,'RESTAURANT_NAME','My Restaurant'),'phone-number':getattr(settings,'RESTAURANT_PHONE_NUMBER','Not available')}
    return render(request,'home.html',context)
def about(request):
    return render(request,'about.html')
def contact_view(request):
    request render(request,'contact.html')

