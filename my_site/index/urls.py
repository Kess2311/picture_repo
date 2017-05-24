from django.conf.urls import url
from . import views

app_name = 'index'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about_page, name='about_me'),
    url(r'^contact/$', views.contact_page, name='contact_me'),
    url(r'^contact_submit/$', views.contact_submit, name='contact_submit'),
    url(r'^view_forms/$', views.view_forms, name='view_forms'),

]
