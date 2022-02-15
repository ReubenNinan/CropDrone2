from django.shortcuts import render
from .models import GPSData

# Create your views here.

def plants(request, pk_test):
    dests = GPSData.objects.all()
    customer = GPSData.objects.filter(user_name=pk_test)
    return render(request, "DataPage.html", {'dests': dests})
