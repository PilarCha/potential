from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^login$',views.login),
    url(r'^create$',views.create),
    url(r'^add/(?P<number>\d+)', views.add),
    url(r'^logout$',views.logout),
    url(r'^delete/(?P<number>\d+)', views.remove),
    url(r'^show/(?P<number>\d+)', views.show),






]
