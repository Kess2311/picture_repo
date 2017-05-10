from django.shortcuts import render
import os
from django.conf import settings

def home(request):
    return render(request, 'index/index.html')

def about_page(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'media/lucas_resume.pdf')
    return render(request, 'index/about.html', {'file':file_path})


def contact_me(request):
    return render(request, 'index/contact.html')
