from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from registration.models import Register
# Create your views here.
def register(request):
    obj = Register()
    if request.method == 'POST':
        obj.fname = request.POST.get('fname')
        obj.lname = request.POST.get('lname')
        obj.email = request.POST.get('email')
        obj.phone = request.POST.get('phone')
        obj.date  = request.POST.get('date')
        obj.gender = request.POST.get('gender')
        obj.aadhar = request.POST.get('aadhar')
        obj.weight = request.POST.get('weight')
        obj.blood_group = request.POST.get('blood_group')
        obj.address = request.POST.get('address')
        obj.username = request.POST.get('username')
        obj.password = request.POST.get('password')
        obj.medications = request.POST.get('medications')
        obj.message = request.POST.get('message')
        obj.save()
        return redirect('/')
    return render(request,'registration.html')


    

