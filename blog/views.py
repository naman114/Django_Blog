from django.shortcuts import render
from django.http import HttpResponse

# Function to handle traffic from our home. Returns what the user will see


def home(request):
    return HttpResponse("<h1>Blog Home</h1>")


def about(request):
    return HttpResponse("<h1>Blog About</h1>")
