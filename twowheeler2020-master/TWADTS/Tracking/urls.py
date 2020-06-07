from django.urls import path
from . import views

app_name = 'Tracking'
urlpatterns = [
    path('live_tracking', views.live_tracking, name='live_tracking'),
    path('tracking_history', views.tracking_history,name='tracking_history'),
    path('attach_new_device', views.attach_new_device,name='attach_new_device'),
    path('all_devices', views.all_devices,name='all_devices'),

]
