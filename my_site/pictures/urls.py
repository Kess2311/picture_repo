from django.conf.urls import url

from . import views

app_name = 'pictures'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chittenango/$', views.chittenango, name='chittenango'),
    url(r'^new_york/$', views.new_york, name='new_york'),
    url(r'^night/$', views.night, name='night'),
    url(r'^colorado/$', views.colorado, name='colorado'),
    url(r'^cars/$', views.cars, name='cars'),
    url(r'^add_photo/$', views.add_photo, name='add_photo'),
    url(r'^edit_photo/(?P<photo_id>[0-9]+)/$', views.edit_photo, name='edit_photo')
]
