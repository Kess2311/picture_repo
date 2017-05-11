from django.shortcuts import render, redirect, get_object_or_404

import os, re
from django.conf import settings
from .forms import ContactForm
from .models import Contact


def home(request):
    main_photo = os.path.join(settings.MEDIA_ROOT, 'media/Church_sunset.jpg')
    return render(request, 'index/index.html', {'sunset': main_photo})


def about_page(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'media/lucas_resume.pdf')
    return render(request, 'index/about.html', {'file': file_path})


def contact_page(request):
    form = ContactForm()
    return render(request, 'index/contact.html', {'form': form})


def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index/contact_submit.html')
    else:
        form = ContactForm()

    return render(request, 'index/contact.html', {'form': form})


def view_forms(request):

    if request.method == 'POST':
        id = re.sub("[^0-9]", "", request.POST.get("message", ""))
        message = get_object_or_404(Contact, pk=id)
        message.read = True
        message.save()
        form_list = Contact.objects.filter(read=False)
        return render(request, 'index/view_contact_forms.html', {'form_list': form_list})
    else:
        form_list = Contact.objects.filter(read=False)
        return render(request, 'index/view_contact_forms.html', {'form_list': form_list})


