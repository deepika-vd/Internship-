from django.shortcuts import render
import datetime

def index(request):
    now=datetime.datetime.now()
    return render(request , "hello/inde.html",{
        
        "newyear":now.day==1 and now.month==1
        
    })
# Create your views here.
