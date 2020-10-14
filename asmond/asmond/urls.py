from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('login.urls')),
    path('framework/', include('framework.urls')),
    path('interface/', include('interface.urls')),
    path('login/', include('login.urls')),
    path('settings/', include('settings.urls')),
    path('admin/', admin.site.urls),
]
