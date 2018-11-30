from django.conf.urls import url
#from django.urls import path
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^newpost/$',views.new),
    url(r'^update/$',views.update),
    url(r'^delete/$',views.delete),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^posts/$',views.posts)
]
