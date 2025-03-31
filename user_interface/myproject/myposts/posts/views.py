import time
from django.http import JsonResponse
from django.shortcuts import render

# Render HTML page
def index(request):
    return render(request, "posts/index.html")

# Load more posts dynamically
def posts(request):
    # Get start and end points from query parameters
    start = int(request.GET.get("start", 0))
    end = int(request.GET.get("end", start + 19))  # Load 20 posts

    # Generate posts dynamically
    data = [f"Post #{i}" for i in range(start, end + 1)]

    # Artificial delay to simulate loading time
    time.sleep(1)

    return JsonResponse({"posts": data})

