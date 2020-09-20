from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'Tracking'
urlpatterns = [
    # path('map', views.map, name='map'),

    path('map', TemplateView.as_view(template_name="live_tracking/maps.html"),
         name='map'),

    path('live_tracking', views.live_tracking, name='live_tracking'),
    path('tracking_history', views.tracking_history, name='tracking_history'),
    path('attach_new_device', views.attach_new_device, name='attach_new_device'),
    path('all_devices', views.all_devices, name='all_devices'),

]
