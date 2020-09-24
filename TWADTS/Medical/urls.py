from django.urls import path
from . import views

app_name = 'Medical'
urlpatterns = [
    path('add_medical_detail', views.add_medical_detail, name='add_medical_detail'),
    path('medical_history', views.medical_history, name='medical_history'),
]
