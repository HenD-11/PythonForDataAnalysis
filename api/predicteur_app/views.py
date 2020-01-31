from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # This is a view
    return HttpResponse("Your are on the main page: isn't it beautiful ?")