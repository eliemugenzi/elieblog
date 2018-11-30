from django.conf.urls import url
#from django.urls import path
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^details/$', views.detail),
    url(r'^bookmark/$',views.bookmark),
    url(r'^posts/$',views.posts),
    url(r'^comment/$',views.comment)
]
