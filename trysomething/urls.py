from django.urls import path
from app1 import views
  
urlpatterns = [
    path("", views.null),
    path("index/<int:id>", views.index),
    path("access/<int:age>", views.access),
]