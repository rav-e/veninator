from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Appointment
# Create your views here.
def home(request):
    return render(request,'home.html')

def faqs(request):
    return render(request,'faqs.html')

def about(request):
    return render(request,'about.html')

def map(request):
    return render(request,'map.html')

def appointment(request):
    obj = Appointment()
    if request.method == 'POST':
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.location = request.POST.get('location')
        obj.date = request.POST.get('date')
        obj.vaccine = request.POST.get('vaccine') 
        obj.time = request.POST.get('time')
        obj.save()
       
    return HttpResponse("Success")