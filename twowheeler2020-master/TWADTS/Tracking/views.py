from django.shortcuts import render

# Create your views here.
def live_tracking(request):

    return render(request, 'live_tracking/live-tracking.html')

def tracking_history(request):

    return render(request, 'live_tracking/tracking-history.html')

def attach_new_device(request):

    return render(request, 'live_tracking/devices/attached_new.html')

def all_devices(request):

    return render(request, 'live_tracking/devices/all_devices.html')
