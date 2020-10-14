from django.urls import path
from . import views

app_name = "interface"
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('homepage', views.homepage, name='homepage'),
    path('map', views.networkmap, name='networkmap'),
    path('devices', views.networkdevices, name='networkdevices'),
    path('problems', views.networkproblems, name='networkproblems'),
]
