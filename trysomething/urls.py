from django.urls import path
from app1 import views
from django.contrib import admin
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
]