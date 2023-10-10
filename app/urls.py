from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('', views.home, name="home"),
    path('evaluate', views.evaluate, name="evaluate"),
    
]
