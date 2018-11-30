from django.conf.urls import url
#from django.urls import path
from . import views
urlpatterns = [
    url(r'^$', views.signin),
    url(r'^register/$', views.register),
    url(r'^signin/$', views.signin),
    url(r'^logout/$',views.logout)
]