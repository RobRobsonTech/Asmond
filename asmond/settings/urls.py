from django.urls import path
from . import views

app_name = "settings"
urlpatterns = [
    path('', views.settings, name='settings'),
]
