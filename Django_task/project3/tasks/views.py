from django.shortcuts import render

def index(request):
    context=["diya",'ayra','vikky']
    return render(request,"hello/display_task.html",{"tasks":context})

def add(request):
    return render(request, "hello/add.html")