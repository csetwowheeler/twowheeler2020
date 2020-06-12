from django.urls import path
from . import views

app_name = 'Insurance'
urlpatterns = [
    path('add_insurance', views.add_insurance, name='add_insurance'),
    path('insurance_detail', views.insurance_detail, name='insurance_detail'),
    path('process_insurance', views.process_insurance, name='process_insurance'),
    path('insurance_guidlines', views.insurance_guidlines, name='insurance_guidlines'),
    path('save_info', views.save_info, name='save_info'),
]
