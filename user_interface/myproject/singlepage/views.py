from django.http import Http404, HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "singlepage/index.html")

texts = ["Text 1", "Text 2", "Text 3"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")
