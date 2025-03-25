from django.shortcuts import render
from django import forms 

class newform(forms.Form):
    task=forms.CharField(label="addtask")
context=["diya",'ayra','vikky']
def index(request):
   
    return render(request,"hello/display_task.html",{"tasks":context})

def add(request):
    if request.method=='POST':
        form= newform(request.POST)
        
        if form.is_valid():
            task=form
            context.append(task)
        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "hello/add.html", {
                "form": form
            })

    return render(request, "hello/add.html", {
        "form": newform()
    })