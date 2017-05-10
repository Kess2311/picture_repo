from django.shortcuts import render


def index(request):
    return render(request, 'pictures/pictures-main.html')


def colorado(request):
    return render(request, 'pictures/colorado.html')


def new_york(request):
    return render(request, 'pictures/ny.html')


def night(request):
    return render(request, 'pictures/night.html')


def chittenango(request):
    return render(request, 'pictures/chittenango.html')
