
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
     path('',views.home,name='home'),
     path('registration/',include('registration.urls')),
     path('faqs/',views.faqs,name='faqs'),
     path('about/',views.about,name='about'),
     path('map/',views.map,name='map'),
     path('signin/',include('signin.urls')),
     path('appointment/',views.appointment,name='appointment')
     
]