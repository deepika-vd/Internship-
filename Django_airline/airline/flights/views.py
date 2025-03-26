from django.shortcuts import render
from .models import Flight, Airport, Passenger

def index(request):
    return render(request, "flights/index.html", {    
        "flights": Flight.objects.all()
    })

def index_airline(request):
    return render(request, "flights/index_airline.html", {
        "airports": Airport.objects.all() 
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = Passenger.objects.all()

    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers
    })
