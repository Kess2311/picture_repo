from django.conf.urls import url

from . import views

app_name = 'pictures'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chittenango/$', views.chittenango, name='chittenango'),
    url(r'^new_york/$', views.new_york, name='new_york'),
    url(r'^night/$', views.night, name='night'),
    url(r'^colorado/$', views.colorado, name='colorado'),
]
