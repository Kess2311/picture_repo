from django.conf.urls import url
from . import views

app_name = 'index'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about_page, name='about_me'),
    url(r'^contact/$', views.contact_me, name='contact_me'),

]
