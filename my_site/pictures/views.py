from django.shortcuts import render, get_object_or_404
from .models import Picture
from .forms import PictureForm


def index(request, page=0):
    pictures = Picture.objects.all()

    page = int(page)
    start = page * 20
    end = (page + 1) * 20

    total = len(pictures)
    has_prev = page > 0
    prev = page - 1 if has_prev else None
    next = page + 1 if end < total else None

    pictures = pictures[start:end]

    return render(request, 'pictures/pictures-main.html', {"picture_list": pictures, 'has_prev': has_prev, 'prev': prev,
                                                           'next': next})


def colorado(request):
    photos = Picture.objects.filter(location='D')

    return render(request, 'pictures/colorado.html')


def new_york(request):
    photos = Picture.objects.filter(location='N')

    return render(request, 'pictures/ny.html')


def night(request):
    photos = Picture.objects.filter(location='B')
    return render(request, 'pictures/night.html')


def chittenango(request):
    photos = Picture.objects.filter(location='C')

    return render(request, 'pictures/chittenango.html')


def cars(request):
    photos = Picture.objects.filter(location='H')
    return render(request, 'pictures/cars.html', {'photo_list': photos})


def add_photo(request):
    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index/contact_submit.html')
    else:
        form = PictureForm()

    return render(request, 'admin_pictures/add_photo.html', {'form': form})


def edit_photo(request, photo_id):
    photo = get_object_or_404(Picture, pk=photo_id)

    if request.method == 'POST':
        results_form = PictureForm(request.POST, request.FILES, instance=photo)
        if results_form.is_valid():
            results_form.save()
            return render(request, 'admin_pictures/edit_photo.html', {'photo': photo})
    else:
        results_form = PictureForm(instance=photo)

    return render(request, 'admin_pictures/edit_photo.html', {'results_form': results_form, 'photo': photo})
