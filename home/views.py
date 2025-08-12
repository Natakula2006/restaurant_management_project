from django.contrib import settings
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    try:
    
        context = {'restaurant_name':getattr(settings,'RESTAURANT_NAME','My Restaurant'),'phone-number':getattr(settings,'RESTAURANT_PHONE_NUMBER','Not available')}
        return render(request,'home.html',context)
    except Exception as e:
        return HttpResponse(f"An error occured: {e}",status= 500)
def about(request):
    try:
        return render(request,'about.html')
    except Exception as e:
        return HttpResponse(f"An error occured: {e}",status = 500)

def contact_view(request):
    try:
        return render(request,'contact.html')
    except Exception as e:
        return HttpResponse(f"An error occured: {e}",status = 500)
def reservations(request):
    try:
        return render(request,'reservations.html')
    except Exception as e:
        return HttpResponse(f"An error occured: {e}",status= 500)

