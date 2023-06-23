from django.urls import path

from . import views

urlpatterns = [
    path('', views.resources, name='resources'),
    path('<slug:slug>/', views.topic, name='topic'),
]